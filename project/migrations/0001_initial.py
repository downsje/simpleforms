# Generated by Django 3.0 on 2021-06-25 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('email_address', models.CharField(max_length=100)),
                ('subscription_type', models.CharField(max_length=5)),
            ],
        ),
    ]
