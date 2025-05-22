from django.urls import path
from .views import ArtList, ArtDet

urlpatterns=[
	path('',ArtList.as_view(),name="lista"),
	path("<slug:slug>",ArtDet.as_view(),name="detalle"),
]