from django.core.mail import send_mail
from marketplace.celery import app


@app.task
def send_mail_before_sing_in(person_mail, username):
    send_mail('Добро пожаловать!', 
              f'Добрый день {username}, спасибо за регистрацию! Теперь вы можете покупать наши товары!', 
              'test.maksim99@gmail.com', 
              [person_mail]
            )
    

@app.task
def send_mail_for_sellers(person_mail, username):
    send_mail('Приветствуем в качестве продавца!', 
              f'Добрый день {username}, спасибо за сотрудничество! Теперь вы можете кроме\
                того что покупать наши товары, и продавать свою продукцию!', 
              'test.maksim99@gmail.com', 
              [person_mail]
            )
    

@app.task
def send_mail_before_add_product(person_mail, username):
    send_mail('Товар успешно добавлен!', 
              f'Добрый день {username}, спасибо за сотрудничество! Ваш товар виден другим пользователям,\
                  теперь они могут его приобрести!', 
              'test.maksim99@gmail.com', 
              [person_mail]
            )
    

@app.task
def send_mail_befor_add_review(person_mail, username):
    send_mail('Нам важно ваше мнение!', 
              f'Добрый день {username}, спасибо за ответственный подход! Ваш отзыв поможет\
                  в продвижении нашего маркетплейса!', 
              'test.maksim99@gmail.com', 
              [person_mail]
            )