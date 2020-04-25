from .models import ProjectApplication
from .serializer import ProjectApplicationSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from .documents import ProjectApplicationDocument
from django.core import serializers as serial
import json
# Create your views here.



@api_view(http_method_names=['GET','POST'])
def project_application_list(request, format=None):
    if request.method == 'GET':

        project = ProjectApplication.objects.all()
        serializer = ProjectApplicationSerializer(project, many=True)

        q = request.query_params.get("search")

        result_data = serializer.data

        if q :
           s = ProjectApplicationDocument.search().query('match', project_name=q)

           result_data = []
           for l in s:
               parse = {
                        'project_name': l.project_name,
                        'path_file': l.path_file,
                        'status_log': l.status_log
                        }
               result_data.append(parse)



        data = {"data": result_data}

        return JsonResponse(data, safe=False, status=200)


    if request.method == 'POST':

        if not bool(request.data):
            data = {
                'message': 'internal error',
            }
            return JsonResponse(data, safe=False, status=404)

        serializer = ProjectApplicationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):

            serializer.save()

            return JsonResponse(serializer.data, status=200)

        return JsonResponse(serializer.errors, status=400)

