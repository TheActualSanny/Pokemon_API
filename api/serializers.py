from rest_framework import serializers
from .models import Pokemon, Ability, PokemonAbility, CombatStats, PokemonInformation, AdditionalInformation, DamageInfo
from rest_framework.reverse import reverse

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
    combat_info = serializers.SerializerMethodField()
    ability_info = serializers.SerializerMethodField()
    main_information = serializers.SerializerMethodField()
    additional_information = serializers.SerializerMethodField()
    damage_information = serializers.SerializerMethodField()
    
    class Meta:
        model = Pokemon
        fields = ['name', 'japanese_name', 'pokedex_number',
                'combat_info', 'ability_info', 'main_information', 
                'additional_information', 'damage_information']
    
    def get_combat_info(self, obj):
        request = self.context.get('request')
        return reverse('api:combat-endpoint', kwargs = {'name' : obj.name}, request = request)
    
    def get_ability_info(self, obj):
        request = self.context.get('request')
        return reverse('api:pokemonability-endpoint', kwargs = {'pokemon_name' : obj.name}, request = request)
    
    def get_additional_information(self, obj):
        request = self.context.get('request')
        return reverse('api:additional-detailed-endpoint', kwargs = {'name' : obj.name},
                       request = request)
    def get_main_information(self, obj):
        request = self.context.get('request')
        return reverse('api:main-detailed-endpoint', kwargs = {'name' : obj.name},
                       request = request)
    def get_damage_information(self, obj):
        request = self.context.get('request')
        return reverse('api:detailed-damage', kwargs = {'pokemon_name' : obj.name}, 
                       request = request)