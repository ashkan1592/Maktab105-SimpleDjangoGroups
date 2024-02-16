from django.contrib import admin
from main.models import Add,Category


class AddAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id','name','category')



admin.site.register(Add,AddAdmin)


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id','name')

admin.site.register(Category,CategoryAdmin)
