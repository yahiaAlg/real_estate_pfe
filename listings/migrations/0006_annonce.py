# Generated by Django 5.0.3 on 2024-04-04 09:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_alter_listing_customer_alter_listing_realtor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annonce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('launching_date', models.DateField()),
                ('title', models.TextField(max_length=50)),
                ('content', models.TextField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('promotionel_information', models.TextField(blank=True)),
                ('real_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.listing')),
            ],
        ),
    ]
