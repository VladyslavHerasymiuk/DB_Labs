import sys

from django.utils.timezone import now

from lab2_App import models
from django.db import IntegrityError

class DatabaseORM:

    def add_customer(self, name, surname , phone_number , VIP):
        #obj, created = models.Customer.objects.get_or_create(name='{}'.format(name), surname='{}'.format(surname), phone_number='{}'.format(phone_number), vip='{}'.format(VIP))
        try:
                obj = models.Customer.objects.get(name='{}'.format(name), surname='{}'.format(surname))
        except models.Customer.DoesNotExist:
            obj = models.Customer(name='{}'.format(name), surname='{}'.format(surname), phone_number='{}'.format(phone_number), vip='{}'.format(VIP))
            obj.save()

    def select_games(self):
        rows = models.Games.objects.raw('SELECT * FROM games')
        return rows


    def select_stadium(self):
        rows = models.Stadiums.objects.raw('SELECT * FROM stadiums')
        return rows

    def select_vip_customers(self):
        rows = models.Customer.objects.raw("SELECT * FROM customer where VIP = 'true'")
        return rows

    def add_game(self, teams, stadium_id, datatime, price):
        obj = models.Games(team1_team2='{}'.format(teams), stadium_id='{}'.format(stadium_id),
                           game_data_time='{}'.format(datatime), ticket_price='{}'.format(price))
        obj.save()

    def add_fact(self, name, surname, game_id):
            cust_id =  models.Customer.objects.raw('SELECT cust_id FROM customer WHERE name=%s and surname =%s', [name,surname])[0]
            obj = models.Facts(cust_id='{}'.format(cust_id), game_id='{}'.format(game_id),sell_data_time=now())
            obj.save()

    def edit_game(self, game_id, stadium_id, datatime, price):
        models.Games.objects.filter(game_id='{}'.format(game_id)).update(stadium_id='{}'.format(stadium_id), game_data_time='{}'.format(datatime), ticket_price='{}'.format(price))

    def del_game(self, g_id):
        models.Games.objects.filter(game_id='{}'.format(g_id)).delete()






