from django.contrib import admin

from main.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'number_of_unique',)
    fields = ('text', 'number_of_unique',)
    readonly_fields = ('number_of_unique',)

    def save_model(self, request, obj, form, change):
        if 'text' in form.changed_data:
            obj.number_of_unique = len(set(obj.text.split()))
        obj.save()
