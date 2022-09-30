# Generated by Django 2.2.13 on 2022-09-30 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='socialMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_url', models.URLField(blank=True, null=True)),
                ('twitter_url', models.URLField(blank=True, null=True)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('skype_url', models.URLField(blank=True, null=True)),
                ('github_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='whoareyou',
            name='facebook_url',
        ),
        migrations.RemoveField(
            model_name='whoareyou',
            name='github_url',
        ),
        migrations.RemoveField(
            model_name='whoareyou',
            name='linkedin_url',
        ),
        migrations.RemoveField(
            model_name='whoareyou',
            name='skype_url',
        ),
        migrations.RemoveField(
            model_name='whoareyou',
            name='twitter_url',
        ),
    ]