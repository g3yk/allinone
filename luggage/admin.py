from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from .models import Luggage

# Register your models here.


class LuggageAdmin(admin.ModelAdmin):
    list_display = ("luggage_id", "weight", "passenger")
    search_fields = ("luggage_id",)
    readonly_fields = ("luggage_id",)
    list_filter = (
        "is_status1",
        "is_status2",
        "is_status3",
        "is_status4",
    )


admin.site.register(Luggage, LuggageAdmin)
