"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

from django.db import models
from .models import Comment, Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Логин'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class FeedbackForm(forms.Form):
    """Класс для формы обратной связи"""
    name = forms.CharField(label='Ваше имя', min_length=2, max_length=40)
    rating = forms.ChoiceField(label='Оцените наш сайт',
                               choices=[('1','Плохо'), ('2','Нормально'), ('3','Хорошо')],
                               widget=forms.RadioSelect, initial=2)
    type = forms.ChoiceField(label='Выберите тип обращения',
                             choices=(('1','Отзыв'),
                                      ('2','Предложение'),
                                      ('3','Претензия')), initial = 1)
    message = forms.CharField(label='Ваш отзыв',
                              widget=forms.Textarea(attrs={'rows':10,'cols':50}))
    email = forms.CharField(label='Ваш адрес электронной почты', min_length=6, max_length=40)
    notice = forms.BooleanField(label='Желаете получить ответ на ваш отзыв через e-mail?',
                                required=False)

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text

class BlogForm (forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'posted', 'author', 'image',)
        labels = {'title': "Заголовок", 'description': "Краткое описание", 'content': "Содержание", 'posted': "Дата", 'author': "Автор", 'image': "Изображение"}
