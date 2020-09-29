from django.forms import ModelForm
from .models import create_happ_user, hike_preferences


class create_new_happ_user(ModelForm):
    class Meta:
        model = create_happ_user
        fields = '__all__'


class survey(ModelForm):
    class Meta:
        model = hike_preferences
        fields = '__all__'
