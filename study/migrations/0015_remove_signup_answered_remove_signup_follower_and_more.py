# Generated by Django 4.0.5 on 2022-06-20 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0014_signup_answered_signup_follower_signup_following_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='answered',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='follower',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='following',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='que_asked',
        ),
    ]
