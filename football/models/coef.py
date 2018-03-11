from django.db.models import Model, TextField, ForeignKey, CASCADE


class Coef(Model):
    match = ForeignKey('AllAttr', on_delete=CASCADE, related_name='Coef_m')
    bookmaker = ForeignKey('Bookmaker', on_delete=CASCADE, related_name='Coef_b')
    one = TextField(null=True)
    x = TextField(null=True)
    two = TextField(null=True)