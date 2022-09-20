from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.owner_apartments.through
    raw_id_fields = ('owner',)


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner', 'id')
    readonly_fields = ['created_at']
    list_display = (
        'id',
        'address',
        'price',
        'owners_phonenumber',
        'owner_pure_phone',
        'new_building',
        'construction_year',
        'town'
    )
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ('like',)
    inlines = [OwnerInline, ]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = (
        'who_complained',
        'complained_apartment'
    )


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('owner_apartments',)
    search_fields = ('Owner_name',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
