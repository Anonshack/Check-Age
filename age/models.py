import datetime
from django.db import models


class TugilganYil(models.Model):
    tugilgan_yil = models.IntegerField()

    def yosh_hisoblash(self):
        a = datetime.date.today()
        yosh = a.year - self.tugilgan_yil
        kun = int((a - datetime.date(self.tugilgan_yil, 1, 1)).days)
        vaqt = kun * 24
        return yosh, kun, vaqt

    def __str__(self):
        return str(self.tugilgan_yil)
