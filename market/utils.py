import traceback
import functools

from django.db import transaction
from django.http import JsonResponse


JSON_DUMPS_PARAMS = {
    'ensure_ascii': False
}


def ret(json_object, status=200):
    """Отдает JSON с правильным HTTP заголовками и в читаемом
    в браузере виде."""
    return JsonResponse(
        json_object,
        status=status,
        safe=not isinstance(json_object, list),
        json_dumps_params=JSON_DUMPS_PARAMS
    )


def error_responce(exception):
    """Форматирует HTTP ответ с описанием ошибки и Traceback'ом"""
    res = {
        'error_message': str(exception),
        'traceback': traceback.format_exc()
        }
    return ret(res, status=400)


def base_view(fn):
    """Декоратор для всех views, для обработки исключений"""
    @functools.wraps(fn)
    def wrapper(request, *args, **kwargs):
        try:
            with transaction.atomic():
                return fn(request, *args, **kwargs)
        except Exception as e:
            return error_responce(e)
    return wrapper