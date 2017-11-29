from django import forms
from lab2_App.database import Database
db = Database()

class Form_game(forms.Form):
    my_choice_field = forms.ChoiceField(choices=db.select_games)

class Form_stadium(forms.Form):
    my_choice_field = forms.ChoiceField(choices=db.select_stadium)

class Form_customer(forms.Form):
    my_choice_field = forms.ChoiceField(choices=db.select_vip_customers)
