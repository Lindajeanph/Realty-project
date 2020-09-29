from django.db import models


class create_happ_user(models.Model):
    admin = models.Manager()

    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    nick_name = models.CharField(primary_key=True, max_length=30, blank=False)
    street_address = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=False)
    country = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=30, blank=False)
    password = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.nick_name


hike_type = [
    ('F', 'Flat'),
    ('H', 'Hilly'),
    ('M', 'Mountains'),
    ('R', 'Rivers'),
    ('G', 'Glacier'),
    ('L', 'Lake')
]

hike_length = [
    ('1-2', '1-2 Miles'),
    ('2-5,', '2-5 Miles'),
    ('5-8', '5-8 Miles'),
    ('8-10', '8-10 Miles'),
    ('10+', '10+ Miles')
]

healthy = [
    ('PH', 'Not to Healthy'),
    ('SH', 'Somewhat Healthy'),
    ('H', 'Healthy'),
    ('PH', 'Pretty Healthy'),
    ('VH', 'Very Healthy')
]

avid = [
    (True, 'Yes'),
    (False, 'No')
]


class hike_preferences(models.Model):
    admin = models.Manager()

    nick_name = models.ForeignKey(create_happ_user, on_delete=models.CASCADE)
    favorite_types_of_hikes = models.CharField(max_length=30, choices=hike_type, blank=False)
    perfect_length_of_hike = models.CharField(max_length=30, choices=hike_length, blank=False)
    avid_hiker = models.BooleanField(choices=avid, default=False)
    how_healthy_are_you = models.CharField(max_length=30, choices=healthy, blank=False)

    def __str__(self):
        return self.nick_name