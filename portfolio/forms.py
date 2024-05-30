from django import forms
from .models import Portfolio, Collaborative

class PortfolioForm(forms.ModelForm):


    class Meta:
        model = Portfolio
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PortfolioForm, self).__init__(*args, **kwargs)

        port_fields = ['title', 'description', 'technologies', 'web_address', 'github', 'image', 'image_description']

        for port in port_fields:
            self.fields[port].widget.attrs.update({'class': 'my-3'})


class CollaborativeForm(forms.ModelForm):


    class Meta:
        model = Collaborative
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CollaborativeForm, self).__init__(*args, **kwargs)

        collab_fields = ['title', 'description', 'technologies', 'web_address', 'github', 'image', 'image_description']

        for c in collab_fields:
            self.fields[port].widget.attrs.update({'class': 'my-3'})