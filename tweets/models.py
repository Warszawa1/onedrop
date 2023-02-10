from django.db import models
import random
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Tweet(models.Model):
    # id is a hidden field that Django has 
    # id = models.AutoField(primary_key=True)
    # many users can have one or many tweets but one tweet can have
    # only one user
    user = models.ForeignKey(User, on_delete=models.CASCADE)#once the user is gone all his stuff is too
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)

    # the string representation on the object itself
    # def __str__(self):
    #     return self.content
    class Meta:
        ordering = ['-id']


    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 200),
            # "image": self.image.url
        }
