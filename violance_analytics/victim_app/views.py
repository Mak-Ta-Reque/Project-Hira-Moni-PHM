from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm, VictimeApplicationForm
# Create your views here.


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']

            print(name, email, subject, body)

            # Now we can generate an email forwarding the email.

    form = ContactForm()
    return render(request, 'form.html', {'form': form})


def victim_application_view(request):

    if request.method == 'POST':
        form = VictimeApplicationForm(request.POST)

        if form.is_valid():
            print('Valid')
            form.save()

    form = VictimeApplicationForm()
    return render(request, 'form.html', {'form': form})



