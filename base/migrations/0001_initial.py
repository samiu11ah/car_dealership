# Generated by Django 4.1.3 on 2022-11-26 12:31

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
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cars/')),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('model_year', models.CharField(default='1960', max_length=4)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('condition', models.CharField(choices=[('new', 'new'), ('old', 'old')], max_length=100)),
                ('condition_rating', models.CharField(blank=True, choices=[('10', '10/10'), ('9', '9/10'), ('8', '8/10'), ('7', '7/10'), ('6', '6/10'), ('5', '5/10'), ('4', '4/10'), ('3', '3/10'), ('2', '2/10'), ('1', '1/10')], max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('sold', models.BooleanField(default=False)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('sold_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
