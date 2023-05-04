from django.shortcuts import render
from .forms import ReportForm
from django.contrib import messages
import logging


def ContactsPage(request):
    form = ReportForm()
    context = {'form': form}
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                form.save()
                messages.success(request, 'Sent successfully')
            else:
                messages.warning(request, 'You should login before send it.')
    else:
        form = ReportForm()
    return render(request, 'Contacts/contacts.html', context)
