from django.shortcuts import render

from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def create(request):

    return render(request, 'billing_profiles/create.html', {

    })