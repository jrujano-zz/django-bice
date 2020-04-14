from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .viewsets import ObtainTokenPairWithColorView, BiceUserCreate

urlpatterns = [
    # path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/obtain/', ObtainTokenPairWithColorView.as_view(), name='token_create'),  
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/create/', BiceUserCreate.as_view(), name="create_user"),
]