from django import forms
from .models import FlightRoute

class FlightRouteForm(forms.ModelForm):
    class Meta:
        model = FlightRoute
        fields = ['source', 'destination', 'direction', 'distance_km', 'duration_mins']
        
    def clean(self):
        cleaned_data = super().clean()
        source = cleaned_data.get('source')
        destination = cleaned_data.get('destination')
        
        if source == destination:
            raise forms.ValidationError("Source and Destination cannot be the same.")
        return cleaned_data