from django.db.models import Model, TextField, IntegerField


class AllAttr(Model):
    time = TextField(null=False)
    status = TextField(null=False)
    team_1 = TextField(null=False)
    team_2 = TextField(null=False)
    #Coef

    def __str__(self):
        return '<time={} status={} team_1={} team_2={}'.format(self.time, self.status, self.team_1, self.team_2)