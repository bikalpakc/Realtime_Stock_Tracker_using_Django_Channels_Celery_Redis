#Same like urls.py for http/wsgi server

from django.urls import path
from .consumers import StocksConsumer

ws_urlpatterns=[
    path('ws/stocks/', StocksConsumer.as_asgi()),
]