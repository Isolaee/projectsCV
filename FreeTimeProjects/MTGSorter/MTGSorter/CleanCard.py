from Card import Card
import Word2Vec as W2V


class CleanCard(Card):
    def __init__(self, name, amount, cmc, colorIdentity, colors, defence, keywords, loyalty, manaCost, oracleText, power, toughness, typeLine):
        
        super().__init__(name=name, amount=amount, cmc=cmc, colorIdentity=colorIdentity, colors=colors, defence=defence, keywords=keywords,loyalty=loyalty, manaCost=manaCost, oracleText=oracleText, power=power, toughness=toughness, typeLine=typeLine)
        # self.PTCR = self.calcPTCR()

    def getPTCR(self):
        if int(self._amount) > 0:
            return int(self._amount)
        else:
            return 1


    def calcPTCR(self):
        if any(self._typeLine) == "Creature":
            return (self._power + self._toughness)/self._cmc
        else:
            return 1

        

    def CreateCleanCard(self):
        """
        Method to create neural network ready card obj.

        Args:
            Cards obj
        Returns:
            CardObj ready to neural network
        """

        cardObj = CleanCard(
            name = W2V.getSentenceVector(self.getName()), # Name as vector via word to vec
            amount = self.getAmount(), # Amount
            typeLine = W2V.getSentenceVector(self.getTypeLine()), # Typeline  as vector via word to vec
            oracleText = W2V.getSentenceVector(self.getOracleText()), # OracleText as vector via word to vec
            cmc = self.getCmc(), # CMC
            colorIdentity = (self.getColorIdentity()), # ColorIdentity
            colors = (self.getColors()), # Colors
            defence = self.getDefence(), # Defence
            keywords = (self.getKeywords()), # Keywords
            loyalty = (self.getLoyalty()),
            manaCost = self.getManaCost(), # Mana cost
            power = self.getPower(), # Power
            toughness = self.getToughness(), # Toughness
            #PTCR = 1
        )
        
        return cardObj