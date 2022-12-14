# Generated by Django 2.2.24 on 2022-09-20 14:51

from django.db import migrations


def transfer_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    owners = Owner.objects.all()
    if owners.exists():
        for flat in Flat.objects.iterator():
            Owner.objects.get_or_create(
                name=flat.owner,
                defaults={
                    'pure_phone': flat.owner_pure_phone
                }
            )


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0003_owner'),
    ]

    operations = [
        migrations.RunPython(transfer_owners)
    ]
