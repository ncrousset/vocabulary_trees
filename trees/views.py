from rest_framework import generics
from .models import Tree
from .serializers import TreeSerializer

class TreeList(generics.ListCreateAPIView):
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer

class TreeDetail(generics.RetrieveUpdateDestroyAPIView):
    pass