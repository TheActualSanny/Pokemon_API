from django.db import models


class PokemonInformation(models.Model):
    '''
        The basic information will be divided in two tables: the pokemon info and the additional info.
    '''
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 90)
    percentage_male = models.FloatField()
    classification = models.CharField(max_length = 200)
    height_meters = models.FloatField(blank = True, null = True)
    weight_kilograms = models.FloatField(blank = True, null = True)
    type1 = models.CharField(max_length = 200)
    type2 = models.CharField(max_length = 200)
    generation = models.CharField(max_length = 200)
    is_legendary = models.BooleanField()

class AdditionalInformation(models.Model):
    '''
        Contains the information that would be redundant in 
        PokemonInformation
    '''
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 90, null = True)
    capture_rate = models.CharField(max_length = 100)
    base_egg_steps = models.IntegerField()
    experience_growth = models.FloatField()
    base_happiness = models.FloatField()

class CombatStats(models.Model):
    '''
        Combat properties on a given pokemon is stored here.
    '''
    id = models.AutoField(primary_key = True)
    pokemon_name = models.CharField(max_length = 90)
    health = models.FloatField()
    attack = models.FloatField()
    defense = models.FloatField()
    speed = models.FloatField()
    special_attack = models.FloatField()
    special_defense = models.FloatField()

class Ability(models.Model):
    '''
        Although there is no additional data on the abilities, such as its
        actual properties, we store the ability names here.
        The relationship will be OneToMany
    '''
    id = models.AutoField(primary_key = True)
    ability_name = models.CharField(max_length = 200)

class PokemonAbility(models.Model):
    '''
        To avoid redundant ability records, we use
        this table.
    '''
    id = models.AutoField(primary_key = True)
    pokemon = models.ForeignKey('api.Pokemon', on_delete = models.CASCADE)
    ability = models.ForeignKey(Ability, on_delete = models.CASCADE)

    

class DamageInfo(models.Model):
    '''
        Damage that the given pokemon takes from a certain 
        class is contained here.
        Currently holds values for 18 different classes.
        The relationship will be OneToOne
    '''
    id = models.AutoField(primary_key = True)
    pokemon_name = models.CharField(max_length = 90)
    against_rock = models.FloatField(null = True)
    against_fairy = models.FloatField(null = True)
    against_fight = models.FloatField(null = True)
    against_fire = models.FloatField(null = True)
    against_flying = models.FloatField(null = True)
    against_ghost = models.FloatField(null = True)
    against_grass = models.FloatField(null = True)
    against_ground = models.FloatField(null = True)
    against_ice = models.FloatField(null = True)
    against_normal = models.FloatField(null = True)
    against_poison = models.FloatField(null = True)
    against_psychic = models.FloatField(null = True)
    against_steel = models.FloatField(null = True)
    against_water = models.FloatField(null = True)
    against_bug = models.FloatField(null = True)
    against_dark = models.FloatField(null = True)
    against_dragon = models.FloatField(null = True)
    against_electric = models.FloatField(null = True)

class Pokemon(models.Model):
    '''
        The base pokemon class. This will contain foreign keys to other tables,
        which contain the main information about a given pokemon
    '''
    name = models.TextField(max_length = 90, primary_key = True)
    japanese_name = models.CharField(max_length = 90)
    pokedex_number = models.IntegerField()
    combat_info = models.ForeignKey(CombatStats, on_delete = models.CASCADE)
    main_information = models.ForeignKey(PokemonInformation, on_delete = models.CASCADE)
    additional_information = models.ForeignKey(AdditionalInformation, on_delete = models.CASCADE)
    damage_information = models.ForeignKey(DamageInfo, on_delete = models.CASCADE)
