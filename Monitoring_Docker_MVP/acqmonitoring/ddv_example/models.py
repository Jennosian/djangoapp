from django.db import models


class AgregateData(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    year = models.CharField(db_column='year', max_length=4, blank=True, null=True)
    month = models.CharField(db_column='month', max_length=4, blank=True, null=True)
    random_id_code = models.CharField(db_column='random_id_code', max_length=50, blank=True, null=True)
    type = models.CharField(db_column='type', max_length=4, blank=True, null=True)
    random_name = models.CharField(db_column='random_name', max_length=100, blank=True, null=True)
    random_amount = models.DecimalField(db_column='random_amount', max_digits=18, decimal_places=2, blank=True, null=True)
    random_count = models.DecimalField(db_column='random_count', max_digits=18, decimal_places=2, blank=True, null=True)
    random_percent = models.DecimalField(db_column='random_percent', max_digits=2, decimal_places=2, blank=True, null=True)
    rule_1 = models.DecimalField(db_column='rule_1', max_digits=18, decimal_places=2, blank=True, null=True)
    rule_2 = models.DecimalField(db_column='rule_2', max_digits=18, decimal_places=2, blank=True, null=True)
    rule_3 = models.DecimalField(db_column='rule_3', max_digits=18, decimal_places=2, blank=True, null=True)
    rule_4 = models.DecimalField(db_column='rule_4', max_digits=18, decimal_places=2, blank=True, null=True)
    created_dtime = models.DateTimeField(db_column='created_dtime', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Agregate_Data'


class DetailData(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    random_name = models.CharField(db_column='random_name', max_length=25, blank=True, null=True)
    random_amount = models.DecimalField(db_column='random_amount', max_digits=18, decimal_places=2, blank=True, null=True)
    date = models.DateField(db_column='date', blank=True, null=True)
    type = models.CharField(db_column='type', max_length=10, blank=True, null=True)
    random_id_code = models.CharField(db_column='random_id_code', max_length=50, blank=True, null=True)
    created_dtime = models.DateTimeField(db_column='created_dtime', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Detail_Data'

