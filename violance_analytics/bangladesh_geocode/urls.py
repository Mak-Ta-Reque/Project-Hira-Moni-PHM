from django.conf.urls import url
from . import views

urlpatterns = [
    
]

def populate_database():
    # Zinuk
    import pandas as pd
    import os
    from django.conf import settings
    from .models import Divisions
    file_name = os.path.join(settings.BASE_DIR, 'data/bgd_adminboundaries_tabulardata.xlsx')
    print(file_name)
    dfs = pd.read_excel(file_name)

    dfs = dfs[['admin4Name_en', 'admin3Name_en',
                'admin2Name_en',
                'admin1Name_en']]
    for index, row in dfs.iterrows():
        division = row['admin1Name_en']
        district = row['admin2Name_en']
        upazilla = row['admin3Name_en']
        union = row['admin4Name_en']
        div = Divisions(name = division, bn_name ='n')
        div.save()



    print(dfs.head())


#populate_database()
