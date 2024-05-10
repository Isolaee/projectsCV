from Card import Card
import filefun
#from py_linq import Enumerable

class Cards(dict):
    # Static variable
    #scryfallDataStaticEnum = Enumerable(filefun.openJSON("ScryfallApiData.json"))
    scryfallDataStatic = filefun.openJSON("ScryfallApiData.json")

    def __init__(self, *args):
        super().__init__(*args)

    def CreatePrintObj(self):
        """
        Method to print list obj in order to have easier prints

        Args:
            Self. Cards obj that contains the names.
        Returns:
            List obj that contains names of given Card objs
        """
        nameList = []
        for each in self.values():
            nameList.append(each.getName())
            
        return nameList

    def createCards(data):
        """
        Creates Card objects by line basis according to given arg.

        Args:
            data (str): given data to be MTG cards as string.

        Returns
            Cards object, that has inherited dict
        """
        # Split by line
        data = data.splitlines()

        # Create dict to hold Cards
        cardStash:Cards = {}

        ## Loop throught data
        for i in data:
            if i != None:
                # Fill a Card
                a = Card.fillCard(i, ScryData=Cards.scryfallDataStatic)
                # Add to cardStash Dict with loop counter as unique Key and card as value
                if a != None:
                    cardStash[a.getName()] = a
                else:
                    continue
            
        return cardStash
    
    # Function to fetch all cards from deck with same typeline
    def getSameTypeLines(self, type):
        """
        Fetches all cards with suitable typeline

        Args:
            type: Given type search parameter.
        
        Returns:
            Cards Object that contains all cards that match.
        """
        cards:Cards = {}
        for each in self.values():
            if type in each.getTypeLine():
                cards.update({each.getName(): each}) ### Change 2

        return cards
    
    def getAllCardNames(self):
        """
        Function to get every cardname in Cards obj and return those.

        Args:
            None
        Returns:
            Str that contains ever cardname in Card obj
        """
        nameList:Cards = {}
        for each in self.values():
            nameList.update({each.getName(): each.getName()})

        return nameList