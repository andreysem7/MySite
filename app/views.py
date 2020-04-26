"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from .forms import FeedbackForm

from django.db import models
from .models import Blog, Comment

from .forms import CommentForm, BlogForm # использование формы ввода комментария


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Домашняя страница',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Контактные данные:',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О нас',
            'year':datetime.now().year,
        }
    )

def links (request):
    """ """
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/links.html',
        {
            'title':'Полезные ресурсы',
            'message':'Здесь содержаться ссылки на полезные сайты.',
            'year':datetime.now().year,
        }
    )

def pool (request):
    """ """
    assert isinstance(request, HttpRequest)
    
    data = None
    rating = {'1': 'Плохо', '2': 'Нормально', '3': 'Хорошо'}
    type = {'1': 'Отзыв', '2': 'Предложение', '3': 'Претензия'}

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['rating'] = rating[form.cleaned_data['rating']]
            data['type'] = type[form.cleaned_data['type']]
            data['message'] = form.cleaned_data['message']
            if(form.cleaned_data['notice'] == True):
                data['notice'] = 'Да'
            else:
                data['notice'] = 'Нет'
            data['email'] = form.cleaned_data['email']
            form = None
    else:
        form = FeedbackForm()

    return render(
        request,
        'app/pool.html',
        {
            'title':'Обратная связь',
            'form':form,
            'year':datetime.now().year,
            'data':data
        }
    )

def registration(request):
    """Renders the registration page."""

    if request.method == "POST": # после отправки формы
        regform = UserCreationForm (request.POST)
        if regform.is_valid(): #валидация полей формы
            reg_f = regform.save(commit=False) # не сохраняем автоматически данные формы
            reg_f.is_staff = False # запрещен вход в административный раздел
            reg_f.is_active = True # активный пользователь
            reg_f.is_superuser = False # не является суперпользователем
            reg_f.date_joined = datetime.now() # дата регистрации
            reg_f.last_login = datetime.now() # дата последней авторизации
            reg_f.save() # сохраняем изменения после добавления данных
            return redirect('home') # переадресация на главную страницу после регистрации

    else:
        regform = UserCreationForm() # создание объекта формы для ввода данных нового пользователя

    assert isinstance(request, HttpRequest)
    return render(
    request,
    'app/registration.html',
        {
        'regform': regform, # передача формы в шаблон веб-страницы
        'year':datetime.now().year,
        }
    )

def blog(request):
    """Renders the blog page."""
    posts = Blog.objects.all() # запрос на выбор всех статей блога из модели

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blog.html',
           {
            'title':'Блог',
            'posts': posts, # передача списка статей в шаблон веб-страницы
            'year':datetime.now().year,
            }
    )

def blogpost(request, parametr):
    """Renders the blogpost page."""
    post_1 = Blog.objects.get(id=parametr) # запрос на выбор конкретной статьи по параметру
    comments = Comment.objects.filter(post=parametr)

    if request.method == "POST": # после отправки данных формы на сервер методом POST

        form = CommentForm(request.POST)

        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user # добавляем (так как этого поля нет в форме) в модель Комментария (Comment) в поле автор авторизованного пользователя
            comment_f.date = datetime.now() # добавляем в модель Комментария (Comment) текущую дату
            comment_f.post = Blog.objects.get(id=parametr) # добавляем в модель Комментария (Comment) статью, для которой данный комментарий
            comment_f.save() # сохраняем изменения после добавления полей
            return redirect('blogpost', parametr=post_1.id) # переадресация на ту же страницу статьи после отправки комментария
    else:
        form = CommentForm() # создание формы для ввода комментария

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blogpost.html',
            {
            'post_1': post_1, # передача конкретной статьи в шаблон веб-страницы
            'comments': comments, # передача всех комментариев к данной статье в шаблон веб-страницы
            'title':'Блог',
            'form': form, # передача формы добавления комментария в шаблон веб-страницы
            'year':datetime.now().year,
            }
            )

def newpost(request):
    """Renders the newpost page."""

    if request.method == "POST":
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()

            blog_f.save()

            return redirect('blog')
    
    else:
        blogform = BlogForm()

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/newpost.html',
            {
            'blogform': blogform,
            'year':datetime.now().year,
            }
            )

def videopost(request):
    """Renders the videopost page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/videopost.html',
        {
            'title':'Раздел видео',
            'message':'Страница с коллекцией видео.',
            'year':datetime.now().year,
        }
    )