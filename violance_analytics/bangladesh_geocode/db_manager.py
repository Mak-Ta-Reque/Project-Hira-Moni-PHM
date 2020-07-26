from django.db import transaction

#@transaction.atomic
def populate_database():
    import pandas as pd
    import os
    from django.conf import settings
    from .models import Divisions, Districts, Upzilas, Unions
    file_name = os.path.join(settings.BASE_DIR, 'data/divisions.csv')
    division_file = pd.read_csv(file_name)
    division_file = division_file[['id', 'name']]
    for index, row in division_file.iterrows():
        div_id = row['id']
        div_name = row['name']
        div_count = Divisions.objects.filter(name=div_name).count()
        if div_count < 1:
            div = Divisions(division_id=div_id, name=div_name, bn_name ='n')
            div.save()
        div_obj = Divisions.objects.get(name=div_name)
    
    file_name = os.path.join(settings.BASE_DIR, 'data/districts.csv')
    district_file = pd.read_csv(file_name)
    district_file = district_file[['district_id', 'division_id', 'name']]
    for index, row in district_file.iterrows():
        div_id = row['division_id']
        dis_id = row['district_id']
        dis_name = row['name']
        div_obj = Divisions.objects.get(division_id=div_id)
        dis_count = Districts.objects.filter(name=dis_name).filter(division=div_obj).count()
        if dis_count < 1:
            dis_object = Districts(district_id=dis_id, division=div_obj, name=dis_name)
            dis_object.save()

    file_name = os.path.join(settings.BASE_DIR, 'data/upazilas.csv')
    upzila_file = pd.read_csv(file_name)
    upzila_file = upzila_file[['district_id', 'upzila_id', 'name']]
    for index, row in upzila_file.iterrows():
        upz_id = row['upzila_id']
        dis_id = row['district_id']
        upz_name = row['name']
        dis_obj = Districts.objects.get(district_id=dis_id)
        upz_count = Upzilas.objects.filter(name=upz_name).filter(district=dis_obj).count()
        if upz_count < 1:
            upz_object = Upzilas(upzila_id=upz_id, district=dis_obj, name=upz_name)
            upz_object.save()

    file_name = os.path.join(settings.BASE_DIR, 'data/unions.csv')
    union_file = pd.read_csv(file_name)
    union_file = union_file[['union_id', 'upzila_id', 'name']]
    for index, row in union_file.iterrows():
        uni_id = row['union_id']
        upz_id = row['upzila_id']
        uni_name = row['name']
        upz_object = Upzilas.objects.get(upzila_id=upz_id)
        uni_count = Unions.objects.filter(name=uni_name).filter(upzila=upz_object).count()
        if uni_count < 1:
            uni_object = Unions(union_id=uni_id, upzila=upz_object, name=uni_name)
            uni_object.save()
