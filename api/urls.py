from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.RootView.as_view(), name = 'root-endpoint'),
    path('pokemons/', views.PokemonView.as_view(), name = 'pokemons-endpoint'),
    path('pokemons/<str:pokemon_name>/', views.PokemonDetailedView.as_view(), name = 'pokemon-detailed'),
    path('ability/', views.AbilityView.as_view(), name = 'ability-endpoint'),
    path('ability/<str:pokemon_name>/', views.PokemonAbilityView.as_view(), name = 'pokemonability-endpoint'),
    path('combat/', views.CombatStatsView.as_view(), name = 'combat-stats'),
    path('combat/<str:name>/', views.CombatStatsDetailedView.as_view(), name = 'combat-endpoint'),
    path('information/', views.MainInfoView.as_view(), name = 'info-endpoint'),
    path('additional/', views.AddInfoView.as_view(), name = 'additional-information-endpoint'),
    path('damage/', views.DamageInfoView.as_view(), name = 'damage-info'),
    path('additional/<str:name>/', views.AddInfoDetailed.as_view(), name = 'additional-detailed-endpoint'),
    path('information/<str:name>/', views.MainInfoDetailed.as_view(), name = 'main-detailed-endpoint'),
    path('damage/<str:pokemon_name>/', views.DetailedDamageInfo.as_view(), name = 'detailed-damage')
]