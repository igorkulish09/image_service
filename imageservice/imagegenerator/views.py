from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ImageSerializer
from rest_framework.renderers import JSONRenderer


class GenerateImageView(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            width = serializer.validated_data['width']
            height = serializer.validated_data['height']
            color = serializer.validated_data['color']
            title = serializer.validated_data['title']
            subTitle = serializer.validated_data['subTitle']
            site = serializer.validated_data['site']

            firebase_image_url = ('https://firebasestorage.googleapis.com/v0/b/aelit-dev.appspot.com/o/products'
                                  '%2F6q02G3ifjqoeftrdjJvM%2Fmain?alt=media&token=015ae3e4-d9d6-4cb5-9e36-9ccd3c4c9623')
            generated_image = serializer.save(image_url=firebase_image_url)

            return Response({"status": 200, "url": generated_image.image_url}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
