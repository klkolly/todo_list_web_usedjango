# Generated by Django 3.1.5 on 2021-02-04 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_text', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
