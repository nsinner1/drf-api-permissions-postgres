from django.shortcuts import render
from rest_framework import generics
from .serializer import BooksSerializer
from .models import Books


# Create your views here.


class BookList(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
