from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse
from dotenv import load_dotenv
import os

load_dotenv()


def oauth_authorize(request):
    CLIENT_ID = os.environ.get('OMNIPORT_CLIENT_ID')
    REDIRECT_URI = 'http://localhost:8000/api/oauth/callback/'

    
    url = f'https://channeli.in/oauth/authorise?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}'
    return redirect(url)


def get_access_token(request):
    CLIENT_ID = os.environ.get('OMNIPORT_CLIENT_ID')
    CLIENT_SECRET = os.environ.get('OMNIPORT_CLIENT_SECRET')
    redirect_uri = 'http://localhost:8000/api/oauth/callback/'
    code = request.GET.get('code')

    url = 'https://channeli.in/open_auth/token/'
    data = {
        'grant_type': 'authorization_code',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': redirect_uri,
        'code': code,
    }

    response = requests.post(url, data=data)
    token_data = response.json()
    access_token = token_data.get('access_token')

    return redirect(f'/api/get_user_data/?access_token={access_token}')

def get_user_data(request):
    access_token = request.GET.get('access_token')
    url = 'https://channeli.in/open_auth/get_user_data/'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    print(response.content)
    return HttpResponse(response.content)