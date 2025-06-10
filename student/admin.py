from django.contrib import admin
from .models import Milestone, StudentProfile

admin.site.register(Milestone)

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('nama', 'no_pelajar', 'kumpulan', 'program', 'kod_kursus')
    list_filter = ('kumpulan',)
    search_fields = ('nama', 'no_pelajar', 'kjmpulan__name') 
