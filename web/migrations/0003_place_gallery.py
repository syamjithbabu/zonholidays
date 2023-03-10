# Generated by Django 4.1.4 on 2023-01-05 06:36

from django.db import migrations, models
import django.db.models.deletion
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_delete_gallery_delete_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='image/testimagemodel/', verbose_name='Image')),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.place')),
            ],
        ),
    ]
