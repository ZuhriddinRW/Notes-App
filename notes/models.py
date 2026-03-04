from django.db import models
from users.models import User


class TimeStampedModel ( models.Model ) :
    created_at = models.DateTimeField ( auto_now_add=True )
    updated_at = models.DateTimeField ( auto_now=True )

    class Meta :
        abstract = True


class Category ( TimeStampedModel ) :
    user = models.ForeignKey ( User, on_delete=models.CASCADE )
    name = models.CharField ( max_length=50 )
    color = models.CharField ( max_length=50 )

    def __str__(self) :
        return self.name


class Note ( TimeStampedModel ) :
    user = models.ForeignKey ( User, on_delete=models.CASCADE )
    category = models.ForeignKey ( Category, null=True, blank=True, on_delete=models.SET_NULL )
    title = models.CharField ( max_length=100 )
    content = models.TextField ( blank=True )
    color = models.CharField ( max_length=50 )
    is_pinned = models.BooleanField ( default=False )
    is_archived = models.BooleanField ( default=False )

    def __str__(self) :
        return self.title