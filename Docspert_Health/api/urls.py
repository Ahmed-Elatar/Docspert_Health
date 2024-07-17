from django.conf import settings
from django.conf.urls.static import static

from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('',index,name="index" ),
    path('login/',user_login,name="login"),
    path('logout/',user_logout,name="logout"),
    path('signup/',user_signup,name="signup"),

    path('add-file/',add_csv_file,name="add_file"),
    path('make-transfer',make_transfer,name="make_transfer"),
    path('list-accounts',list_accounts,name="list_accounts"),
    path('list-transfers',list_transfers,name="list_transfers"),

    
    

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)