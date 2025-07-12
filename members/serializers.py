from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Member
        fields='__all__'
        read_only_fields=('id','membership_date')

    def validate_email(self, value):
        if Member.objects.filter(email=value).exists():
            if not self.instance or self.instance.email != value:
                raise serializers.ValidationError("Email exists")
        return value


    