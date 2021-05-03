from django.urls import path
from auth.views import MyObtainTokenPairView, RegisterView
from rest_framework_simplejwt.views import TokenRefreshView
from auth.views import (
    api_advisor_view,
    api_advisor_view_post,
    api_booking_view,

)

app_name = 'auth'
urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('<int:userid>/advisor/<int:advisorid>/', api_advisor_view_post, name='alist'),
    path('<int:userid>/advisor/', api_advisor_view, name='list'),
    path('<int:userid>/advisor/booking/', api_booking_view, name='blist'),

]
