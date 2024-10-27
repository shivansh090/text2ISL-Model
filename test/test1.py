from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

user = User.objects.get(username='yourUsername')  # Replace with actual username
token = Token.objects.get(user=user)
print(token.key)  # This should be the token you use in Postman
