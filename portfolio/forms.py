from django import forms
from .models import Portfolio

class PortfolioForm(forms.ModelForm):


    class Meta:
        model = Portfolio
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PortfolioForm, self).__init__(*args, **kwargs)

        port_fields = ['title', 'description', 'technologies', 'web_address', 'web_address', 'image']

        for port in port_fields:
            self.fields[port].widget.attrs.update({'class': 'my-3'})

    # from_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    # to_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))