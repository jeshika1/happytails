from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import AdoptionApplication, Animal, ContactMessage, addyours,Process

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')
    


admin.site.register(ContactMessage)

admin.site.register(addyours)

admin.site.register(AdoptionApplication)

class ProcessAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')  # add other fields as needed
    actions = ['accept_process', 'deny_process']

    def accept_orders(self, request, queryset):
        queryset.update(status='accepted')

    def deny_orders(self, request, queryset):
        queryset.update(status='denied')

admin.site.register(Process, ProcessAdmin)