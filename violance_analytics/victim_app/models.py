from django.db import models

# Create your models here.


class VictimApplication(models.Model):
    RAPE = 'rape'
    PHYSICAL_TORTURE = 'physical_torture'
    MENTAL_TORTURE = 'metal_torture'

    MALE = 'male'
    FEMALE = 'female'
    UNSPECIFIED = 'unspecified'

    FRIEND = 'friend'
    UNKNOWN = 'unknown'
    RELATIVE = 'relative'
    INLAWS = 'in-laws'

    POLICE = 'police'
    UNO = 'UNO'
    CHAIRMAN = 'chairman'
    MEMBER = 'member'

    AUTHORITY = [
        (POLICE, 'Police'),
        (UNO, 'UNO'),
        (CHAIRMAN, 'Chairman'),
        (MEMBER, 'Member')

    ]

    RELATION = [
        (FRIEND, 'Friend(s)'),
        (UNKNOWN, 'Unknown'),
        (RELATIVE, 'Relative(s)'),
        (INLAWS, 'In laws')

    ]

    INCIDENTS = [
        (RAPE, 'Rape'),
        (PHYSICAL_TORTURE, 'Attacking Physically'),
        (MENTAL_TORTURE, 'Mental Torture')
    ]
    GENDER = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (UNSPECIFIED, 'Unspecified')
    ]

    name = models.CharField(max_length=50, default='No name')
    incident_type = models.CharField(max_length=20, choices=INCIDENTS, default=MENTAL_TORTURE)
    incident_date = models.DateField()
    place = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50)
    address_3 = models.CharField(max_length=50)
    address_4 = models.CharField(max_length=50)
    address_5 = models.CharField(max_length=20, default='Bangladesh')
    gender = models.CharField(max_length=15, choices=GENDER, default=FEMALE)
    relation_with_criminal = models.CharField(max_length=20,choices=RELATION, default=UNKNOWN)
    witness = models.BooleanField(default=False)
    witness_name = models.CharField(max_length=20, default='No name')
    informed_authority = models.BooleanField(default=False)
    authority_name = models.CharField(max_length=20, choices=AUTHORITY, default='None')
    description = models.CharField(max_length=300, default='')
    current_status_of_victim = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.incident_type







