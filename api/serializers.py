from rest_framework import serializers
from .models import Pokemon, Ability, PokemonAbility

class PokemonSerializer(serializers.ModelSerializer):
    '''
        Lists basic info about the pokemon.
        The logic to list detailed information about the
        relations of the Pokemon table is written in the DetailedPokemonSerializer.
    '''
    class Meta:
        model = Pokemon
        fields = ['name', 'japanese_name', 'pokedex_number']


class DetailedPokemonSerializer(serializers.ModelSerializer):
    '''
        Contains the main information about the pokemons.
        This resource will contain the URLs to get the neccessary data
        from the abilities.
    '''
    class Meta:
        model = Pokemon
        fields = []

class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        fields = ['id', 'ability_name']

class PokemonAbilitySerializer(serializers.ModelSerializer):
    ability = AbilitySerializer()
    class Meta:
        model = PokemonAbility
        fields = ['ability']