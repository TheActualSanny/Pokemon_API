from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import Pokemon, PokemonAbility, Ability, CombatStats
from .serializers import PokemonSerializer, AbilitySerializer, PokemonAbilitySerializer, CombatStatsSerializer, CombatStatsDetailedSerializer, DetailedPokemonSerializer

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
    serializer_class = PokemonSerializer
    permission_classes = [AllowAny]

class PokemonDetailedView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, pokemon_name: str):
        try:
            pokemon = Pokemon.objects.filter(name = pokemon_name).prefetch_related('combat_info')
        except Pokemon.DoesNotExist as ex:
            raise ex('Make sure to pass a correct pokemon name.')
        serializer = DetailedPokemonSerializer(data = pokemon, many = True, 
                                               context = {'request' : request})
        serializer.is_valid()
        return Response(serializer.data)

        
class AbilityView(ListAPIView):
    queryset = Ability.objects.all()
    serializer_class = AbilitySerializer
    permission_classes = [AllowAny]

class PokemonAbilityView(APIView):
    '''
        Returns the ability resources of a 
        certain pokemon.
    '''
    def get(self, request, pokemon_name: str):
        try:
            prefetched_data = PokemonAbility.objects.prefetch_related('pokemon').filter(pokemon__name = pokemon_name)
            finalized_abilities = prefetched_data.prefetch_related('ability')
        except PokemonAbility.DoesNotExist as ex:
            raise ex('Make sure to pass a correct pokemon name.')
        
        serializer = PokemonAbilitySerializer(data = finalized_abilities, many = True)
        serializer.is_valid()
        return Response(serializer.data)


class CombatStatsView(ListAPIView):
    queryset = CombatStats.objects.all() 
    serializer_class = CombatStatsSerializer
    permission_classes = [AllowAny]

class CombatStatsDetailedView(APIView):
    '''
        Allows the user to view detailed combat information
        about a given pokemon.
    '''
    permission_classes = [AllowAny]

    def get(self, request, pokemon_name: str):
        try:
            combat_stats = CombatStats.objects.get(pokemon_name = pokemon_name)
        except CombatStats.DoesNotExist as ex:
            raise ex('Make sure to pass a correct pokemon name.')
        serializer = CombatStatsDetailedSerializer(combat_stats)
        return Response({'pokemon' : serializer.data})
        