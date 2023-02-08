from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
import random

from .models import Tweet 

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)

def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{"id":x.id, "content": x.content, "likes": random.randint(0, 250) } for x in qs]
    data = {
        "isUser": False,
        "response": tweets_list
    }

    return JsonResponse(data)








def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIEW
    Consumed by JavaScript
    return json data
    """
    data = {
        "id": tweet_id,
        # "content": obj.content,
        #"image_path": obj.image.url
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not found"
        status = 404
    return JsonResponse(data, status=status)

    