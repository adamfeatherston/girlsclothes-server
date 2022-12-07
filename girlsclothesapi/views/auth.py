from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from girlsclothesapi.models import Kid


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    '''Handles the authentication of a user

    Method arguments:
    request -- The full HTTP request object
    '''
    username = request.data['username']
    password = request.data['password']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    authenticated_user = authenticate(username=username, password=password)

    # If authentication was successful, respond with their token
    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)

        data = {
            'valid': True,
            'token': token.key,
            'staff': authenticated_user.is_staff
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
    request -- The full HTTP request object
    '''
    account_type = request.data.get('account_type', None)
    username = request.data.get('username', None)
    email = request.data.get('email', None)
    first_name = request.data.get('first_name', None)
    last_name = request.data.get('last_name', None)
    password = request.data.get('password', None)

    if account_type is not None \
        and username is not None\
        and email is not None\
        and first_name is not None \
        and last_name is not None \
        and password is not None:

        try:
            # Create a new user by invoking the `create_user` helper method
            # on Django's built-in User model
            new_user = User.objects.create_user(
                username=request.data['username'],
                email=request.data['email'],
                first_name=request.data['firstName'],
                last_name=request.data['lastName'],
                password=request.data['password']
            )
        except IntegrityError:
            return Response(
                {'message': 'An account with that username already exists'},
                status=status.HTTP_400_BAD_REQUEST
            )

        account = None

        if account_type == 'kid':
            account = Kid.objects.create(
                age=request.data['age'],
                dress_size=request.data['dressSize'],
                shoe_size=request.data['shoeSize'],
                shirt_size=request.data['shirtSize'],
                underwear_or_diaper_size=request.data['underwearOrDiaperSize'],
                sock_size=request.data['sockSize'],
                user=new_user
            )
            token = Token.objects.create(user=account.user)
        elif account_type == 'parent':
            new_user.is_staff = True
            new_user.save()
            token = Token.objects.create(user=new_user)


        data = { 'token': token.key, 'staff': new_user.is_staff }
        return Response(data)

    return Response({'message': 'You must provide username, email, password, first_name, last_name and account_type'}, status=status.HTTP_400_BAD_REQUEST)