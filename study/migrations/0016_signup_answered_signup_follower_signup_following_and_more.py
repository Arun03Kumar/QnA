# Generated by Django 4.0.5 on 2022-06-20 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0015_remove_signup_answered_remove_signup_follower_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='answered',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='follower',
            field=models.IntegerField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='following',
            field=models.IntegerField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='que_asked',
            field=models.IntegerField(max_length=100, null=True),
        ),
    ]
