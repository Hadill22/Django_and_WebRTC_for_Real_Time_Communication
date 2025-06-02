from django.urls import path, include
from .views import join_room
from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, ParticipantViewSet, SessionLogViewSet
from . import views
from .views import create_room, join_room
router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'participants', ParticipantViewSet)
router.register(r'sessionlogs', SessionLogViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('create-room/', views.create_room, name='create_room'),
    path('join/', join_room, name='join_room'),
    path('join/<str:room_id>/', views.chat_room, name='chat_room'),
]
