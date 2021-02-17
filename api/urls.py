from django.urls import path
from .views.stretch_views import Stretches, StretchDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('stretches/', Stretches.as_view(), name='stretches'),
    path('stretch/<int:pk>/', StretchDetail.as_view(), name='stretch_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
