from .models import NotePost
from .serializers import NotePostSerializer, NoteListSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class NoteListView(APIView):
    """
    List all titles of note snippets
    """
    def get(self, request, format=None):
        note_snippets = NotePost.objects.all()
        serializer = NoteListSerializer(note_snippets, many=True)
        return Response(serializer.data)


class NoteView(APIView):
    """
    get, update or delete a particular note snippet
    """
    def get_object(self, pk):
        try:
            return NotePost.objects.get(pk=pk)
        except NotePost.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = NotePostSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = NotePostSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"message": "Note Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)


class NoteCreateView(APIView):
    """
    create a new note snippet
    """
    def post(self, request, format=None):
        serializer = NotePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)