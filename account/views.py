from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from helpers.main import decode_bytes_to_dict
import requests
import json
import base64

base_url = "http://127.0.0.1:8000/accounts/users/"


@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8").replace("'", '"'))
        res = requests.post(base_url, data=data)
        return Response(data=res.content, status=res.status_code, template_name='index.html')
    elif request.method=='GET':
        return render(request, 'index.html')


@api_view(['GET'])
def login_user(request):
    if request.method == 'GET':
        data = decode_bytes_to_dict(request.body)
        credentials = "{}:{}".format(data.get('email'), data.get('password'))
        encoded_bytes = base64.b64encode(credentials.encode("utf-8"))
        encoded_credentials = str(encoded_bytes, "utf-8")
        headers = {"Authorization": "Basic %s" % encoded_credentials}
        res = requests.get(base_url + "me/", data=data, headers=headers)
        print(res.content)
        return Response(data=decode_bytes_to_dict(res.content), status=res.status_code,
                        template_name='index.html')


# def

