from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET', 'POST'])
def book(request):

    if request.method == 'GET':
        # get all the book
        # serialize them
        # return json
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        # create a book
        # validate the data
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    return HttpResponse("Hello from Backend")


def about(request):
    # return HttpResponse("welcome to about")
    return render(request, 'files/about.html', {'data': "test-data"})
