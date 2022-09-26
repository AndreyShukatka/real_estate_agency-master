# Generated by Django 2.2.24 on 2022-09-20 15:19

from django.db import migrations


def transfer_owners(apps, schema_editor):
    Flats = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flats.objects.iterator():
        for owner in Owner.objects.filter(name=flat.owner.iterator()):
            owner.flat.add(flat)

            # def transfer_owners(apps, schema_editor):
            #     Flats = apps.get_model('property', 'Flat')
            #     Owner = apps.get_model('property', 'Owner')
            #     owners = Owner.objects.all()
            #     for owner in owners:
            #         owners_all_flats = Flats.objects.filter(owner=owner.Owner_name)
            #         for flat in owners_all_flats:
            #             owner.owner_apartments.add(flat)
            #             owner.save()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0004_auto_20220920_1751'),
    ]

    operations = [
        migrations.RunPython(transfer_owners)
    ]
