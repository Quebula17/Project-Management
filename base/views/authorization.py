from django.shortcuts import redirect
import requests
from django.http import HttpResponse
from dotenv import load_dotenv
import os
from django.contrib.auth import get_user_model
from base.models.black_listed_users import BlacklistedUser

User = get_user_model()

load_dotenv()


def user_exists(username):
    return User.objects.filter(username=username).exists()


def is_user_blacklisted(username):
    return BlacklistedUser.objects.filter(user__username=username).exists()

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

    print("get_user_data called")
    access_token = request.GET.get('access_token')
    url = 'https://channeli.in/open_auth/get_user_data/'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    print(response.content)
    
    if response.status_code == 200:

        omniport_data = response.json()


        role=omniport_data['person']['roles'][1]['role']
        username=omniport_data['username']
        email=omniport_data['contactInformation']['instituteWebmailAddress']
        full_name=omniport_data['person']['fullName']
        current_year=omniport_data['student']['currentYear']
        full_name=full_name.split() 

        print(full_name)

        if is_user_blacklisted(username):
            return HttpResponse('<html><body style="display: flex; justify-content: center; align-items: center; height: 100vh;"><h1 style="text-align: center; font-weight: bold;">You are blacklisted</h1></body></html>', status=403)


        if not user_exists(username) and role == 'Maintainer':

            if current_year == 4:
                user = User.objects.create(
                    username=username,
                    email=email,
                    first_name=full_name[0],
                    last_name=full_name[1],
                    current_year=current_year,
                    is_admin=True,
                )
                user.save()

            else:
                user = User.objects.create(
                    username=username,
                    email=email,
                    first_name=full_name[0],
                    last_name=full_name[1],
                    current_year=current_year,
                    is_admin=False,
                )
                user.save()

            url = f'http://localhost:8000/api/token/'
            data = {
                'username': user.username,
                'password': 'password',
            }
            response = requests.post(url, data=data)
            response = response.json()
            
            access = response['access']
            refresh = response['refresh']
            return redirect(f'http://localhost:3000/authenticating?access={access}&refresh={refresh}')
        
        elif user_exists(username):

            user = User.objects.get(username=username)

            url = f'http://localhost:8000/api/token/'
            data = {
                'username': user.username,
                'password': 'password',
            }
            response = requests.post(url, data=data)
            response = response.json()
            access = response['access']
            refresh = response['refresh']
            return redirect(f'http://localhost:3000/authenticating?access={access}&refresh={refresh}')
        
        else:
            return HttpResponse("You are not a maintainer")
        
    else:
        return HttpResponse("Some unexpected error occured")
    
    

        






