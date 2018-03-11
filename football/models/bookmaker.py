from django.db.models import Model, TextField


class Bookmaker(Model):
    name = TextField(null=True)
    href = TextField(null=True)
    way = TextField(null=True)
    #Coef
