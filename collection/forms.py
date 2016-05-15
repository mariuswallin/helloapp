from django.forms import ModelForm
from collection.models import Aktiviteter

class AktivitetForm(ModelForm):
    class Meta:
        model = Aktiviteter
        fields = ('name','description',)
   
        