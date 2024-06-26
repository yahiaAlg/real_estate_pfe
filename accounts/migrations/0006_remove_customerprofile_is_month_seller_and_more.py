# Generated by Django 5.0.4 on 2024-04-19 09:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_customerprofile_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerprofile',
            name='is_month_seller',
        ),
        migrations.RemoveField(
            model_name='customerprofile',
            name='profile_img',
        ),
        migrations.RemoveField(
            model_name='realtorprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='realtorprofile',
            name='name',
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='is_month_customer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='profile_image',
            field=models.ImageField(default='assets/img/customer-default.png', upload_to='profiles/%y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='status',
            field=models.CharField(choices=[('Guest', 'Guest'), ('PREMIUM', 'Premium'), ('Normal', 'Normal')], default='Normal', max_length=10),
        ),
        migrations.AlterField(
            model_name='realtorprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='realtorprofile',
            name='profile_image',
            field=models.ImageField(default='assets/img/realtor-default.png', upload_to='realtors/%Y/%m/%d/'),
        ),
        migrations.CreateModel(
            name='DesignerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('portfolio_url', models.URLField(blank=True)),
                ('skills', models.TextField(blank=True)),
                ('bio', models.TextField(blank=True)),
                ('profile_image', models.ImageField(default='assets/img/designer-default.png', upload_to='designers/%Y/%m/%d/')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
