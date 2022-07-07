from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Signup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=10, null=True)
    dob = models.CharField(max_length=10, null=True)
    follower = models.IntegerField(max_length=200, null=True)
    following = models.IntegerField(max_length=200, null=True)
    que_asked = models.IntegerField(max_length=100, null=True)
    answered = models.IntegerField(max_length=100, null=True)
    usr_img = models.ImageField(upload_to="img/", default="")

    def _str_(self):
        return self.user.username


class Questions(models.Model):
    id = models.AutoField
    que = RichTextField(blank=True, null=True)
    topic = models.CharField(max_length=100, null=True)
    ans = RichTextField(blank=True, null=True)
    user = models.CharField(max_length=50, null=True)
    user_id = models.IntegerField(max_length=100, null=True)
    atopic = models.CharField(max_length=100, null=True)
    h = models.IntegerField(max_length=200, null=True)
    nh = models.IntegerField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)


class Feedback(models.Model):
    feedback_name = models.CharField(max_length=20, null=True)
    feedback_contact = models.CharField(max_length=30, null=True)
    feedback_email = models.CharField(max_length=10, null=True)
    feedback_comment = RichTextField(blank=True, null=True)


class Helpful(models.Model):
    num = models.IntegerField(max_length=200, null=True)
    num2 = models.IntegerField(max_length=200, null=True)
    numid = models.IntegerField(max_length=200, null=True)


class Blog(models.Model):
    id = models.AutoField
    user_id = models.IntegerField(default=1, max_length=200, null=True)
    user_name = models.CharField(max_length=200, null=True)
    topic = models.CharField(max_length=200, null=True)
    blog_c = RichTextField(blank=True, null=True)
