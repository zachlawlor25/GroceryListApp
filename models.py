import json

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
    # Opening JSON file
    f = open('items.json')
 
    # returns JSON object as
    # a dictionary
    data = json.load(f)

    #create list to get next sequence in keys
    intList = []

    for item in data.keys():
      intList.append(int(item))

    nextVal = (intList[-1] + 1)
    
    #Add new values to dictionary
    data[str(nextVal)] = {"item": self.name, "store": self.store}

    with open('items.json', 'w') as jsonFile:
      json.dump(data, jsonFile, indent=4)
    
    print(data)
