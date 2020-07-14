from bangladesh_geocode.models import Divisions
from victim_app.models import VictimApplication

def fetch_division_names():
    names = Divisions.objects.all().values_list('name')
    name_list = []
    for x in names:
        name_list.append(x[0])
    
    return name_list

def fetch_division_crime_count(name_list):
    print ("helo")
    counts = []
    for x in name_list:
        div_object = Divisions.objects.get(name=x)
        counts.append(VictimApplication.objects.filter(address_4=div_object).count())

    return counts
