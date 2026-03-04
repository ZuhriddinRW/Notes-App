from django.contrib import admin
from notes.models import Category, Note

admin.site.register ( [Category, Note] )