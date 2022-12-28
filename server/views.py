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


@api_view(['GET', 'PUT', 'DELETE'])
def book_details(requset, id):

    try:
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if requset.method == 'GET':
        serialzer = BookSerializer(book)
        return Response(serialzer.data)
        pass
    elif requset.method == 'PUT':
        serialzer = BookSerializer(book,data=requset.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif requset.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def index(request):
    return HttpResponse("Hello from Backend")


def about(request):
    # return HttpResponse("welcome to about")
    return render(request, 'files/about.html', {'data': "test-data"})
