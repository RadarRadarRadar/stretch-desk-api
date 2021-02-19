from django.urls import path
from .views.stretch_views import Stretches, StretchDetail, MyStretches
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Stretches
    path('stretches/', Stretches.as_view(), name='stretches'),
    path('stretch/<int:pk>/', StretchDetail.as_view(), name='stretch_detail'),
    # Owned Stretches
    path('mystretches/', MyStretches.as_view(), name='my_stretches'),
    # Authorization
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
