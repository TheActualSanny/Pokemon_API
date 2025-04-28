from rest_framework import serializers
from .models import Pokemon, Ability, PokemonAbility, CombatStats, PokemonInformation, AdditionalInformation, DamageInfo

class PokemonSerializer(serializers.ModelSerializer):
    '''
        Lists basic info about the pokemon.
        The logic to list detailed information about the
        relations of the Pokemon table is written in the DetailedPokemonSerializer.
    '''
    class Meta:
        model = Pokemon
        fields = ['name', 'japanese_name', 'pokedex_number']



class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        fields = ['id', 'ability_name']

class PokemonAbilitySerializer(serializers.ModelSerializer):
    ability = AbilitySerializer()
    class Meta:
        model = PokemonAbility
        fields = ['ability']


class CombatStatsDetailedSerializer(serializers.ModelSerializer):
    '''
        Serializes the combat stats as a resource.
    '''
    class Meta:
        model = CombatStats
        exclude = ['pokemon_name']


class DetailedInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonInformation
        fields = '__all__'


class DetailedAdditionalInformation(serializers.ModelSerializer):
    class Meta:
        model = AdditionalInformation
        fields = '__all__'


class DetailedDamageInformation(serializers.ModelSerializer):
    class Meta:
        model = DamageInfo
        fields = '__all__'

class CombatStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CombatStats
        fields = '__all__'


class DetailedPokemonSerializer(serializers.HyperlinkedModelSerializer):
    '''
        Contains the main information about the pokemons.
        This resource will contain the URLs to get the neccessary data
        from the abilities.
    '''
    combat_info = CombatStatsDetailedSerializer()
    main_information = DetailedInformationSerializer()
    additional_information = DetailedAdditionalInformation()
    damage_information = DetailedDamageInformation()
    
    class Meta:
        model = Pokemon
        fields = ['name', 'japanese_name', 'pokedex_number',
                  'combat_info', 'main_information', 'additional_information',
                  'damage_information']
        
