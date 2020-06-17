from django import forms


class CreateNewList(forms.Form):
    name = forms.CharField(label="Country", max_length=200)
    #Date = forms.DateField(label="Date", input_formats=True)
    city = forms.CharField(label="City", max_length=200)
    population = forms.IntegerField()


