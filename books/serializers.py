from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'
        read_only_fields=('id', 'created_at','updated_at')

    def validate(self, data):
        if data.get('available_copies', 0) > data.get('total_copies', 0):
            raise serializers.ValidationError(
                "Available copies cannot exceed total copies"
            )
        return data

    def validate_isbn(self, value):
        if len(value) not in [10,13]:
            raise serializers.ValidationError("ISBN length must be 10 or 13")
        return value