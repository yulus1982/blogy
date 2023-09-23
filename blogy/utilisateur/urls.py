from django.urls import path
from utilisateur.views import acceuil, user_register, user_logout, user_login, userProfile
urlpatterns = [
path('', acceuil, name="acceuil"),
path('register', user_register, name="register"),
path('login',user_login, name="login"),
path('logout',user_logout, name="logout"),
path('userprofile',userProfile, name="userprofile"),


]