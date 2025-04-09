from Card import Card
from CleanCard import CleanCard
import filefun
from pandas import DataFrame
import pandas as pd


class Deck(DataFrame):
    # Static variable
    #scryfallDataStaticEnum = Enumerable(filefun.openJSON("ScryfallApiData.json"))
    scryfallDataStatic = filefun.openJSON("MTGsorter\ScryfallApiData.json")

    def __init__(self, *args):
        super().__init__(*args)


    def CreatePrintObj(self):
        """
        Method to print list obj in order to have easier prints

        Args:
            Self. Deck obj that contains the names.
        Returns:
            List obj that contains names of given Card objs
        """
        nameList = []
        for each in self.values():
            nameList.append(each.getName())
            
        return nameList
    
    def createMachineLearningCard(data):
        """
        Creates ML ready pd.Dataframe object.

        Args:
            Data as list
        Returns:
            pd.Dataframe that contains ML ready data
        """
        cardDf: DataFrame = {
                'name': [],
                'amount': [],
                'typeLine': [],
                'oracleText': [],
                'cmc': [],
                'colorIdentity':[],
                'defence':[],
                'keywords':[],
                'loyalty':[],
                'power':[],
                'toughness':[],
        }
        cardDf = pd.DataFrame(cardDf)

        for line in data:
            if line != None:
                # Fill a Card
                a = Card.fillCard(line, ScryData=Deck.scryfallDataStatic)
                a = CleanCard.CreateCleanCard(a)

                newRow:DataFrame = {
                            'name': a.getName(),
                            'amount': a.getAmount(),
                            'typeLine': a.getTypeLine(),
                            'oracleText':a.getOracleText(),
                            'cmc': a.getCmc(),
                            'colorIdentity': a.getColorIdentity(),
                            'defence': a.getDefence(),
                            'keywords': a.getKeywords(),
                            'loyalty': a.getLoyalty(),
                            'power': a.getPower(),
                            'toughness': a.getToughness(),
                    }
                newRow = pd.DataFrame([newRow])
                cardDf = pd.concat([cardDf, newRow], ignore_index=True)
            else:
                continue
        return cardDf




    def createCards(data, isClean=False):
        """
        Creates Card objects by line basis according to given arg.

        Args:
            data (str): given data to be MTG Deck as string or as a list.
            isClean (Bool): If arg "isClean" is True the deck will be returned as pd.Dataframe with every card written as row.

        Returns
            Deck object, that has inherited pd.Dataframe
        """
        # check input type
        if isinstance(data, str):
            # Split by line
            data = data.splitlines()

            # Create dict to hold Deck
            cardStash:Deck = {}
            cleanCardStash:DataFrame = {
                'name': [],
                'amount': [],
                'typeLine': [],
                'oracleText': [],
                'cmc': [],
                'colorIdentity':[],
                'colors': [],
                'defence':[],
                'keywords':[],
                'loyalty':[],
                'manaCost':[],
                'power':[],
                'toughness':[],
                'PTCR':[],
            }

            ## Loop throught data
            for i in data:
                if i != None:
                    # Fill a Card
                    if isClean is False:
                        a = Card.fillCard(i, ScryData=Deck.scryfallDataStatic)
                        # Add to cardStash Dict with loop counter as unique Key and card as value
                        if a != None:
                            cardStash[a.getName()] = a
                        else:
                            continue
                    else:
                        a = Card.fillCard(i, ScryData=Deck.scryfallDataStatic)
                        a = CleanCard.CreateCleanCard(a)
                        name, amount, typeLine, oracleText, cmc, colorIdentity, colors, defence, keywords, loyalty, manaCost, power, toughness, PTCR = a.getName(), a.getAmount(), a.getTypeLine(), a.getOracleText(), a.getCmc(), a.getColorIdentity(), a.getColors(), a.getDefence(), a.getKeywords(), a.getLoyalty, a.getManaCost(), a.getPower(), a.getToughness(), a.getPTCR()
                        cleanCardStash.add(name, amount, typeLine, oracleText, cmc, colorIdentity, colors, defence, keywords, loyalty, manaCost, power, toughness, PTCR)

                        # This return is for cleanCardStash, that is a dataframe, not a dict.
                
            if isClean == True:
                return cleanCardStash
            else:
                return cardStash
        
        elif isinstance(data, list):
            # Create dict to hold Cards
            cardStash:Deck = {}
            ## Loop throught data
            for i in data:
                if i != None:
                    # Fill a Card
                    if isClean is False:
                        a = Card.fillCard(i, ScryData=Deck.scryfallDataStatic)
                        # Add to cardStash Dict with loop counter as unique Key and card as value
                        if a != None:
                            cardStash[a.getName()] = a
                        else:
                            continue
                    else:
                        a = Card.fillCard(i, ScryData=Deck.scryfallDataStatic)
                        a = CleanCard.CreateCleanCard(a)
                        name, amount, typeLine, oracleText, cmc, colorIdentity, colors, defence, keywords, loyalty, manaCost, power, toughness, PTCR = a.getName(), a.getAmount(), a.getTypeLine(), a.getOracleText(), a.getCmc(), a.getColorIdentity(), a.getColors(), a.getDefence(), a.getKeywords(), a.getLoyalty, a.getManaCost(), a.getPower(), a.getToughness(), a.getPTCR()
                        cleanCardStash.add(name, amount, typeLine, oracleText, cmc, colorIdentity, colors, defence, keywords, loyalty, manaCost, power, toughness, PTCR)

                        # This return is for cleanCardStash, that is a dataframe, not a dict.

                
            if isClean == True:
                return cleanCardStash
            else:
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
        cards:Deck = {}
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
            Cards Obj that contains card names
        """
        nameList:Deck = {}
        for each in self.values():
            nameList.update({each.getName(): each.getName()})

        return nameList
    
    def createManaCurve(self):
        """
        Function to create manacurve of the deck

        Args:
            None
        Returns list of every CMC
        """
        # Create list to hold cmc
        cmcList = []
        # fetch all cmc of cards
        for each in self.values():
            if each.getTypeLine() != "Land":
                cmcList.append(int(each.getCmc()))

        # return sorted list
        return cmcList
    
    def getPermanents(self):
        """
        Function to fetch all permanents from deck

        Args:
            Deck
        Return
            Cards Obj that contains all permanents
        """
        # Create container for cards
        permanentList:Deck = {}
        # Loop trough given deck to find all permanents
        for each in self.values():
            # All cards except Instants and Sorveries are permanents
            if each.getTypeLine() != "Instant" and each.getTypeLine() != "Sorcery":
                permanentList.update({each.getName(): each})

        return permanentList
    
    def getInstantsAndSorceries(self):
        """
        Function to fetch all Instants and Sorceries from deck

        Args:
            Deck
        Return
            Cards Obj that contains all Instant and Sorceries
        """
        # Create container for cards
        spellList:Deck = {}
        # Loop trough given deck to find all permanents
        for each in self.values():
            # All cards except Instants and Sorveries are permanents
            if each.getTypeLine() == "Instant" or each.getTypeLine() == "Sorcery":
                spellList.update({each.getName(): each})

        return spellList
    
    # def getCardTypeDist(self):
    #     """
    #     Function to get 
    #     """