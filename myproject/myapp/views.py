from django.shortcuts import render
import logging
from django.http import HttpResponse
from random import randint, choice

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse("Hello, world!")


def about(request):
    try:
        # some code that might raise an exception
        result = 1 / 0
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse("Oops, something went wrong.")
    else:
        logger.debug('About page accessed')
        return HttpResponse("This is the about page.")


def heads_and_tails(request):
    logger.info('Сработала функция подбрасывании монеты')
    return HttpResponse(choice(['Орел', 'решка']))


def cube(request):
    logger.info('Выпала одна из граней куба')
    return HttpResponse(str(randint(1, 7)))


def random_choice(request):
    logger.info('Сработала функция случайного числа')
    return HttpResponse(str(randint(1, 100)))


def home(request):
    html = '''<title>Главная страница</title>
              <h1>Это главная страница</h1>
              <p1>Моя первый DJANGO проект</p1>
    '''
    logger.info('Запустили главную  страницу home')
    return HttpResponse(html)


def about_me(request):
    html = '''<title>О СЕБЕ</title>
             <h1>Информация обо мне</h1>
             <p1>Я студент 3 курса университета в городе Ростов-На-Дону. </p1>
             <p2>Мне 20 лет и я хочу стать высококачественным it-специалистом</p2>
    '''
    logger.info('запустили страницу с информации обо мне about_me')
    return HttpResponse(html)
