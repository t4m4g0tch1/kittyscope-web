from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("stats/extensions", views.extensions, name="extensions"),
    path("stats/size-top", views.size_top, name="size-top"),
    path("stats/images-top", views.images_top, name="images-top"),
    path("stats/docs-top", views.docs_top, name="docs-top"),
    path("files/<int:file_id>", views.info, name="info"),
    path("folder", views.analyze_folder, name="folder"),
]
