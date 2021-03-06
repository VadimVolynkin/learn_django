# Generated by Django 3.2.6 on 2021-08-18 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onetoone', '0003_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='onetoone.person')),
                ('salary', models.PositiveIntegerField()),
            ],
        ),
    ]
