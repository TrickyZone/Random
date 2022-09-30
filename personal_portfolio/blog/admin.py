from django.contrib import admin
from . import models

# admin customization
class AuthorProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'gender', 'date']
    list_filter = ('gender',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author', 'is_draft', 'date']
    list_editable = ['name', 'author', 'is_draft']
    list_filter = ('author', )

class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author', 'is_draft', 'date']
    list_editable = ['name', 'author', 'is_draft']
    list_filter = ('author', )

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'author', 'is_draft', 'pub_date']
    list_editable = ['title', 'category', 'is_draft']
    list_filter = ('category', 'author', 'is_draft')

# Register your models here.   

admin.site.register(models.AuthorProfile, AuthorProfileAdmin)
admin.site.register(models.PostCategory, CategoryAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Post, PostAdmin)


# class DevProfileAdmin(admin.ModelAdmin):
#     list_display = ['id','intro', 'position1', 'position2', 'position3', 'position4']
#     # list_filter = ('position_choice',)


# class MyModelAdmin(admin.ModelAdmin):
#       def has_add_permission(self, request):
#     # if there's already an entry, do not allow adding
#     count = MyModel.objects.all().count()
#     if count == 0:
#       return True

#     return False

class DevProfileAdmin(admin.ModelAdmin):
      list_display = ['id','intro', 'position1', 'position2', 'position3', 'position4']
      def has_add_permission(self, request):
            
    # if there's already an entry, do not allow adding
            count = models.dev_profile.objects.all().count()
            if count == 0:
                return True

            return False
          
admin.site.register(models.dev_profile, DevProfileAdmin)



class sampleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author', 'is_draft', 'date']
    list_editable = ['name', 'author', 'is_draft']
    list_filter = ('author', )
admin.site.register(models.PostSample, sampleAdmin)
