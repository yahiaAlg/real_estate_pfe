# Generated by Django 5.0.3 on 2024-04-05 23:29

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_rename_realstor_order_listings_order_has_arrived'),
        ('listings', '0007_listing_is_published'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='payment_status',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='review_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='commission',
        ),
        migrations.RemoveField(
            model_name='order',
            name='has_arrived',
        ),
        migrations.RemoveField(
            model_name='order',
            name='listings',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='transaction_type',
        ),
        migrations.AddField(
            model_name='order',
            name='arrival_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='order',
            name='listing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.listing'),
        ),
        migrations.AddField(
            model_name='order',
            name='purchase_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('IN_STOREHOUSE', 'In Storehouse'), ('SHIPPED', 'Shipped'), ('ARRIVED', 'Arrived')], default='IN_STOREHOUSE', max_length=13),
        ),
        migrations.AlterField(
            model_name='contact',
            name='consultation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='is_reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='contact',
            name='reponse_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='contact',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
