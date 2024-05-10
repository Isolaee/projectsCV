import re
#from py_linq import Enumerable

class Card:
    def __init__(self,
                 #Print Fields
                 artist,
                 # Gameplay Fields
                 name,
                 amount,
                 scryfallId,
                 typeLine,
                 oracleText,
                 layout = "layout",
                 allParts = "allparts",
                 cardFaces = "cardfaces",
                 cmc = "cmc",
                 colorIdentity = "colorIdentity",
                 colorIndicator = "ColorIndicator",
                 colors = "colors",
                 defense = "defence",
                 edhRecRank = "edhRecRank",
                 handModifier = "handModifier",
                 keywords = "keywords",
                 legalities = "legalities",
                 lifeModifiers = "lifeModifiers",
                 loyalty = "loyalty",
                 manaCost = "manaCost",
                 power = "power",
                 toughness = "Toughness",
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
        self._defence = defense
        self._edhRecRank = edhRecRank
        self._handModfier = handModifier
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
        return self._name
    def getAmount(self):
        return self._amount
    def getScryfallId(self):
        return self._scryfallId
    def getlayout(self):
        return self._layout
    def getallParts(self):
        return self._allParts
    def getCardFaces(self):
        return self._cardFaces
    def getCmc(self):
        return self._cmc
    def getcolorIdentity(self):
        return self._colorIdentity
    def getColorIndicator(self):
        return self._colorIndicator
    def getColors(self):
        return self._colors
    def getDefence(self):
        return self._defence
    def getEdhRecRank(self):
        return self._edhRecRank
    def getHandModifier(self):
        return self._handModfier
    def getKeywords(self):
        return self._keywords
    def getLegalities(self):
        return self._legalities
    def getLifeModifier(self):
        return self._lifeModifier
    def getLoyalty(self):
        return self._loyalty
    def getManaCost(self):
        return self._manaCost
    def getOracleText(self):
        return self._oracleText
    def getPower(self):
        return self._power
    def getToughness(self):
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

        # Removing the first empty char from regex string
        regexResultAmount = regexResult.group("amount").lstrip()
        regexResultName = regexResult.group("name").lstrip()

        ## finding card data from Scyfall data
        # Iterate through the entire dictionary (With this approuch you can get values with .get(""))
        for item in ScryData:
            if "name" in item and regexResultName in item["name"]:
                # Found a match, add the entire entry to the result
                matching_entry = item
                break

        cardObj = Card(
                artist = matching_entry.get("artist"), # Artist # Artist
                name = matching_entry.get("name"), # Name
                amount = regexResultAmount, # Amount
                scryfallId = matching_entry.get("scryfallId"), # ScryfallId
                typeLine = matching_entry.get("type_line"), # Typeline
                oracleText = matching_entry.get("oracle_text"), # OracleText
                layout = matching_entry.get("layout"), # Layout
                allParts = matching_entry.get("all_parts"),
                cardFaces = matching_entry.get("card_faces"),
                cmc = matching_entry.get("cmc"), # CMC
                colorIdentity = matching_entry.get("color_identity"), # ColorIdentity
                colorIndicator = matching_entry.get("color_indicator"), # colorIndicator
                colors = matching_entry.get("colors"), # Colors
                defense = matching_entry.get("defence"), # Defence
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
    