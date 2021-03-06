# Generated by Django 2.1.2 on 2019-01-26 19:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0002_auto_20190126_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('expense_description', models.CharField(max_length=200)),
                ('expense_date', models.DateField(default=datetime.datetime.now)),
                ('expense_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.Category')),
            ],
        ),
    ]
