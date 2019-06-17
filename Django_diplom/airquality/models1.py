from django.db import models


class Astanadata(models.Model):
    number = models.IntegerField('№')
    time = models.DateTimeField('Дата и время')
    aqi = models.IntegerField('Уровень pm2.5')

    def __unicode__(self):
        return '/%/' % self.number

    def get_absolute_url(self):
        return 'viewdata/%s/' % self.aqi





