# Generated by Django 5.1.5 on 2025-01-15 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('inp_text', models.TextField(max_length=999, verbose_name='Enter Your Text')),
            ],
        ),
    ]
