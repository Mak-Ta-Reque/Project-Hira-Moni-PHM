from django.db import models

# Create your models here.


class Divisions(models.Model):
    name = models.CharField(max_length=250)
    bn_name = models.CharField(max_length=250)
    url = models.URLField(max_length=500, null=True, blank=True, default=None)

    is_active = models.NullBooleanField(default=True)
    is_delete = models.NullBooleanField(default=False)
    insert_user = models.CharField(max_length=30, null=True, blank=True)
    insert_date = models.DateTimeField(auto_now=True)
    update_user = models.CharField(max_length=30, null=True, blank=True, default=None)
    update_date = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name


class Districts(models.Model):
    division = models.ForeignKey(Divisions, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    bn_name = models.CharField(max_length=250)
    latitude = models.DecimalField(max_digits=14, decimal_places=10, null=True, blank=True)
    longitude = models.DecimalField(max_digits=14, decimal_places=10, null=True, blank=True)
    url = models.URLField(max_length=500, null=True, blank=True, default=None)

    is_active = models.NullBooleanField(default=True)
    is_delete = models.NullBooleanField(default=False)
    insert_user = models.CharField(max_length=30, null=True, blank=True)
    insert_date = models.DateTimeField(auto_now=True)
    update_user = models.CharField(max_length=30, null=True, blank=True, default=None)
    update_date = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name


class Upzilas(models.Model):
    district = models.ForeignKey(Districts, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    bn_name = models.CharField(max_length=250)
    latitude = models.DecimalField(max_digits=14, decimal_places=10, null=True, blank=True)
    longitude = models.DecimalField(max_digits=14, decimal_places=10, null=True, blank=True)
    url = models.URLField(max_length=500, null=True, blank=True, default=None)

    is_active = models.NullBooleanField(default=True)
    is_delete = models.NullBooleanField(default=False)
    insert_user = models.CharField(max_length=30, null=True, blank=True)
    insert_date = models.DateTimeField(auto_now=True)
    update_user = models.CharField(max_length=30, null=True, blank=True, default=None)
    update_date = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name


class Unions(models.Model):
    upzila = models.ForeignKey(Upzilas, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    bn_name = models.CharField(max_length=250)
    latitude = models.DecimalField(max_digits=14, decimal_places=10, null=True, blank=True)
    longitude = models.DecimalField(max_digits=14, decimal_places=10, null=True, blank=True)
    url = models.URLField(max_length=500, null=True, blank=True, default=None)

    is_active = models.NullBooleanField(default=True)
    is_delete = models.NullBooleanField(default=False)
    insert_user = models.CharField(max_length=30, null=True, blank=True)
    insert_date = models.DateTimeField(auto_now=True)
    update_user = models.CharField(max_length=30, null=True, blank=True, default=None)
    update_date = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name


def populate_database():
    import pandas as pd
    from ..violance_analytics import settings
    file_name = settings.BASE_DIR
    print(file_name)
    dfs = pd.read_excel(file_name, sheetname=None)
