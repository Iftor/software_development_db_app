# Generated by Django 3.2.9 on 2021-12-12 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_software_development', '0002_alter_project_beginning_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='orders_number',
            field=models.IntegerField(default=0, verbose_name='Количество заказов'),
        ),
    ]