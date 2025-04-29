from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Pokemon, PokemonAbility, Ability, CombatStats, PokemonInformation, AdditionalInformation, DamageInfo
from . import serializers 
from drf_yasg.utils import swagger_auto_schema

class RootView(APIView):
    '''
        Returns URLs for the endpoints of
        our API.
    '''
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({
            'pokemons' : reverse('api:pokemons-endpoint', request = request),
            'combat' : reverse('api:combat-stats', request = request),
            'ability' : reverse('api:ability-endpoint', request = request)
        })
    


class PokemonView(ListAPIView):
    '''
        Lists all of the pokemons available in the
        database,
        requires the user to be authenticated.
    '''
    queryset = Pokemon.objects.all()
    serializer_class = serializers.PokemonSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(responses = {200 : serializers.PokemonSerializer})
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class PokemonDetailedView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(responses = {200: serializers.DetailedPokemonSerializer})
    def get(self, request, pokemon_name: str):
        try:
            pokemon = Pokemon.objects.filter(name = pokemon_name)
        except Pokemon.DoesNotExist as ex:
            raise ex('Make sure to pass a correct pokemon name.')
        serializer = serializers.DetailedPokemonSerializer(data = pokemon, many = True, 
                                               context = {'request' : request})
        serializer.is_valid()
        return Response(serializer.data)

        
class AbilityView(ListAPIView):
    queryset = Ability.objects.all()
    serializer_class = serializers.AbilitySerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(responses = {200: serializers.AbilitySerializer})
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class PokemonAbilityView(APIView):
    '''
        Returns the ability resources of a 
        certain pokemon.
    '''
    @swagger_auto_schema(response = {200: serializers.PokemonAbilitySerializer})
    def get(self, request, pokemon_name: str):
        try:
            prefetched_data = PokemonAbility.objects.prefetch_related('pokemon').filter(pokemon__name = pokemon_name)
            finalized_abilities = prefetched_data.prefetch_related('ability')
        except PokemonAbility.DoesNotExist as ex:
            raise ex('Make sure to pass a correct pokemon name.')
        
        serializer = serializers.PokemonAbilitySerializer(data = finalized_abilities, many = True)
        serializer.is_valid()
        return Response(serializer.data)

class DamageInfoView(ListAPIView):
    queryset = DamageInfo.objects.all()
    serializer_class = serializers.DetailedDamageInformation
    permission_classes = [AllowAny]

    @swagger_auto_schema(responses = {200: serializers.DetailedDamageInformation})
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class DetailedDamageInfo(RetrieveAPIView):
    queryset = DamageInfo.objects.all()
    serializer_class = serializers.DetailedDamageInformation
    permission_classes = [AllowAny]
    lookup_field = 'pokemon_name'

    @swagger_auto_schema(responses = {200: serializers.DetailedDamageInformation})
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class MainInfoView(ListAPIView):
    queryset = PokemonInformation.objects.all()
    serializer_class = serializers.DetailedInformationSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(responses = {200: serializers.DetailedInformationSerializer})
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class MainInfoDetailed(RetrieveAPIView):
    queryset = PokemonInformation.objects.all()
    serializer_class = serializers.DetailedInformationSerializer
    permission_classes = [AllowAny]
    lookup_field = 'name'

    @swagger_auto_schema(responses = {200: serializers.DetailedInformationSerializer})
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class AddInfoView(ListAPIView):
    queryset = AdditionalInformation.objects.all()
    serializer_class = serializers.DetailedAdditionalInformation
    permission_classes = [AllowAny]

    @swagger_auto_schema(responses = {200: serializers.DetailedAdditionalInformation})
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class AddInfoDetailed(RetrieveAPIView):
    queryset = AdditionalInformation.objects.all()
    serializer_class = serializers.DetailedAdditionalInformation
    permission_classes = [AllowAny]
    lookup_field = 'name'

    @swagger_auto_schema(responses = {200: serializers.DetailedAdditionalInformation})
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class CombatStatsView(ListAPIView):
    queryset = CombatStats.objects.all() 
    serializer_class = serializers.CombatStatsSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(responses = {200: serializers.CombatStatsSerializer})
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class CombatStatsDetailedView(APIView):
    '''
        Allows the user to view detailed combat information
        about a given pokemon.
    '''
    permission_classes = [AllowAny]

    @swagger_auto_schema(responses = {200: serializers.CombatStatsDetailedSerializer})
    def get(self, request, name: str):
        try:
            combat_stats = CombatStats.objects.get(pokemon_name = name)
        except CombatStats.DoesNotExist as ex:
            raise ex('Make sure to pass a correct pokemon name.')
        serializer = serializers.CombatStatsDetailedSerializer(combat_stats, context = {'request' : request})
        return Response({'pokemon' : serializer.data})
        