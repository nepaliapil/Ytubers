from django.shortcuts import render, redirect
from .models import ContactTeam
from django.contrib import messages

    # full_name = models.CharField(max_length=100)
    # email = models.CharField(max_length=100)
    # phone = models.IntegerField()
    # company_name = models.CharField(max_length=100)
    # subject = models.CharField(max_length=100)
    # detail_message = models.TextField()
    # full_name = models.CharField(max_length=100)
    # user_id = models.IntegerField(blank=True)

# Create your views here.
def contactTeam(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']
        company_name = request.POST['company_name']
        subject = request.POST['subject']
        detail_message = request.POST['detail_message']
        user_id = request.POST['user_id']

        contactTeam = ContactTeam(full_name=full_name, email=email, phone=phone, company_name=company_name, subject=subject, detail_message=detail_message, user_id=user_id)
        contactTeam.save()
        messages.success(request, 'Thanks for reaching out we will respond as soon as possible!')
        return redirect('contact')