from django.shortcuts import render
from api.models import Note

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.views import APIView
from api.serializers import NoteSerializer

class NotesApiView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer



class NoteApiView(APIView):
    def get(self, request, pk):
        note = Note.objects.get(id = pk)
        ser = NoteSerializer(note)
        return Response(ser.data)
    
    def delete(self, request,pk):

        Note.objects.get(id=pk).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk, format=None):
        note = Note.objects.get(id=pk)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


