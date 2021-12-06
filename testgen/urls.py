from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('gen1d', views.gen1d, name="gen1d"),
    path('gen2d', views.gen2d, name="gen2d"),
    path('bigint', views.bigint, name="bigint"),
    path('tree', views.tree, name="tree"),
    path('graph', views.graph, name="graph"),
    path('string', views.string, name="string"),
]
