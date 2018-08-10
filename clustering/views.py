from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.conf import settings
from .forms import UploadFileForm
from .KMeansClustering import KMeansClustering
from sklearn.externals import joblib
import os
import shutil

# Create your views here.
def index(request):
	print("upload page")
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			print("Form valid")
			fileName = request.FILES['file']
			name,extn = fileName.name.split(".")
			print("Got " + extn + " file")
			if (extn == "xls" or extn == "xlsx"):
				kmc = KMeansClustering(fileName)
				clusters = kmc.create_model()
				
				##Save results object
				os.chdir(settings.SITE_ROOT)
				print(settings.SITE_ROOT)
				path = '../clustering/KM_temp'
				os.chdir(path)
				print(path + '/' + fileName.name)
				print(os.path.exists(path + '/' + fileName.name))
				if not os.path.isdir(fileName.name):
					os.mkdir(fileName.name)
				path = './' + fileName.name
				os.chdir(path)
				joblib.dump(clusters,  name + '_results.pkl')
				os.chdir(settings.SITE_ROOT)
				
				context = {'clusters':clusters}
				return render(request, 'clustering/result.html', context)
			else:
				form = UploadFileForm()
	else:
		form = UploadFileForm()
	return render(request, 'clustering/index.html', {'form': form})

def cluster_data(request, fileName, clsIndx):
	print("index : " + clsIndx)
	print("result page" + fileName + str(clsIndx))
	return HttpResponse(fileName + str(clsIndx) + " test !!!")
