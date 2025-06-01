import channels_graphql_ws
from .models import Room
from graphene_django.types import DjangoObjectType
import graphene
class RoomCreatedSubscription(channels_graphql_ws.Subscription):
    room = graphene.Field(lambda: RoomType)

    class Arguments:
        pass

    def subscribe(self, info):
        return ["room_created"]

    def publish(self, info):
        return RoomCreatedSubscription(room=self.room)

    @classmethod
    def broadcast(cls, group, payload):
        cls.broadcast(group=group, payload=payload)
