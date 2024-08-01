from django.contrib import admin
from .models import (Availability, TimeSlotAvailability, 
SpaService, SpecificDate, TimeSlot, ServiceCategory)

# Inline for SpecificDate within AvailabilityAdmin
class SpecificDateInline(admin.TabularInline):
    model = Availability.specific_dates.through
    extra = 3  # Number of empty forms to display for adding new dates

# Inline for TimeSlotAvailability within AvailabilityAdmin
class TimeSlotAvailabilityInline(admin.TabularInline):
    model = TimeSlotAvailability
    extra = 5  # Number of empty forms to display for adding new time slots
    fields = ['specific_date', 'time_slot', 'is_available']
    autocomplete_fields = ['time_slot']

# Availability Admin
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ("spa_service",)
    inlines = [SpecificDateInline, TimeSlotAvailabilityInline]

admin.site.register(Availability, AvailabilityAdmin, )


# Register TimeSlot and SpaService separately
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('time',)
    search_fields = ['time']

admin.site.register(TimeSlot, TimeSlotAdmin)


class SpaServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "is_access")
    list_filter = ("category", "is_access")

admin.site.register(SpaService, SpaServiceAdmin)
