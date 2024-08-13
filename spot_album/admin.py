from django.contrib import admin
from .models import Publication
from .models import Comments
from.models import User
from .models import Friends




admin.site.register(Publication)
admin.site.register(Comments)
admin.site.register(User)
admin.site.register(Friends)
