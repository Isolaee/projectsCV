import re

class Card:
    def __init__(self,
                 #Print Fields
                 artist:str = "Chris Rush",
                 # Gameplay Fields
                 name:str = "R. Garfield",
                 amount:int = 0,
                 scryfallId:int = 0,
                 typeLine:str = "Richard Garfield, Ph.D.",
                 oracleText:str = "You win the game. Period.",
                 layout:str = "layout",
                 allParts:str = "allparts",
                 cardFaces:str = "cardfaces",
                 cmc:int = "cmc",
                 colorIdentity:str = "colorIdentity",
                 colorIndicator:str = "ColorIndicator",
                 colors:str = "colors",
                 defence:int = "defence",
                 edhRecRank:int = "edhRecRank",
                 handModifier:str = "handModifier",
                 keywords:str = "keywords",
                 legalities:str = "legalities",
                 lifeModifiers:str = "lifeModifiers",
                 loyalty:int = "loyalty",
                 manaCost:int = "manaCost",
                 power:int = "power",
                 toughness:int = "Toughness",
                 ):
        
        self._name = name
        self._amount = amount
        self._scryfallId = scryfallId
        self._layout = layout
        self._allParts = allParts
        self._cardFaces = cardFaces
        self._cmc = cmc
        self._colorIdentity = colorIdentity
        self._colorIndicator = colorIndicator
        self._colors = colors
        self._defence = defence
        self._edhRecRank = edhRecRank
        self._handModifer = handModifier
        self._keywords = keywords
        self._legalities = legalities
        self._lifeModifier = lifeModifiers
        self._loyalty = loyalty
        self._manaCost = manaCost
        self._oracleText = oracleText
        self._power = power
        self._toughness = toughness
        self._typeLine = typeLine
        self._artist = artist

    # Getters
    def getName(self):
        if self._name is not None:
            return self._name
        else:
            return "Unknown"
    def getAmount(self):
        if int(self._amount) > 0:
            return int(self._amount)
        else:
            return 0
    def getScryfallId(self):
        return self._scryfallId
    def getLayout(self):
        return self._layout
    def getAllParts(self):
        return self._allParts
    def getCardFaces(self):
        return self._cardFaces
    def getCmc(self):
        return self._cmc
    def getColorIdentity(self):
        return self._colorIdentity
    def getColorIndicator(self):
        return self._colorIndicator
    def getColors(self):
        return self._colors
    def getDefence(self):
        if self._defence is type(int):
            return int(self._defence)
        else:
            return 0
    def getEdhRecRank(self):
        return self._edhRecRank
    def getHandModifier(self):
        return self._handModifer
    def getKeywords(self):
        if not self._keywords:
            return "No keywords"
        else:
            return self._keywords
    def getLegalities(self):
        return self._legalities
    def getLifeModifier(self):
        return self._lifeModifier
    def getLoyalty(self):
        if not self._loyalty:
            return 0
        else:
            return self._loyalty
    def getManaCost(self):
        return self._manaCost
    
    def getOracleText(self):
        return str(self._oracleText)

    def getPower(self):
        if not self._power:
            return 0
        else:
            return self._power
    def getToughness(self):
        if not self._toughness:
            return 0
        else:
            return self._toughness
        
    def getTypeLine(self):
        return self._typeLine
    def getArtist(self):
        return self._artist

    ### Methods

    def fillCard(DeckData, ScryData):
        """
        Creates single card object according to given string.
        
        Args:
            data (str): Single string that contains number of same cards (as if amount) and cardname.

        Returns:
            Single Card object that contains all of the data fetched from Scryfall with that name.
        """

        # Regtex search criteria.
        regexString = "(?P<amount>\d+)\s?(?P<name>(?:[a-zA-Z']+(?:,\s)?|(?:\s))+)"

        # Regex searches.
        try:
            regexResult = re.search(regexString, DeckData)
        except:
            print("Regex parse failed")

        if regexResult == None:
            return

        # Removing empty chars from regex string
        regexResultAmount = regexResult.group("amount").strip()
        regexResultName = regexResult.group("name").strip()

        ## finding card data from Scyfall data
        # Iterate through the entire dictionary (With this approuch you can get values with .get(""))
        for item in ScryData:
            if "name" in item and regexResultName in item["name"]:
                # Found a match, add the entire entry to the result
                matching_entry = item
                break

        cardObj = Card(
                artist = matching_entry.get("artist"), # Artist
                name = matching_entry.get("name"), # Name
                amount = regexResultAmount, # Amount
                scryfallId = matching_entry.get("id"), # ScryfallId
                typeLine = matching_entry.get("type_line"), # Typeline
                oracleText = matching_entry.get("oracle_text"), # OracleText
                layout = matching_entry.get("layout"), # Layout
                allParts = matching_entry.get("all_parts"),
                cardFaces = matching_entry.get("card_faces"),
                cmc = matching_entry.get("cmc"), # CMC
                colorIdentity = matching_entry.get("color_identity"), # ColorIdentity
                colorIndicator = matching_entry.get("color_indicator"), # colorIndicator
                colors = matching_entry.get("colors"), # Colors
                defence = matching_entry.get("defence"), # Defence
                edhRecRank = matching_entry.get("edhrec_rank"), # EdhRecRank
                handModifier = matching_entry.get("hand_modifier"), # HandModifier
                keywords = matching_entry.get("keywords"), # Keywords
                legalities = matching_entry.get("legalities"), # Legalities
                lifeModifiers = matching_entry.get("life_modifier"), # LigeModifier
                loyalty = matching_entry.get("loyalty"), # Loyalty
                manaCost = matching_entry.get("mana_cost"), # Mana cost
                power = matching_entry.get("power"), # Power
                toughness = matching_entry.get("toughness") # Toughness
                )
        
        return cardObj

    def getFeatures(self):
        print(self.getName(), ", Amount: ", self.getAmount(), ", Colors: ", self.getColors(), ", Oracle Text: ", self.getOracleText(), "Power/Toughness: ", self.getPower(), "/", self.getToughness())
