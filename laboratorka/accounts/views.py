#render - объединяет html-шаблон с данными и возвращает http-ответ
from django.shortcuts import render

#импортирует класс для перенаправления пользователя на другой url после успешной регистрации
from django.http import HttpResponseRedirect

#импортируем ф-ии login, logout для управления аутентификацией пользователя
from django.contrib.auth import login, logout

#импортируем стандартную форму регистрации
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


#представление для регистрации новго пользователя
#обрабатывает get-запрос (показать пустую форму) и post-запрос (принять данные, создать пользователя)
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) #если отправил форму - создаем экземпляр формы и заполняем данные
        if form.is_valid():
            user = form.save() #хеширует пароль и возвращает объект user
            login(request, user) #выполняем вход в этого пользователя
            return HttpResponseRedirect('/articles') #после успешной регистрации - перенаправление на страницу со статьями
    else: #обработка get-запроса
        form = UserCreationForm() #создание пустой формы без данных
    return render(request, 'accounts/signup.html', {'form': form}) #рендер шаблона и его вывод

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect('/articles')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return HttpResponseRedirect('/articles')