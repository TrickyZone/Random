# Generated by Django 2.2.13 on 2022-09-30 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0004_aboutme_asmpe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='asmpe',
            field=models.FileField(upload_to='details/pdfs/'),
        ),
    ]