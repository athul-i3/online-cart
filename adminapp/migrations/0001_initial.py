# Generated by Django 4.1.4 on 2024-04-25 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admincat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_image', models.ImageField(default='sample.jpg', upload_to='cat')),
                ('cat_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('phonenumber', models.TextField()),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mess_title', models.CharField(max_length=20)),
                ('mess_discription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.ImageField(upload_to='products')),
                ('product_name', models.CharField(max_length=30, null=True)),
                ('brand_name', models.CharField(max_length=25)),
                ('product_price', models.IntegerField(null=True)),
                ('product_disc', models.CharField(max_length=20)),
                ('product_warranty', models.CharField(max_length=20, null=True)),
                ('product_delivery', models.CharField(max_length=20, null=True)),
                ('product_rate', models.CharField(max_length=20, null=True)),
                ('Cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.admincat')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_review', models.CharField(max_length=200)),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.products')),
                ('userid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discription', models.CharField(max_length=50)),
                ('cust_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('quantity', models.IntegerField(null=True)),
                ('total', models.FloatField(null=True)),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.products')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.customer')),
            ],
        ),
    ]
