from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import json

base_url = "http://127.0.0.1:8000/accounts/users/"


@api_view(['POST'])
def create_user(request):
    if request.method=='POST':
        data = json.loads(request.body.decode("utf-8").replace("'", '"'))
        res = requests.post(base_url, data=data)
        return Response(data=res.content, status=res.status_code, template_name='index.html')
    elif request.method=='GET':
        return render(request, 'index.html')


# @api_view(['GET'])
# def login_user(request):
#     if request.method=='GET':
#         data = json.loads(request.body.decode("utf-8").replace("'", '"'))
#         headers = {
#             "Authorization": "Basic a2dAZ21haWwuY29tOkdvb2dsZTE5NzQ="
#         }
#         res = requests.get(base_url+"me/", data=data)
#         print(data)
#         return Response(data=res.content, status=res.status_code, template_name='index.html',
#                         headers=headers)

