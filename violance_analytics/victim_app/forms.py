from django import forms
from .models import VictimApplication
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row
from django.forms.widgets import DateInput


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label='E-mail')
    category = forms.ChoiceField(choices=[('question', 'Question'), ('other', 'Other')])
    subject = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'name',
            'email',
            'category',
            'subject',
            'body',
            Submit('submit', 'Submit', css_class='btn-success')

        )




class VictimeApplicationForm(forms.ModelForm):
    class Meta:
        model = VictimApplication
        fields = '__all__'
        widgets = {
            'incident_date': DateInput(attrs= {'type':'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['place'].label = "Village/Street"
        self.fields['address_1'].label = "Union/Post office"
        self.fields['address_2'].label = "Upazilla/P. S. "
        self.fields['address_3'].label = "District"
        self.fields['address_4'].label = "Division"
        self.fields['address_5'].label = "Country"
        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.layout = Layout('name', 'incident_type', 'incident_date',
                                    Row('place',
                                    'address_1', 'address_2',
                                    'address_3', 'address_4', 'address_5'),
                                    'gender', 'relation_with_criminal', 'witness', 'witness_name',
                                    'informed_authority', 'authority_name', 'description',
                                    'current_status_of_victim',
            Submit('submit','Submit', css_class='btn-success')

        )

