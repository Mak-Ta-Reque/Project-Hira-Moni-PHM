from django.db import models

# Create your models here.


class Divisions(models.Model):
    division_id = models.IntegerField(default=0)
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
    district_id = models.IntegerField(default=0)
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
    upzila_id = models.IntegerField(default=0)
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
    union_id = models.IntegerField(default=0)
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

