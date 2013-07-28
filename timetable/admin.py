from timetable.models import Calendar, Classification, Color, Event, EventClassification
from django.contrib import admin


class CalendarAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )

    prepopulated_fields = {'slug': ('name', )}

    fieldsets = ((None, {'fields': ('name', 'slug', 'color', )}),)

admin.site.register(Calendar, CalendarAdmin)


# class Admin(admin.ModelAdmin):
#     list_display = ('name', )
#     list_display_links = ('name', )
#     list_filter = ('', )

#     prepopulated_fields = {'slug': ('name', )}

#     fieldsets = ((None, {'fields': ('name', 'slug', )}),)

# admin.site.register(, Admin)


class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', )
    list_display_links = ('name', )

    fieldsets = ((None, {'fields': ('name', 'color', )}),)

admin.site.register(Color, ColorAdmin)


# class Admin(admin.ModelAdmin):
#     list_display = ('name', )
#     list_display_links = ('name', )
#     list_filter = ('', )

#     prepopulated_fields = {'slug': ('name', )}

#     fieldsets = ((None, {'fields': ('name', 'slug', )}),)

# admin.site.register(, Admin)


# class Admin(admin.ModelAdmin):
#     list_display = ('name', )
#     list_display_links = ('name', )
#     list_filter = ('', )

#     prepopulated_fields = {'slug': ('name', )}

#     fieldsets = ((None, {'fields': ('name', 'slug', )}),)

# admin.site.register(, Admin)
