from django.contrib import admin
from . import models

admin.site.register(models.Categoriya)
admin.site.register(models.News)
admin.site.register(models.Region)
admin.site.register(models.NewsImage)
admin.site.register(models.CommentNews)
admin.site.register(models.StatuxNews)