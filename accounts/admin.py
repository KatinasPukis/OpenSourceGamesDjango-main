from django.contrib import admin
from .models  import Comment, Customer, GameComment , UserGame , NewsClass, Vote
# Register your models here.
admin.site.register(Customer),
admin.site.register(UserGame),
admin.site.register(NewsClass),
admin.site.register(Comment),
admin.site.register(GameComment),
admin.site.register(Vote),