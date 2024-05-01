from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from .models import Luggage

# Register your models here.


class LuggageAdmin(admin.ModelAdmin):
    list_display = ("pk", "weight", "passenger")
    search_fields = ("pk",)
    # readonly_fields = ("pk",)
    list_filter = (
        "status1",
        "status2",
        "status3",
        "status4",
    )


admin.site.register(Luggage, LuggageAdmin)
