from django.urls import path
from . import views

urlpatterns = [
    path('', views.RootView.as_view(), name = 'root-endpoint'),
    path('pokemons/', views.PokemonView.as_view(), name = 'pokemons-endpoint'),
    path('ability/', views.AbilityView.as_view(), name = 'ability-endpoint'),
    path('ability/<str:pokemon_name>/', views.PokemonAbilityView.as_view(), name = 'pokemonability-endpoint')
]