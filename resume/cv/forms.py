from django.forms import ModelForm

from cv.models import Detal

class DetalForm(ModelForm):
    class Meta:
        model = Detal
        fields = ['name' , 'mobile' , 'email', 'school', 'degree','skill','project','previous_work','certification','about']
