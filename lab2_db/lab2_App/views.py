from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from lab2_App.database import Database
from lab2_App.forms import *

db = Database()


def index(request):
    db.connect()
    return render(request, "index.html")


def insert(request):
    form = Form_game()
    admin_T = request.POST.get('admin_True')
    if admin_T == 'True':
        return HttpResponseRedirect('/insert_admin/')
    else:
        return render(request, 'insert.html', {'form': form})


def insert_admin(request):
    form3 = Form_customer()
    form1 = Form_stadium()
    form2 = Form_game()
    return render(request, 'admin.html', {'form1': form1, 'form2': form2, 'form3': form3, })


def insert_post(request):
    try:
        game_id = request.POST.get('dropdown1')
        name = request.POST.get("name_insert")
        surname = request.POST.get("surname_insert")
        number = request.POST.get("number_insert")
        if request.POST.get("vip_insert") == "True":
            VIP = 'true'
        else:
            VIP = 'false'
        db.add_customer(name, surname, number, VIP)
        db.add_fact(name, surname, game_id)
        return HttpResponseRedirect("/")
    except:
        return render(request, "error_page.html")


def post_admin_add(request):
    team1 = request.POST.get('team1')
    team2 = request.POST.get('team2')
    datetime = request.POST.get('datetime')
    price = request.POST.get('price')
    stadium_id = request.POST.get('dropdown2')
    teams = team1 + '-' + team2
    db.add_game(teams, stadium_id, datetime, price)
    return HttpResponseRedirect(reverse('insert_admin'))

def post_admin_del(request):
    game_id = request.POST.get('dropdown3')
    db.del_game(game_id)
    return HttpResponseRedirect(reverse('insert_admin'))

def post_admin_edit(request):
    game_id = request.POST.get('dropdown4')
    stadium_id = request.POST.get('dropdown5')
    price = request.POST.get('price')
    datetime = request.POST.get('datetime')
    db.edit_game(game_id, stadium_id, datetime, price)
    return HttpResponseRedirect(reverse('insert_admin'))

def post_admin_search(request):
    froms = request.POST.get('from')
    to = request.POST.get('to')
    context = {
        'form4': db.select_games_range(froms,to)
    }
    return render(request, 'admin.html', context)

def admin_update(request):
    return HttpResponseRedirect(reverse('insert_admin'))

def search_word(request):
    word = request.POST.get('word')
    context = {
        'form5': db.fulltext_find_word(str(word))
    }
    return render(request, 'admin.html', context)

def search_string(request):
    stt = request.POST.get('string')
    print("'%s'" % (stt))
    context = {
        'form6': db.fulltext_find_str(str(stt))
    }
    return render(request, 'admin.html', context)

def xml_dump(request):
    print("555")
    db.load_dump()
    return HttpResponseRedirect(reverse('insert_admin'))