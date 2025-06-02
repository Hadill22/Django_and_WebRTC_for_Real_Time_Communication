import channels_graphql_ws
import graphene

# (Ne plus importer RoomType ici pour éviter la circularité)
# from .schema import RoomType

class RoomCreatedSubscription(channels_graphql_ws.Subscription):
    # 1) Définition différée du type RoomType via lambda et import à l’intérieur :
    room = graphene.Field(lambda: __import__("chat.schema", fromlist=["RoomType"]).RoomType)

    class Arguments:
        pass

    def subscribe(self, info):
        return ["room_created"]

    def publish(self, info):
        # self.room contient déjà l’instance Room
        return RoomCreatedSubscription(room=self.room)

    @classmethod
    def broadcast(cls, group, payload):
        # Appeler la méthode parente pour envoyer dans le groupe WebSocket
        channels_graphql_ws.Subscription.broadcast(group=group, payload=payload)
