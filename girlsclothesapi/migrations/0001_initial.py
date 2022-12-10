# Generated by Django 4.1.3 on 2022-12-10 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClothingItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_description', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=15)),
                ('clean_or_dirty', models.BooleanField(blank=True, null=True)),
                ('item_fits', models.BooleanField(blank=True, null=True)),
                ('sibling_has_match', models.BooleanField()),
                ('item_image', models.ImageField(blank=True, null=True, upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='ClothingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ClothingUse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Outfit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outfit_description', models.CharField(max_length=50)),
                ('outfit_image', models.ImageField(blank=True, null=True, upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='OutfitItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothing_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='girlsclothesapi.clothingitem')),
                ('outfit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='girlsclothesapi.outfit')),
            ],
        ),
        migrations.AddField(
            model_name='outfit',
            name='clothing_items',
            field=models.ManyToManyField(related_name='clothing_items', through='girlsclothesapi.OutfitItem', to='girlsclothesapi.clothingitem'),
        ),
        migrations.CreateModel(
            name='Kid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, max_length=15, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('dress_size', models.CharField(blank=True, max_length=5, null=True)),
                ('shoe_size', models.CharField(blank=True, max_length=5, null=True)),
                ('shirt_size', models.CharField(blank=True, max_length=5, null=True)),
                ('pant_size', models.CharField(blank=True, max_length=5, null=True)),
                ('underwear_or_diaper_size', models.CharField(blank=True, max_length=5, null=True)),
                ('sock_size', models.CharField(blank=True, max_length=5, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItemUse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothing_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='girlsclothesapi.clothingitem')),
                ('clothing_use', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='girlsclothesapi.clothinguse')),
            ],
        ),
        migrations.CreateModel(
            name='ItemsBeingWorn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothing_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='girlsclothesapi.clothingitem')),
                ('outfit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='girlsclothesapi.outfit')),
            ],
        ),
        migrations.AddField(
            model_name='clothingitem',
            name='clothing_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='girlsclothesapi.clothingtype'),
        ),
        migrations.AddField(
            model_name='clothingitem',
            name='clothing_uses',
            field=models.ManyToManyField(related_name='clothing_uses', through='girlsclothesapi.ItemUse', to='girlsclothesapi.clothinguse'),
        ),
        migrations.AddField(
            model_name='clothingitem',
            name='kid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='girlsclothesapi.kid'),
        ),
    ]
