from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse
from .forms import JASERForm
from .models import JASER

def index(request):
    return render(request, 'home/index.html')

def pdf_list(request):
    pdfs = JASER.objects.all().order_by('-uploaded_at')
    return render(request, 'home/pdf_list.html', {'pdfs': pdfs})

@login_required
def upload_jaser(request):
    if request.method == 'POST':
        form = JASERForm(request.POST, request.FILES)
        if form.is_valid():
            jaser = form.save(commit=False)
            jaser.user = request.user  # Set the user to the current logged-in user
            jaser.save()
            messages.success(request, 'PDF uploaded successfully!')
            return redirect('index')  # Redirect to the homepage or any other page
    else:
        form = JASERForm()

    return render(request, 'home/upload_pdf.html', {'form': form})

@login_required
def edit_jaser(request, jaser_id):
    jaser = get_object_or_404(JASER, id=jaser_id)

    if request.method == 'POST':
        form = JASERForm(request.POST, request.FILES, instance=jaser)
        if form.is_valid():
            form.save()
            messages.success(request, 'PDF updated successfully!')
            return redirect('jaser_list')  # Redirect to the list of JASER uploads
    else:
        form = JASERForm(instance=jaser)

    return render(request, 'home/edit_pdf.html', {'form': form, 'jaser': jaser})

@login_required
def delete_jaser(request, jaser_id):
    jaser = get_object_or_404(JASER, id=jaser_id)

    if request.method == 'POST':
        jaser.delete()
        messages.success(request, 'PDF deleted successfully!')
        return redirect('jaser_list')  # Redirect to the list of JASER uploads

    return render(request, 'home/delete_pdf.html', {'jaser': jaser})

@login_required
def jaser_list(request):
    jasers = JASER.objects.filter(user=request.user)  # Display only the user's uploads
    return render(request, 'home/jaser_list.html', {'jasers': jasers})