# Generated by Django 3.2.9 on 2021-11-16 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    def fill_cars(apps, schema_editor):
        Car = apps.get_model('api', 'Car')
        for i in range(10):
            car = Car(name=f'car name {i}', description=f'car desc {i}', price=100*i + 100).save()


    operations = [
        migrations.RunPython(fill_cars),
    ]
