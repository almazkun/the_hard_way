from django.urls import path


from .views import greeting, game

urlpatterns = [
    path("", greeting, name="home"),
    path("game", game, name="game"),
]
