from timetable.models import Calendar, Classification, Color, Event, EventClassification
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


class CalendarAdmin(admin.ModelAdmin):
    list_display = ('color_display', 'name', )
    list_display_links = ('name', )

    prepopulated_fields = {'slug': ('name', )}

    fieldsets = ((None, {'fields': ('name', 'slug', 'color', )}),)

admin.site.register(Calendar, CalendarAdmin)


class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name', )

    prepopulated_fields = {'slug': ('name', )}

    fieldsets = ((None, {'fields': ('name', 'slug', 'description', )}),)

admin.site.register(Classification, ClassificationAdmin)


class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'color_display', )
    list_display_links = ('name', )

    fieldsets = ((None, {'fields': ('name', 'color', )}),)

admin.site.register(Color, ColorAdmin)


class EventClassificationInline(admin.StackedInline):
    model = EventClassification
    extra = 0


class EventAdmin(admin.ModelAdmin):
    list_display = ('calendar_color', 'name', 'start_date_time', 'end_date_time', 'all_day_event', 'active', )
    list_display_links = ('name', )
    list_filter = ('calendar', )
    search_fields = ['name', ]

    inlines = [EventClassificationInline, ]

    prepopulated_fields = {'slug': ('name', )}

    fieldsets = ((None, {'fields': ('calendar', 'name', 'slug', 'description')}),
                (_('Date and Time'), {'fields': ('start_date_time', 'end_date_time', 'all_day_event', )}),
                (_('Classification'), {'fields': ('tags', )}), )

admin.site.register(Event, EventAdmin)
