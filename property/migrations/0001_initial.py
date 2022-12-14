# Generated by Django 2.2.24 on 2022-09-20 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=200, verbose_name='ФИО владельца')),
                ('owners_phonenumber', models.CharField(max_length=20, verbose_name='Номер владельца')),
                ('owner_pure_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=12, region=None, verbose_name='Нормализованный номер владельца')),
                ('new_building', models.BooleanField(choices=[(True, 'Да'), (False, 'Нет')], null=True, verbose_name='Новостройка')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Когда создано объявление')),
                ('description', models.TextField(blank=True, verbose_name='Текст объявления')),
                ('price', models.IntegerField(db_index=True, verbose_name='Цена квартиры')),
                ('town', models.CharField(db_index=True, max_length=50, verbose_name='Город, где находится квартира')),
                ('town_district', models.CharField(blank=True, help_text='Чертаново Южное', max_length=50, verbose_name='Район города, где находится квартира')),
                ('address', models.TextField(help_text='ул. Подольских курсантов д.5 кв.4', verbose_name='Адрес квартиры')),
                ('floor', models.CharField(help_text='Первый этаж, последний этаж, пятый этаж', max_length=3, verbose_name='Этаж')),
                ('rooms_number', models.IntegerField(db_index=True, verbose_name='Количество комнат в квартире')),
                ('living_area', models.IntegerField(blank=True, db_index=True, null=True, verbose_name='количество жилых кв.метров')),
                ('has_balcony', models.NullBooleanField(db_index=True, verbose_name='Наличие балкона')),
                ('active', models.BooleanField(db_index=True, verbose_name='Активно-ли объявление')),
                ('construction_year', models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Год постройки здания')),
                ('like', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Лайки')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Owner_name', models.CharField(max_length=200, verbose_name='Имя владельца')),
                ('owner_phonenumber', models.CharField(max_length=20, verbose_name='Номер владельца')),
                ('owner_pure_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=12, region=None, verbose_name='Нормализованный номер владельца')),
                ('owner_apartments', models.ManyToManyField(blank=True, db_index=True, related_name='flat_owners', to='property.Flat', verbose_name='Квартиры в собственности')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_complaint', models.TextField(verbose_name='Текст жалобы')),
                ('complained_apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.Flat', verbose_name='Квартира, на которую пожаловались')),
                ('who_complained', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался')),
            ],
        ),
    ]
