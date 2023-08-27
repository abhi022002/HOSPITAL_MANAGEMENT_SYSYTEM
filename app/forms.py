# from django import forms
# from .models import physician

# class PatientForm(forms.Form):
#     ssn = forms.IntegerField()
#     name = forms.CharField(max_length=100)
#     age = forms.IntegerField()
#     gender = forms.CharField(max_length=10)
#     pcp = forms.ModelChoiceField(queryset=physician.objects.all())
    # pcp = forms.ModelChoiceField(queryset=Physician.objects.all())


from django import forms
from .models import patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = patient
        fields = ('ssn', 'name', 'gender', 'age', 'pcp')



 