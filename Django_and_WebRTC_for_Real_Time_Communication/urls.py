from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ API REST (DRF) pour /api/participants/ etc.
    path('api/', include('chat.urls')),  # <<--- ajoute /api ici
     path('', include('chat.urls')),  
    # ✅ Authentification JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # ✅ GraphQL (avec graphiql=True pour debug)
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
