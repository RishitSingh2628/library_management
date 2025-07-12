from django.urls import path
from . import views

urlpatterns=[
    path('transactions/', views.TransactionListView.as_view(),name='transaction-list'),
    path('transaction/issue/', views.issue_book, name='issue-book'),
    path('transaction/return/', views.return_book, name='return-book')
]