# Generated by Django 5.2 on 2025-04-21 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('Status', models.CharField(max_length=255)),
                ('TaskAssigned', models.DateField()),
                ('TaskCompleted', models.DateField()),
            ],
            options={
                'db_table': 'DB_Tasks',
            },
        ),
    ]
