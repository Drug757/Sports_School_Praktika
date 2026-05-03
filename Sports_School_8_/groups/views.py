from django.shortcuts import render
from .models import Group


def group_list(request):
    """
    Отображает список всех групп.
    Получает данные из базы и передаёт их в шаблон.
    """
    groups = Group.objects.all() # получение данных из базы

    return render(
        request,
        "groups/list.html",
        {"groups": groups},
    )