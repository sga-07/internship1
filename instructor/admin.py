from django.contrib import admin
from .models import Lecture

@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):

    list_display = ('date', 'start_time', 'end_time', 'link',)
    list_filter = ('date',)
    search_fields = ('date', 'start_time', 'end_time', 'link',)
    date_hierarchy = 'date'
