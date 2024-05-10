# Import GUI (JarAPp)
from appJar import gui
from Cards import Cards
import filefun

def press(btn):
    """
    Load Button function

    Args:
        Button title
    Returns:
        Nothing.
    """
    # Making currentDeck global so all the tools will work
    global currentDeck

    if btn == "Load":
        # Load Deck -- Create cards -- open file -- file entry -- selected file
        currentDeck = Cards.createCards(filefun.openFile(app.getEntry("DeckUpload")))
        deckPreviewText = Cards.getAllCardNames(currentDeck)
        app.clearListBox("DeckPreview", callFunction=False)
        app.addListItems("DeckPreview", deckPreviewText.values()) # names are {x:name] in dict


# Start GUI func
def startGUI():
    """
    Starts GUI (JarApp)
    
    Args:
        None
    returns:
        Nothing.
    """
    app.go()

def menuControls(item):
    """
    MenuControl function

    Args:
        Item that was clicked
    Returns:
        Nothing.
    """
    if item == "Close":
        app.stop()

def dataMenuControls(item):
    """
    Controls for Data menu

    Args:
        Item that was clicked
    Returns:
        Nothing.
    """
    if item == "Type Search":
        searchTerm = app.stringBox("TypeLineStringBox", "What type you wish to search?")
        data = Cards.getSameTypeLines(currentDeck, type = searchTerm)
        app.clearListBox("DeckPreview", callFunction=False)
        app.addListItem("DeckPreview", "All cards with '" + str(searchTerm) + "': ")
        app.addListItems("DeckPreview", data.keys()) #### change 1

### GUI
app = gui("MTGDeckStats", "800x600")
# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Welcome to MTGDeckStats")
app.setBg("lightblue")
app.setFont(20)

# Menu
fileMenus = ["Close"]
app.addMenuList("Menu", fileMenus, menuControls)

# DataMenu
dataMenu = ["Type Search"]
app.addMenuList("Data", dataMenu, dataMenuControls)

## File Entry
app.addFileEntry("DeckUpload")

# Add Load button
app.addButton("Load", press)

# Deck Preview window.
app.addListBox("DeckPreview")