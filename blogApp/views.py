from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings
import os

from serializers import PostSerializer



class ReactAppView(View):

    def get(self, request):
        try:

            with open(os.path.join(settings.REACT_APP, 'build', 'index.html')) as file:
                return HttpResponse(file.read())

        except :
            return HttpResponse(
                """
                index.html not found ! build your React app !!
                """,
                status=501,
            )


class PostListCreateAPIView(ListCreateAPIView):
    serializer_class = PostSerializer


