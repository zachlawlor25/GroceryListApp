import json
from json.decoder import JSONDecodeError

class Item:
  def __init__(self, name, store):
    self.name = name
    self.store = store

  def readJson():
    # Opening JSON file
    f = open('items.json')
 
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    
    # Iterating through the json
    # list
    for i in data:
        print(f"Item {i}: {data[i]}")
    
    # Closing file
    f.close()

  def writeJson(self):

    try:
      # Opem json file
      f = open('items.json')
 
      # returns JSON object as
      # a dictionary
      data = json.load(f)
    except JSONDecodeError:
      #creates dictionary if JSON file is empty and can't create a dictionary
      data = {}

    #create list to get next sequence in keys
    intList = []
    for item in data.keys():
      intList.append(int(item))
    
    #checks if there is an index created already, if not, starts the new value at 1
    if (len(intList) > 0):
      nextVal = (intList[-1] + 1)
    else:
      nextVal = 1
    
    #Add new values to dictionary
    data[str(nextVal)] = {"item": self.name.title(), "store": self.store.title()}

    with open('items.json', 'w') as jsonFile:
      json.dump(data, jsonFile, indent=4)
    
