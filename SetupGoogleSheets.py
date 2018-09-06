from oauth2client.service_account import ServiceAccountCredentials
import gspread

class SetupGoogleSheets:

    def __init__(self):

        self.scope = ['https://spreadsheets.google.com/feeds',
                      'https://www.googleapis.com/auth/drive']

        # Connection to spread sheet stored as json - keep it secret, keep it safe
        self.creds = ServiceAccountCredentials.from_json_keyfile_name('PokemonDandD-9d05328feefa.json', self.scope)
        self.client = gspread.authorize(self.creds)
        self.

        self.google_sheet = self.client.open('Pokemon D & D')
        self.num_of_sheets = self.google_sheet.worksheets()

    def create_general_sheet(self):

        """
        
        This method creates the general stat sheet where all players can 
        see the players starting pokemon.
        :return: 
        """

    def create_player_sheet(self, name):

        """
        
        This method sets up the sheet to start the pokemon adventure for each individual player
        :param name: Name of the player you wish to create
        :return: None in python, should see a successful page creation in 
        google sheets
        """

    def
