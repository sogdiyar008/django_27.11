from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    ip = request.META['REMOTE_ADDR']
    path = request.path

    return HttpResponse(f'host:    {host}<br><br>'
                        f'Browser:   {user_agent}<br><br>'
                        f'IP:   {ip}<br><br>'
                        f'Path:   {path}<br><br>')


def error(request):
    return HttpResponse(f'К сожалению произошла ошибка',  status=404,reason='OSHIBKA U TEBYA')


def user(request,login='Noname', directory='Noname dir', number_post='Unknown_number'):
    return HttpResponse(f'Your Login:  {login}<br><br>'
                        f'Directory  {directory}<br><br>'
                        f'Number of directory:  {number_post}<br><br>')
