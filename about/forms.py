from django import forms
from .models import About, Education, Work_experience, Interest



class AboutForm(forms.ModelForm):


    class Meta:
        model = About
        fields = '__all__'


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
    to_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), required=False)


class Work_experienceForm(forms.ModelForm):
    class Meta:
        model = Work_experience
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Work_experienceForm, self).__init__(*args, **kwargs)

        work_fields = [
            'from_date',
            'to_date',
            'job_title',
            'company',
            'location',
            'achievement1',                
            'achievement2',
            'achievement3',
            'achievement4',
            'achievement5'
        ]

        for work in work_fields:
            self.fields[work].widget.attrs.update({'class': 'my-3'})

    from_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    to_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), required=False)


class InterestForm(forms.ModelForm):

    class Meta:
        model = Interest
        fields = '__all__'