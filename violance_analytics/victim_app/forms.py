from django import forms
from .models import VictimApplication
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


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
            Submit('submit','Submit', css_class='btn-success')

        )




class VictimeApplicationForm(forms.ModelForm):

    class Meta:
        model = VictimApplication
        fields = ('name', 'incident_type', 'incident_date','place',
                  'gender', 'relation_with_criminal', 'witness', 'witness_name',
                  'informed_authority', 'authority_name', 'description',
                  'current_status_of_victim')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.layout = Layout('name', 'incident_type', 'incident_date','place',
                  'gender', 'relation_with_criminal', 'witness', 'witness_name',
                  'informed_authority', 'authority_name', 'description',
                  'current_status_of_victim',
            Submit('submit','Submit', css_class='btn-success')

        )
