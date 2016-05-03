from django.contrib import admin

from collection.models import Aktiviteter

class AktivitetAdmin(admin.ModelAdmin):
    model = Aktiviteter
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Aktiviteter,AktivitetAdmin)

#legger name automatisk til slug.