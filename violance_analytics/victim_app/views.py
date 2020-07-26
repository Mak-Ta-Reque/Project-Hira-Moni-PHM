from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm, VictimeApplicationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


#@login_required(login_url='login')
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


@login_required(login_url='login')
def victim_application_view(request):
    form = VictimeApplicationForm()
    if request.method == 'POST':
        print('POST')
        form = VictimeApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'userinput_form.html', context)



