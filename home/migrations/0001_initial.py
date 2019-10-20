# Generated by Django 2.2.6 on 2019-10-20 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('nic', models.CharField(blank=True, max_length=13, null=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=13, null=True)),
            ],
        ),
    ]
