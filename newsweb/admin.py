from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "JACAI ADMIN"
admin.site.site_title = "JACAI"
admin.site.index_title = "API List"

admin.site.register(ArticleType)
admin.site.register(ResearchInterest)
admin.site.register(Citation)
admin.site.register(Issue)
admin.site.register(Volume)
admin.site.register(Author)
admin.site.register(PublishedArticles)