# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import contacts
from django.shortcuts import render
import time
from django.shortcuts import redirect

def index(request):
	n = len(contacts.objects.all())
	all_contacts = contacts.objects.all()
	context = {'n':n,'all_contacts':all_contacts}
	return render(request,'phonebook/index.html',context)


def addcontact(request):
	if request.method == 'POST':						  #receiving data using POST method
		email = request.POST['email']  #receiving phone_number,email and plant name
		name = request.POST['name']
		phone_number = request.POST['phone_number']
		phone_number = int(phone_number)			
		contact_obj = contacts()					#creating new plant object and assigning the received values
		#conatct_obj.plant_id = p_max	
		contact_obj.name = name			
		contact_obj.phone_number = phone_number
		contact_obj.email = email
		contact_obj.added_at = time.asctime( time.localtime(time.time()))
		contact_obj.save()
		return redirect('/index')			#redirecting to home page after saving the plant
	return render(request, 'phonebook/addcontact.html')

'''def addcontact(request):
	
	context = {}
	return render(request,'phonebook/dummy.html',context)'''