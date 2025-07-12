from django.db import models
from books.models import Book
from members.models import Member

class Transaction(models.Model):
    STATUS=[
        ('issued', 'Issued'),
        ('returned', 'Returned')
    ]

    
    book=models.ForeignKey(Book, on_delete=models.CASCADE)
    member=models.ForeignKey(Member, on_delete=models.CASCADE)
    issue_date=models.DateTimeField(auto_now_add=True)
    return_date=models.DateTimeField(null=True, blank=True)
    status= models.CharField(max_length=10, choices=STATUS, default='issued')

    def __str__(self):
        return f"{self.book.title} - {self.member.name}"

    class Meta:
        ordering=['-issue_date']
