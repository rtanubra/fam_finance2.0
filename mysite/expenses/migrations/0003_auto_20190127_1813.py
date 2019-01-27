# Generated by Django 2.1.2 on 2019-01-27 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_expense_method_of_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='method_of_payment',
            field=models.CharField(choices=[('Credit', 'Credit'), ('Cash/Debit', 'Cash/Debit')], default='Cash/Debit', max_length=11),
        ),
    ]