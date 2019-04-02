from django.shortcuts import render
from firstapp.models import Topic,Webpage,AccessRecord
# Create your views here.

from django.http import HttpResponse

def index(request):
	webpage_list = AccessRecord.objects.order_by('date')
	date_dict = {'access_records': webpage_list}


	my_dic = {'insert_me':'We are working on something new'}
	#return HttpResponse('Hello Anusha')
	return render(request,'firstapp/index.html' , context = date_dict)

def home(request):
	return HttpResponse('Hello Home')