from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.apartments.through
    raw_id_fields = ('owner',)

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner', 'id')
    readonly_fields = ['created_at']
    list_display = (
        'id',
        'address',
        'price',
        'owner_pure_phone',
        'new_building',
        'construction_year',
        'town'
    )
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ('likes',)
    inlines = [OwnerInline, ]

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = (
        'who_complained',
        'apartment'
    )

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('apartments',)
    search_fields = ('name',)
