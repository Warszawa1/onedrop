from django.db import models
import random
from django.conf import settings

User = settings.AUTH_USER_MODEL

class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Tweet(models.Model):
    # Maps to SQL data
    # id is a hidden field that Django has 
    # id = models.AutoField(primary_key=True)
    # many users can have one or many tweets but one tweet can have
    # only one user
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)#once the user is gone all his stuff is too
    likes = models.ManyToManyField(User, related_name='tweet_user', blank=True, through=TweetLike)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    # the string representation on the object itself
    # def __str__(self):
    #     return self.content
    class Meta:
        ordering = ['-id']


    @property
    def is_retweet(self):
        return self.parent != None
        


    def serialize(self):
        '''
        Can be deleted
        '''
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 200),
            # "image": self.image.url
        }
