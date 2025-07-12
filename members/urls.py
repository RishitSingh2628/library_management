from django.urls import path
from . import views

urlpatterns=[
    path('members/', views.MemberListCraete.as_view(),name='member-list-create'),
    path('members/<int:pk>', views.MemberRetrieveUpdateDestroyView.as_view(), name='member-detail')
]