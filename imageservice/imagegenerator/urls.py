from django.urls import path
from .views import GenerateImageView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    # path('generate/', GenerateImageView.as_view(), name='generate_image'),
    path('generate/', csrf_exempt(GenerateImageView.as_view()), name='generate-image-view'),

]
