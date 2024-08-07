from django.contrib import admin
from .models import Publication
from .models import Comments
from.models import User




admin.site.register(Publication)
admin.site.register(Comments)
admin.site.register(User)

