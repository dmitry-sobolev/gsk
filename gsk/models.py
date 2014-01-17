from django.db import models


class Garage(models.Model):
    number = models.PositiveIntegerField(verbose_name=u'', max_length=5)

    first_name = models.CharField(verbose_name=u'', max_length=50)
    second_name = models.CharField(verbose_name=u'', max_length=50)
    last_name = models.CharField(verbose_name=u'', max_length=50)
    address = models.CharField(verbose_name=u'', max_length=50)
    phone = models.CharField(verbose_name=u'', max_length=50)
    passport_data = models.TextField(verbose_name=u'')

    length = models.FloatField(verbose_name=u'')
    width = models.FloatField(verbose_name=u'')

    electric_meter_number = models.CharField(verbose_name=u'', max_length=50)


class Pass(models.Model):
    application = models.CharField(verbose_name=u'', max_length=50)
    pass_holder_last_name = models.CharField(verbose_name=u'', max_length=50)
    cars_number = models.CharField(verbose_name=u'', max_length=50)
    date_until = models.DateField(verbose_name=u'')

    garage = models.ForeignKey(Garage)


class ElectricMeterReading(models.Model):
    reading_date = models.DateField(verbose_name=u'')
    value = models.IntegerField(verbose_name=u'')

    garage = models.ForeignKey(Garage)


class Payment(models.Model):
    year = models.CharField(verbose_name=u'', max_length=50)
    check_number = models.CharField(verbose_name=u'', max_length=50)
    amount = models.FloatField(verbose_name=u'')
    payment_date = models.DateField(verbose_name=u'')
    tariff = models.FloatField(verbose_name=u'')

    garage = models.ForeignKey(Garage)
