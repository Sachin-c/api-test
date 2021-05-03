from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import forms
from django.utils import timezone
# from emoji_picker.widgets import EmojiPickerTextInputAdmin, EmojiPickerTextareaAdmin


class Advisor(models.Model):
    advisor_id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=420)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # image = models.ImageField(upload_to='profile_pics', null=False, blank=False)


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    advisor_name = models.TextField(max_length=420)
    advisor_image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    advisor_id = models.IntegerField()
    book_time = models.DateTimeField(max_length=420)
