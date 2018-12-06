import gspread
import pokebase as pb
from random import randint
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSpreadSheet:

    def __init__(self):
        
        """ This was for fun, if I had to make a commit for work. I need to make base classes to update players. """
        
        """Make sure to enable google api from the google cloud drive!"""

        self.scope      = ['https://spreadsheets.google.com/feeds',
                        'https://www.googleapis.com/auth/drive']

        # Connection to spread sheet stored as json - keep it secret, keep it safe
        self.creds      = ServiceAccountCredentials.from_json_keyfile_name('PokemonDandD-9d05328feefa.json', self.scope)
        self.client     = gspread.authorize(self.creds)

        self.temp_sheet         = self.client.open('Pokemon D & D')
        self.sheet              = self.temp_sheet.get_worksheet(0)
        self.alex_statsheet     = self.temp_sheet.get_worksheet(1)
        self.brenna_statsheet   = self.temp_sheet.get_worksheet(2)
        self.bri_statsheet      = self.temp_sheet.get_worksheet(3)
        self.morgan_statsheet   = self.temp_sheet.get_worksheet(4)
        self.shana_statsheet    = self.temp_sheet.get_worksheet(5)

        # The stats
        self.types      = []
        self.stat_names = []
        self.stats      = []
        self.abilities  = []

    def get_Alex_Pokemon_Information(self, json_data):

        """
        :param json_data:  json data from the google spread sheets
        :return: 
        """

        # Get pokemon's current level from sheet for stat calculations
        self.level = int(self.alex_statsheet.cell(2, 4).value)

        # Get Alex's Lead Pokemon, Need Type, Abilities, Base Stats
        Alex_Pokemon = json_data[0]["Active Pokemon"].lower()
        Alex_Front = pb.pokemon(Alex_Pokemon)

        # Using the api PROPERLY now !! I tried to access like a json document which was a rookie mistake.
        pokemon_type            = str(Alex_Front.types[0].type)
        Alex_base_stat_hp       = Alex_Front.stats[5].base_stat
        Alex_base_stat_atk      = Alex_Front.stats[4].base_stat
        Alex_base_stat_def      = Alex_Front.stats[3].base_stat
        Alex_base_stat_sp_atk   = Alex_Front.stats[2].base_stat
        Alex_base_stat_sp_def   = Alex_Front.stats[1].base_stat
        Alex_base_stat_speed    = Alex_Front.stats[0].base_stat


        # calculate those statistics based on level, STAT!
        hp, atk, defense, sp_atk, sp_def, speed = self._calculate_pokemon_stats_by_level(Alex_base_stat_hp,
                                               Alex_base_stat_atk,
                                               Alex_base_stat_def,
                                               Alex_base_stat_sp_atk,
                                               Alex_base_stat_sp_def,
                                               Alex_base_stat_speed,
                                               level = self.level)

        pokemon_abilities  = Alex_Front.abilities
        pokemon_ability    = (str(pokemon_abilities[0].ability.name))

        # Update stats in the google speadsheet.
        self.alex_statsheet.update_cell(row=2, col=2, value=pokemon_ability)
        self.alex_statsheet.update_cell(row=2, col=3, value=pokemon_type)
        self.alex_statsheet.update_cell(row=2, col=5, value=hp)
        self.alex_statsheet.update_cell(row=2, col=6, value=atk)
        self.alex_statsheet.update_cell(row=2, col=7, value=defense)
        self.alex_statsheet.update_cell(row=2, col=8, value=sp_atk)
        self.alex_statsheet.update_cell(row=2, col=9, value=sp_def)
        self.alex_statsheet.update_cell(row=2, col=10, value=speed)

        return [hp, atk, defense, sp_atk, sp_def, speed, pokemon_type, pokemon_ability]

    def get_Brenna_Pokemon_Information(self, json_data):


        """
        :param json_data:  json data from the google spread sheets
        :return: 
        """

        self.level      = int(self.brenna_statsheet.cell(2, 4).value)

        # Get Brenna's Lead Pokemon, Need Type, Abilities, Base Stats
        Brenna_Pokemon    = json_data[1]["Active Pokemon"].lower()
        Brenna_Front      = pb.pokemon(Brenna_Pokemon)

        #Brenna Stats - This call gets the stats from the Pokebase API.
        pokemon_type            = str(Brenna_Front.types[0].type)
        Brenna_base_stat_hp       = Brenna_Front.stats[5].base_stat
        Brenna_base_stat_atk      = Brenna_Front.stats[4].base_stat
        Brenna_base_stat_def      = Brenna_Front.stats[3].base_stat
        Brenna_base_stat_sp_atk   = Brenna_Front.stats[2].base_stat
        Brenna_base_stat_sp_def   = Brenna_Front.stats[1].base_stat
        Brenna_base_stat_speed    = Brenna_Front.stats[0].base_stat

        hp, atk, defense, sp_atk, sp_def, speed = self._calculate_pokemon_stats_by_level(Brenna_base_stat_hp,
                                               Brenna_base_stat_atk,
                                               Brenna_base_stat_def,
                                               Brenna_base_stat_sp_atk,
                                               Brenna_base_stat_sp_def,
                                               Brenna_base_stat_speed,
                                               level = self.level)

        pokemon_abilities  = Brenna_Front.abilities
        pokemon_ability    = (str(pokemon_abilities[0].ability.name))

        # Update stats of lead pokemon.
        self.brenna_statsheet.update_cell(row=2, col=2, value=pokemon_ability)
        self.brenna_statsheet.update_cell(row=2, col=3, value=pokemon_type)
        self.brenna_statsheet.update_cell(row=2, col=5, value=hp)
        self.brenna_statsheet.update_cell(row=2, col=6, value=atk)
        self.brenna_statsheet.update_cell(row=2, col=7, value=defense)
        self.brenna_statsheet.update_cell(row=2, col=8, value=sp_atk)
        self.brenna_statsheet.update_cell(row=2, col=9, value=sp_def)
        self.brenna_statsheet.update_cell(row=2, col=10, value=speed)

        return [hp, atk, defense, sp_atk, sp_def, speed, pokemon_type, pokemon_ability]
    
    def get_Bri_Pokemon_Information(self, json_data):


        """
        :param json_data:  json data from the google spread sheets
        d:return: 
        """

        self.level      = int(self.bri_statsheet.cell(2, 4).value)

        # Get Bri's Lead Pokemon, Need Type, Abilities, Base Stats
        Bri_Pokemon    = json_data[2]["Active Pokemon"].lower()
        Bri_Front      = pb.pokemon(Bri_Pokemon)

        #Bri Stats - This call gets the stats from the Pokebase API.
        pokemon_type            = str(Bri_Front.types[0].type)
        Bri_base_stat_hp       = Bri_Front.stats[5].base_stat
        Bri_base_stat_atk      = Bri_Front.stats[4].base_stat
        Bri_base_stat_def      = Bri_Front.stats[3].base_stat
        Bri_base_stat_sp_atk   = Bri_Front.stats[2].base_stat
        Bri_base_stat_sp_def   = Bri_Front.stats[1].base_stat
        Bri_base_stat_speed    = Bri_Front.stats[0].base_stat

        hp, atk, defense, sp_atk, sp_def, speed = self._calculate_pokemon_stats_by_level(Bri_base_stat_hp,
                                               Bri_base_stat_atk,
                                               Bri_base_stat_def,
                                               Bri_base_stat_sp_atk,
                                               Bri_base_stat_sp_def,
                                               Bri_base_stat_speed,
                                               level = self.level)

        pokemon_abilities  = Bri_Front.abilities
        pokemon_ability    = (str(pokemon_abilities[0].ability.name))

        # Update stats of lead pokemon.
        self.bri_statsheet.update_cell(row=2, col=2, value=pokemon_ability)
        self.bri_statsheet.update_cell(row=2, col=3, value=pokemon_type)
        self.bri_statsheet.update_cell(row=2, col=5, value=hp)
        self.bri_statsheet.update_cell(row=2, col=6, value=atk)
        self.bri_statsheet.update_cell(row=2, col=7, value=defense)
        self.bri_statsheet.update_cell(row=2, col=8, value=sp_atk)
        self.bri_statsheet.update_cell(row=2, col=9, value=sp_def)
        self.bri_statsheet.update_cell(row=2, col=10, value=speed)

        return [hp, atk, defense, sp_atk, sp_def, speed, pokemon_type, pokemon_ability]

    def get_Morgan_Pokemon_Information(self, json_data):

        """
        :param json_data:  json data from the google spread sheets
        :return: 
        """

        self.level = int(self.morgan_statsheet.cell(2, 4).value)

        # Get Morgan's Lead Pokemon, Need Type, Abilities, Base Stats
        Morgan_Pokemon = json_data[3]["Active Pokemon"].lower()
        Morgan_Front = pb.pokemon(Morgan_Pokemon)

        # Morgan Stats - This call gets the stats from the Pokebase API.
        pokemon_type = str(Morgan_Front.types[0].type)
        Morgan_base_stat_hp = Morgan_Front.stats[5].base_stat
        Morgan_base_stat_atk = Morgan_Front.stats[4].base_stat
        Morgan_base_stat_def = Morgan_Front.stats[3].base_stat
        Morgan_base_stat_sp_atk = Morgan_Front.stats[2].base_stat
        Morgan_base_stat_sp_def = Morgan_Front.stats[1].base_stat
        Morgan_base_stat_speed = Morgan_Front.stats[0].base_stat

        hp, atk, defense, sp_atk, sp_def, speed = self._calculate_pokemon_stats_by_level(Morgan_base_stat_hp,
                                                                                         Morgan_base_stat_atk,
                                                                                         Morgan_base_stat_def,
                                                                                         Morgan_base_stat_sp_atk,
                                                                                         Morgan_base_stat_sp_def,
                                                                                         Morgan_base_stat_speed,
                                                                                         level=self.level)

        pokemon_abilities = Morgan_Front.abilities
        pokemon_ability = (str(pokemon_abilities[0].ability.name))

        # Update stats of lead pokemon.
        self.morgan_statsheet.update_cell(row=2, col=2, value=pokemon_ability)
        self.morgan_statsheet.update_cell(row=2, col=3, value=pokemon_type)
        self.morgan_statsheet.update_cell(row=2, col=5, value=hp)
        self.morgan_statsheet.update_cell(row=2, col=6, value=atk)
        self.morgan_statsheet.update_cell(row=2, col=7, value=defense)
        self.morgan_statsheet.update_cell(row=2, col=8, value=sp_atk)
        self.morgan_statsheet.update_cell(row=2, col=9, value=sp_def)
        self.morgan_statsheet.update_cell(row=2, col=10, value=speed)

        return [hp, atk, defense, sp_atk, sp_def, speed, pokemon_type, pokemon_ability]

    def get_Shana_Pokemon_Information(self, json_data):

        """
        :param json_data:  json data from the google spread sheets
        :return: 
        """

        self.level = int(self.shana_statsheet.cell(2, 4).value)

        # Get Shana's Lead Pokemon, Need Type, Abilities, Base Stats
        Shana_Pokemon = json_data[4]["Active Pokemon"].lower()
        Shana_Front = pb.pokemon(Shana_Pokemon)

        # Shana Stats - This call gets the stats from the Pokebase API.
        pokemon_type = str(Shana_Front.types[0].type)
        Shana_base_stat_hp = Shana_Front.stats[5].base_stat
        Shana_base_stat_atk = Shana_Front.stats[4].base_stat
        Shana_base_stat_def = Shana_Front.stats[3].base_stat
        Shana_base_stat_sp_atk = Shana_Front.stats[2].base_stat
        Shana_base_stat_sp_def = Shana_Front.stats[1].base_stat
        Shana_base_stat_speed = Shana_Front.stats[0].base_stat

        hp, atk, defense, sp_atk, sp_def, speed = self._calculate_pokemon_stats_by_level(Shana_base_stat_hp,
                                                                                         Shana_base_stat_atk,
                                                                                         Shana_base_stat_def,
                                                                                         Shana_base_stat_sp_atk,
                                                                                         Shana_base_stat_sp_def,
                                                                                         Shana_base_stat_speed,
                                                                                         level=self.level)

        pokemon_abilities = Shana_Front.abilities
        pokemon_ability = (str(pokemon_abilities[0].ability.name))

        # Update stats of lead pokemon.
        self.shana_statsheet.update_cell(row=2, col=2, value=pokemon_ability)
        self.shana_statsheet.update_cell(row=2, col=3, value=pokemon_type)
        self.shana_statsheet.update_cell(row=2, col=5, value=hp)
        self.shana_statsheet.update_cell(row=2, col=6, value=atk)
        self.shana_statsheet.update_cell(row=2, col=7, value=defense)
        self.shana_statsheet.update_cell(row=2, col=8, value=sp_atk)
        self.shana_statsheet.update_cell(row=2, col=9, value=sp_def)
        self.shana_statsheet.update_cell(row=2, col=10, value=speed)

        return [hp, atk, defense, sp_atk, sp_def, speed, pokemon_type, pokemon_ability]

    def _get_jsonized_output(self):
        
        """
        :return:  gets all of the records in the first sheet. 
        """
        return self.sheet.get_all_records()

    def _calculate_pokemon_stats_by_level(self,     hp, attack, defense, sp_atk, sp_def, speed, level):

        """
        private function that calculates all stats for chosen pokemon on the fly.        
        :param hp:  Pokemon base hp
        :param attack: Pokemon base attack
        :param defense: Pokemon base defense
        :param sp_atk:  Pokemon base special attack
        :param sp_def: Pokemon base special defense
        :param speed: Pokemon base speed
        :param level: Pokemon level (Mined from the google sheets)
        :return: 
        """

        # Calculates the pokemons stats based on the base stats and their complicated formulas
        # todo: Create an IV, EV and Nature generator and modify the stats to take this into account.

        level_hp = round((((2 * hp) * level)/(100) + 10 + level))
        level_atk = round((((2 * attack) * level) / (100) + 5))
        level_def = round((((2 * defense) * level) / (100) + 5))
        level_sp_atk = round((((2 * sp_atk) * level) / (100) + 5))
        level_sp_def = round((((2 * sp_def) * level) / (100) + 5))
        level_speed = round((((2 * speed) * level) / (100) + 5))

        return level_hp, level_atk, level_def, level_sp_atk, level_sp_def, level_speed


    #todo: create new class for these "generator" functions
    def _IVGenerator(self):
        raise NotImplementedError

    def _EVCalculator(self):
        raise NotImplementedError

    def _NatureGenerator(self):

        rnjesus = randint(1,25)
        nature = pb.nature(rnjesus)
        print(nature)

    def _Roll_Encounter_Generator(self, route, encounter_table):
        raise NotImplementedError

if __name__ == "__main__":
    GSS = GoogleSpreadSheet()
    json_data = GSS._get_jsonized_output()
    while(1):
        alex_pokemon_data = GSS.get_Alex_Pokemon_Information(json_data)
        brenna_pokemon_data = GSS.get_Brenna_Pokemon_Information(json_data)
        brie_pokemon_data = GSS.get_Bri_Pokemon_Information(json_data)
        morgan_pokemon_data = GSS.get_Morgan_Pokemon_Information(json_data)
        shana_pokemon_data = GSS.get_Shana_Pokemon_Information(json_data)
    # GSS._NatureGenerator()
