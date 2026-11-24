from django.contrib import admin

from .models import (
    Appointment,
    ArtistProfile,
    PortfolioWork,
    RequestReference,
    Sketch,
    Style,
    TattooRequest,
)


@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class RequestReferenceInline(admin.TabularInline):
    model = RequestReference
    extra = 0


@admin.register(TattooRequest)
class TattooRequestAdmin(admin.ModelAdmin):
    list_display = ("id", "client", "artist", "status", "created_at")
    list_filter = ("status",)
    inlines = [RequestReferenceInline]


admin.site.register([ArtistProfile, PortfolioWork, Sketch, Appointment])