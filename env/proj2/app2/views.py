from django.shortcuts import render
#from app2.models import User
from app2.forms import NewUserForm


# Create your views here.
def index(request):
	
	#strq = {'Help_Support':'i am str'}
	return render(request,'app2/index.html')

def user(request):

	form = NewUserForm()

	if request.method == 'POST':
		form = NewUserForm(request.POST)

		if form.is_valid():
			form.save(commit = True)
			return index(request)
		else :
			print('Error invalid')

	return render(request,'app2/users.html',{'form':form})

	# user_list = User.objects.order_by('first_name')
	# user_dict = {'record_list':user_list}
	# return render(request,'app2/users.html',context = user_dict)
