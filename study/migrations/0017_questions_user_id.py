# Generated by Django 4.0.5 on 2022-06-20 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0016_signup_answered_signup_follower_signup_following_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='user_id',
            field=models.IntegerField(max_length=100, null=True),
        ),
    ]
