# Generated by Django 3.2.6 on 2021-08-19 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PersonProxy',
            fields=[
            ],
            options={
                'ordering': ['-name'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('model_inheritance.person',),
        ),
    ]