# Generated by Django 4.1.7 on 2023-10-04 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='femaleProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
