from django.urls import path
from Authentication_app.views import *
from Books_app.views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('registration/', Registration,name='registration'),
    path('login/', MyTokenobtainedPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get_user_details/', GetUserDetails, name='get_user_details'),
    path('update_user/', UpdateUser,name='update_user'),
    
    path('bookmanagement/',BookManagement.as_view(),name='book_management'),
    path('readinglist_management/',ReadingList_Management.as_view(),name='readinglist_management')
]
