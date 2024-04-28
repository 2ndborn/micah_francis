from django import forms
from .models import Education, Interest


class EducationForm(forms.ModelForm):


    class Meta:
        model = Education
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EducationForm, self).__init__(*args, **kwargs)

        ed_fields = ['from_date', 'to_date', 'institution', 'qualification', 'location']

        for ed in ed_fields:
            self.fields[ed].widget.attrs.update({'class': 'my-3'})

    from_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    to_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))


class InterestForm(forms.ModelForm):


    class Meta:
        model = Interest
        fields = '__all__'