# Generated by Django 4.0.5 on 2022-06-20 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunzapp', '0003_child_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='financialNeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('need_1', models.CharField(max_length=100)),
                ('need_2', models.CharField(max_length=100)),
                ('need_3', models.CharField(max_length=100)),
                ('need_4', models.CharField(max_length=100)),
                ('need_5', models.CharField(max_length=100)),
                ('need_6', models.CharField(max_length=100)),
            ],
        ),
    ]
