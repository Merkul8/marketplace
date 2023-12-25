from django import forms
from .models import Review


class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('description', 'image', 'estimate',)
        widgets = {
            'description': forms.Textarea(attrs={"rows": 1, 'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'type': 'file'}),
        }