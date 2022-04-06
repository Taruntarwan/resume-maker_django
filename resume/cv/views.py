from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Detal
from django.template import loader
from django.contrib import messages
import pdfkit
import io
from cv.forms import DetalForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
	if request.user.is_authenticated:
		user = request.user
		form = DetalForm(request.POST)
		if form.is_valid():
			data = form.save(commit=False)
			data.user = user
			data.save()
			return redirect('list')
		else:
			return render(request,"cv/index.html",{'form':form})



def download(request,id):
	data = Detal.objects.get(pk=id)
	template = loader.get_template("cv/display.html")
	html = template.render({'data':data})
	option = {
	'page-size':'Letter',
	'encoding':'UTF-8'
	}
	pdf = pdfkit.from_string(html,False,option)
	response = HttpResponse(pdf,content_type='application/cv')
	response['Content-Disposition'] = 'attachment'

	return response

def display(request,id):
	data = Detal.objects.get(pk=id)
	return render(request,'cv/display.html',{'data':data})

def edit(request,id):
	data =Detal.objects.get(pk=id)
	form= DetalForm(instance= data)
	if request.method=='POST':
		form= DetalForm(request.POST,instance=data)
		if form.is_valid():
			form.save()
			return redirect('list')
	return render(request,'cv/edit.html', {'form': form})
	

def list(request):
	if request.user.is_authenticated:
		user = request.user
		form = DetalForm()
		data = Detal.objects.filter(user=user)
		return render(request,"cv/list.html",{'form':form,'data' : data})
	else:
		return HttpResponseRedirect('/login/')

def delete(request,id):
	data = Detal.objects.get(pk=id)
	data.delete()
	messages.success(request,'resume delete successfully.')
	return redirect('list')

def home(request):
	return redirect('list')


# if request.method == 'POST':
		# 	name = request.POST.get("name","")
		# 	mobile = request.POST.get("mobile","")
		# 	email = request.POST.get("email","")
		# 	school = request.POST.get("sname","")
		# 	degree = request.POST.get("degree","")
		# 	skill = request.POST.get("skill","")
		# 	project = request.POST.get("project","")
		# 	previous_work = request.POST.get("previous","")
		# 	certification = request.POST.get("certification","")
		# 	about = request.POST.get("about","")

			# detail = Detal(name= name,mobile = mobile,email=email,school=school,degree=degree,
			# 	skill=skill,project=project,previous_work=previous_work,certification=certification,about=about)
			# detail.user = user
			# detail.save()



