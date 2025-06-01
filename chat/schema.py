import graphene
from graphene_django.types import DjangoObjectType
from .models import Room, Participant, ChatParticipantRoleChoices
from .graphql_subscriptions import RoomCreatedSubscription

class Subscription(graphene.ObjectType):
    room_created = RoomCreatedSubscription.Field()

schema = graphene.Schema(query=Query, mutation=Mutation, subscription=Subscription)
class Query(graphene.ObjectType):
    # Ajoute ici tes champs GraphQL
    pass

class Mutation(graphene.ObjectType):
    # Ajoute ici tes mutations
    pass

class Subscription(graphene.ObjectType):
    # Ajoute ici tes subscriptions
    pass



class ChatParticipantRoleEnum(graphene.Enum):
    HOST  = ChatParticipantRoleChoices.HOST
    GUEST = ChatParticipantRoleChoices.GUEST

class RoomType(DjangoObjectType):
    class Meta:
        model = Room
        fields = "__all__"

class ParticipantType(DjangoObjectType):
    role = graphene.Field(ChatParticipantRoleEnum)
    class Meta:
        model = Participant
        fields = "__all__"
    def resolve_role(self, info):
        return self.role.upper() 
    
    
class Query(graphene.ObjectType):
    all_rooms        = graphene.List(RoomType)
    room             = graphene.Field(RoomType, id=graphene.ID(required=True))
    all_participants = graphene.List(ParticipantType)
    participant      = graphene.Field(ParticipantType, id=graphene.ID(required=True))

    def resolve_all_rooms(root, info):
        return Room.objects.all()
    def resolve_room(root, info, id):
        return Room.objects.get(pk=id)

    def resolve_all_participants(root, info):
        return Participant.objects.all()
    def resolve_participant(root, info, id):
        return Participant.objects.get(pk=id)

class CreateRoom(graphene.Mutation):
    room = graphene.Field(RoomType)
    class Arguments:
        code = graphene.String(required=True)
        name = graphene.String(required=True)
    def mutate(self, info, code, name):
        r = Room.objects.create(code=code, name=name)
        return CreateRoom(room=r)

class UpdateRoom(graphene.Mutation):
    room = graphene.Field(RoomType)
    class Arguments:
        id   = graphene.ID(required=True)
        name = graphene.String()
    def mutate(self, info, id, name=None):
        r = Room.objects.get(pk=id)
        if name: r.name = name; r.save()
        return UpdateRoom(room=r)

class DeleteRoom(graphene.Mutation):
    ok = graphene.Boolean()
    class Arguments:
        id = graphene.ID(required=True)
    def mutate(self, info, id):
        Room.objects.get(pk=id).delete()
        return DeleteRoom(ok=True)

class CreateParticipant(graphene.Mutation):
    participant = graphene.Field(ParticipantType)
    class Arguments:
        username = graphene.String(required=True)
        role     = ChatParticipantRoleEnum(required=True)
        room_id  = graphene.ID(required=True)
    def mutate(self, info, username, role, room_id):
        room = Room.objects.get(pk=room_id)
        p = Participant.objects.create(
            username=username, role=role.value, room=room
        )
        return CreateParticipant(participant=p)

class UpdateParticipant(graphene.Mutation):
    participant = graphene.Field(ParticipantType)
    class Arguments:
        id       = graphene.ID(required=True)
        username = graphene.String()
        role     = ChatParticipantRoleEnum()
    def mutate(self, info, id, username=None, role=None):
        p = Participant.objects.get(pk=id)
        if username: p.username = username
        if role:     p.role = role.value
        p.save()
        return UpdateParticipant(participant=p)

class DeleteParticipant(graphene.Mutation):
    ok = graphene.Boolean()
    class Arguments:
        id = graphene.ID(required=True)
    def mutate(self, info, id):
        Participant.objects.get(pk=id).delete()
        return DeleteParticipant(ok=True)

class Mutation(graphene.ObjectType):
    create_room        = CreateRoom.Field()
    update_room        = UpdateRoom.Field()
    delete_room        = DeleteRoom.Field()
    create_participant = CreateParticipant.Field()
    update_participant = UpdateParticipant.Field()
    delete_participant = DeleteParticipant.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)