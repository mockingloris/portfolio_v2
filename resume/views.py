from django.shortcuts import render,get_object_or_404
from .models import Skill,Project
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
import json

def index(request):
        projects = Project.objects.order_by('createdAt')
        context = {"projects":projects}
        return render(request,'resume/index.html', context)

def about(request):
    context = ''
    return render(request,'resume/about.html',context)

def contact_thanks(request):
    context = ''
    return render(request,'resume/contact_thanks.html',context)

def contact(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name', '')
        note = request.POST.get('note', '')
        from_email = request.POST.get('email', '')
        subject = 'Get in touch - portfolio website'
        if subject and note and from_email and full_name:
            try:
                note += "\n From: " + full_name + "\n Email: " + from_email
                print(note)
                send_mail(subject, note, from_email, ['hassanabidpk89@gmail.com'])
            except BadHeaderError:
                print("invalid header")
                return HttpResponse(json.dumps({'message':'Invalid header found.'}),content_type="application/json")
            return HttpResponse(json.dumps({'message':'Thanks for getting in touch! I will get back to you ASAP!'}),content_type="application/json")
        else:
            return HttpResponse(json.dumps({'message':"Fill in all the fields and try again!"}),content_type="application/json")
    else:
        context = {}
        return render(request,'resume/contact.html',context)
