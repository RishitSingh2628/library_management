from rest_framework import serializers
from .models import Transaction
from books.models import Book
from members.models import Member

class TransactionSerializer(serializers.ModelSerializer):
    book_title=serializers.CharField(source='book.title', read_only=True)
    member_name=serializers.CharField(source='member.name', read_only=True)

    class Meta:
        model=Transaction
        fields='__all__'
        read_only_fields=('id', 'issue_date', 'return_date')

class IssueBookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields=['book', 'member']

    def validate(self, data):
        book=data['book']
        member=data['member']

        if not member.is_active:
            raise serializers.ValidationError("Member not active")
        
        if book.available_copies <=0:
            raise serializers.ValidationError("No Copies Available")

        if Transaction.objects.filter(
            book=book,
            member=member,
            status='issued'
        ).exists():
            raise serializers.ValidationError("Member already has this book")
        
        return data

class ReturnBookSerializer(serializers.Serializer):
    transaction_id=serializers.IntegerField()

    def validate_transaction_id(self, value):
        try:
            transaction = Transaction.objects.get(id=value, status='issued')
            return value
        except Transaction.DoesNotExist:
            raise serializers.ValidationError("Book Already returned")