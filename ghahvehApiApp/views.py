from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

@api_view(['GET'])
def index(request):
    return Response({"Success": "The setup was successful"})

@api_view(['GET'])
def GetAllPosts(request):
    get_posts = Post.objects.all()
    serializer = PostSerializer(get_posts, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def UpdatePost(request):
    post_id = request.data.get('post_id')
    get_new_title = request.data.get('new_title')
    get_new_content = request.data.get('new_content')
    get_image = request.data.get('image')  # Get the image data from request

    try:
        post = Post.objects.get(id=post_id)

        if get_new_title:
            post.title = get_new_title
        if get_new_content:
            post.content = get_new_content
        if get_image:
            post.image = get_image

        post.save()
        return Response({"Success": "The post was successfully updated"}, status=200)

    except Post.DoesNotExist:
        return Response({"Error": "The post does not exist"}, status=404)
