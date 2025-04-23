from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import Pokemon, PokemonAbility, Ability
from .serializers import PokemonSerializer, AbilitySerializer, PokemonAbilitySerializer

class RootView(APIView):
    '''
        Returns URLs for the endpoints of
        our API.
    '''
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({
            'pokemons' : reverse('pokemons-endpoint', request = request)
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


class AbilityView(ListAPIView):
    queryset = Ability.objects.all()
    serializer_class = AbilitySerializer
    permission_classes = [AllowAny]

class PokemonAbilityView(APIView):
    '''
        Returns the ability resources of a 
        certain pokemon.
    '''
    def get(self, request, pokemon_name):
        try:
            prefetched_data = PokemonAbility.objects.prefetch_related('pokemon').filter(pokemon__name = pokemon_name)
            finalized_abilities = prefetched_data.prefetch_related('ability')
        except PokemonAbility.DoesNotExist as ex:
            raise ex('Make sure to pass a correct pokemon name.')
        
        serializer = PokemonAbilitySerializer(data = finalized_abilities, many = True)
        serializer.is_valid()
        return Response(serializer.data)
        