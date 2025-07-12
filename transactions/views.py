from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.status import HTTP_200_OK

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer, IssueBookSerializer, ReturnBookSerializer
from books.models import Book

class TransactionListView(generics.ListAPIView):
    queryset=Transaction.objects.all()
    serializer_class=TransactionSerializer


@api_view(["POST"])
def issue_book(request):
    serializer= IssueBookSerializer(data=request.data)
    if serializer.is_valid():
        book=serializer.validated_data['book']
        member=serializer.validated_data['member']

        transaction=Transaction.objects.create(
            book=book,
            member=member,
            status='issued'
        )

        book.available_copies -= 1
        book.save()

        return Response(TransactionSerializer(transaction).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def return_book(request):
    serializer=ReturnBookSerializer(data=request.data)
    if serializer.is_valid():
        transaction_id=serializer.validated_data['transaction_id']

        try:
            transaction=Transaction.objects.get(id=transaction_id, status='issued')

            transaction.return_data=timezone.now()
            transaction.status='returned'
            transaction.save()

            book=transaction.book
            book.available_copies += 1
            book.save()

            return Response(TransactionSerializer(transaction).data, status=HTTP_200_OK)

        except Transaction.DoesNotExist:
            return Response({'error':'Already Returned'},status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)