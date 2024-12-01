from rest_framework.serializers import ModelSerializer
from apps.post.models import Post
from rest_framework import status
from apps.post.models import Post
from apps.post.api.serializers.import Modelsserializaers
class postSerializer(ModelSerializer):
          class Meta:
                  model = Post
                  fields = ['title', 'description,' 'orden','crear_all']
                  #fields = ['tiltle']