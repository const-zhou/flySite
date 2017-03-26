from django.contrib import admin

# Register your models here.
from .models import SectionItem, Fruit


class SectionInline(admin.TabularInline):
    model = SectionItem

class FruitAdmin(admin.ModelAdmin):
    inlines = [SectionInline]
    fields = ('name', 'description')

admin.site.register(Fruit, FruitAdmin)
# admin.site.register(SectionItem)