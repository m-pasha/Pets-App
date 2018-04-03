from django.contrib import admin

from app.models import Pet


class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_pet', 'name', 'birthday', 'owner')
    list_filter = ('type_pet', 'owner')
    search_fields = ('name',)
    empty_value_display = '-empty-'


admin.site.register(Pet, PetAdmin)
