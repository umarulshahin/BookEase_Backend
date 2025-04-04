from django.urls import path
from Authentication_app.views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('registration/', Registration,name='registration'),
    path('login/', MyTokenobtainedPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get_user_details/', GetUserDetails, name='get_user_details'),
    path('update_user/', UpdateUser,name='update_user'),
]
