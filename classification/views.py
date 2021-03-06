from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .NBCreateCorpus import NBCreateCorpus
from .NBCategoryPredictor import NBCategoryPredictor

# Create your views here.

def index(request):
	#template = loader.get_template('classification/index.html')
	q_list = ["how are you", "how is classifier"]
	#q_list = []
	context = { 'latest_question_list': q_list}
	#return HttpResponse("Hello, world. You're at the classification home !!!")
	return HttpResponse(template.render(context, request))
	
def upload_file(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			print("Saurabh")
			fileName = request.FILES['file']
			name,extn = fileName.name.split(".")
			#return HttpResponseRedirect('/success/url')
			print("Got " + extn + " file")
			if (extn == "xls" or extn == "xlsx"):
				nbcc = NBCreateCorpus(fileName, "Nov 2017")
				corpusPath = nbcc.create_corpus()
				nbcp = NBCategoryPredictor(corpusPath)
				nbcp.create_model()
				return HttpResponse('Got your file !!')
			else:
				form = UploadFileForm()
	else:
		form = UploadFileForm()
	return render(request, 'classification/index.html', {'form': form})

