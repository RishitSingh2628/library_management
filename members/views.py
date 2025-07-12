from django.shortcuts import render
from members.models import Member
from rest_framework import generics
from members.serializers import MemberSerializer

class MemberListCraete(generics.ListCreateAPIView):
    queryset=Member.objects.all()
    serializer_class=MemberSerializer


class MemberRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Member.objects.all()
    serializer_class=MemberSerializer

class MemberRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Member.objects.all()
    serializer_class=MemberSerializer
