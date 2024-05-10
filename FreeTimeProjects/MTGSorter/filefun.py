import json

## Read/Open the data
def openFile(file):
    """
    Opens given file.

    Args:
        File to be opened

    Returns:
        Opened file (str)
    """

    try:
        with open(file, 'r', encoding="utf8") as deckfile:
            deckData = deckfile.read()
    except FileNotFoundError:
        print("Error: Invalid format in the deck file.")

    return deckData

def openJSON(file):
    """
    Opens given JSON.

    Args:
        JSON to be opened,
        Read / Write / Execute,
        Encoding type
    Returns:
        Open JSON
    """
    with open(file, "r", encoding="utf8") as openFile:
        scryFile = json.load(openFile)

        return scryFile