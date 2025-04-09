# Import GUI (JarAPp)
from appJar import gui
from Deck import Deck
import filefun
import matplotlib.pyplot as plt
import numpy as np
# From here below are for histogram
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

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
        currentDeck = Deck.createCards(filefun.openFile(app.getEntry("DeckUpload")))
        deckPreviewText = Deck.getAllCardNames(currentDeck)
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
        data = Deck.getSameTypeLines(currentDeck, type = searchTerm)
        app.clearListBox("DeckPreview", callFunction=False)
        app.addListItem("DeckPreview", "All cards with '" + str(searchTerm) + "': ")
        app.addListItems("DeckPreview", data.keys())

    if item == "Mana Curve":
        cmcData = Deck.createManaCurve(currentDeck)
        createHistogram(cmcData)
    if item == "Permanents":
        deckPreviewText = Deck.getAllCardNames(Deck.getPermanents(currentDeck))
        app.clearListBox("DeckPreview", callFunction=False)
        app.addListItems("DeckPreview", deckPreviewText.values()) # names are {x:name] in dict
    if item == "Spells":
        deckPreviewText = Deck.getAllCardNames(Deck.getInstantsAndSorceries(currentDeck))
        app.clearListBox("DeckPreview", callFunction=False)
        app.addListItems("DeckPreview", deckPreviewText.values()) # names are {x:name] in dict
    if item == "Card Distribution":
        createHistogram(currentDeck)
        

def createHistogram(list):
    """
    Function to create histogram of a list

    Args:
        a List to craete histogram from
    Returns:
        None
    """
    # Create plot
    plt.hist(list)  # You can adjust the number of bins as needed
    plt.xlabel('CMC')
    plt.ylabel('Frequency')
    plt.title('CMC Distribution')
    plt.grid(True)  # Add grid lines (optional)
    plt.show()  # Display the histogram
    plt.yticks(range(min(list), max(list) + 1)) # y-axis to whole numbers

    fig = Figure(figsize=(6, 4))

    # Embed the figure in a Tkinter canvas
    canvas = FigureCanvasTkAgg(fig, master="GraphCanvas")
    canvas.draw()
    canvas.get_tk_widget().pack()


### GUI
app = gui("MTGDeckStats", "800x600")
# Stickiness and strechiness
app.setSticky("new") # North, East, West
app.setStretch("column")
# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Welcome to MTGDeckStats")
app.setBg("lightblue")
app.setFont(20)

# Menu
fileMenus = ["Close"]
app.addMenuList("Menu", fileMenus, menuControls)

# DataMenu
dataMenu = ["Type Search", "Mana Curve", "Permanents", "Spells", "Card Distribution"]
app.addMenuList("Data", dataMenu, dataMenuControls)

## File Entry
app.addFileEntry("DeckUpload")

# Add Load button
app.addButton("Load", press)

# Deck Preview window.
app.addListBox("DeckPreview")

# Graphs
app.addCanvas("GraphCanvas")