import random
from django.contrib.auth import get_user_model
from rest_framework import views, permissions, status
from rest_framework.response import Response
from server.da_day.models import Note, Question
from server.da_day.serializers import NoteSerializer


UserModel = get_user_model()


class NotesListView(views.APIView):
    permission_classes = (
        permissions.AllowAny,
    )

    def get(self, request, pk):
        queryset = Note.objects.filter(user=pk)
        serializer = NoteSerializer(queryset, many=True)
        emotions = {}

        for n in serializer.data:
            emotions[n.id] = n.emotion

        return Response(data=emotions)


class NoteCreateView(views.APIView):
    queryset = Question.objects.all()
    permission_classes = (
        permissions.AllowAny,
    )

    def get(self, request, pk):
        question = random.choice(self.queryset.all()).__str__()
        return Response({'question': question}, status=status.HTTP_200_OK)

    def post(self, request, pk):
        text = request.data.get('text')
        avatar = request.data.get('avatar')

        user = UserModel.objects.get(id=pk)

        note = Note(
            description=text,
            emotion=avatar,
            user=user,
        )

        note.save()

        return Response(status=status.HTTP_200_OK)
