import json

def findGroupsInLocation(coordinate):
    '''Returns data about all groups in a coordinate, returns None if there are no groups present.'''
    groups = []
    with open("backend/groups.json", "r") as file:
        # Decodes JSON from groups file into python lists and dictionaries
        allGroups = json.loads(file.read())
    # Searches all groups for correct location
    for group in allGroups:
        # Checks if location matches with specified location 
        if (group["location"]["x-axis"] == coordinate[0]) and (group["location"]["y-axis"] == coordinate[1]):
            groups.append(group)
    if groups == []:
        return(None)
    else:
        return(groups)

def findGroupByName(name):
    '''Returns data about all groups with the specified name, returns None if there are no groups present.'''
    groups = []
    with open("backend/groups.json", "r") as file:
        # Decodes JSON from groups file into python lists and dictionaries
        allGroups = json.loads(file.read())
    # Searches all groups for correct name
    for group in allGroups:
        # Checks if name matches with specified name
        if group["name"] == name:
            groups.append(group)
    if groups == []:
        return(None)
    else:
        return(groups)

def getGroupNameFromUser(groupNames):
    '''Asks the user for a valid name until one is given, a valid name is one that is unique to all other names.'''
    # In future this will connect to front end
    while True:
        newName = input("Enter new group name: ")
        if newName in groupNames:
            print("This name is already in use")
            pass
        else:
            break
    return(newName)

def getLocationFromUser():
    '''Asks the user to select a location on the map'''
    # In future this will connect to front end
    x = input("Enter x-axis: ")
    y = input("Enter y-axis: ")
    return((x, y))
    
def mergeGroupNames(group1, group2):
    '''Creates new name for merging groups and ensures there is no duplicate names for groups.'''
    # Retrieves the list of all unique group names
    with open("backend/groupNames.json", "r") as file:
        groupNames = json.loads(file.read())
    # Removes names of both groups from unique group name list
    groupNames.remove(group1["name"])
    groupNames.remove(group2["name"])
    newName = getGroupNameFromUser(groupNames)
    # Adds new group name to unique group name list
    groupNames.append(newName)
    with open("backend/groupNames.json", "w") as file:
        file.write(json.dumps(groupNames))
    return(newName)
    
def mergeGroupUnits(group1Units, group2Units):
    '''Sums up values of different group's units and removes duplicates.'''
    newGroupUnits = []
    for unit in group1Units:
        newGroupUnits.append(unit)
    for unit in group2Units:
        # Checks all dictionaries in newGroupUnits for duplicates
        for newUnit in newGroupUnits:
            keyOfUnit = list(unit.keys())[0]
            keyOfNewUnit = list(newUnit.keys())[0]
            valueOfUnit = unit[keyOfUnit]
            valueOfNewUnit = newUnit[keyOfNewUnit]
            if keyOfUnit == keyOfNewUnit:
                totalValue = valueOfUnit + valueOfNewUnit
                unit.update({keyOfUnit: totalValue})
            else:
                pass
        newGroupUnits.append(unit)
    return(newGroupUnits)

def mergeGroups(group1, group2):
    '''Takes the data for two different groups, adds their units together, and returns data for a single group.
    If the groups are of opposing factions, the groups will fail to merge, None will be returned.
    If locations are different, a new location will be requested from the user.'''
    # Checks if location of group 1 is different than location of group 2
    if group1["location"] != group2["location"]:
        newLocation = getLocationFromUser()
    else:
        newLocation = group1["location"]
    # Checks that factions are the same - cannot merge opposing factions
    if group1["faction"] != group2["faction"]:
        return(None)
    else:
        newFaction = group1["faction"]
    newName = mergeGroupNames(group1, group2)
    newUnits = mergeGroupUnits(group1["units"], group2["units"])
    # Create new group object
    newGroup = {
        "faction": newFaction,
        "name": newName,
        "location": {
            "x-axis": newLocation[0],
            "y-axis": newLocation[1]
        },
        "units": newUnits
    }
    # Save group to groups.json
    with open("backend/groups.json", "r") as file:
        allGroups = json.loads(file.read())
    group1 = findGroupByName(group1["name"])[0]
    group2 = findGroupByName(group2["name"])[0]
    print(allGroups)
    print(group1)
    print(group2)
    allGroups.remove(group1)
    allGroups.remove(group2)
    allGroups.append(newGroup)
    with open("backend/groups.json", "w") as file:
        file.write(json.dumps(allGroups))

def createGroup(faction, units):
    '''Unfinished'''
    with open("backend/groupNames.json", "r") as file:
        groupNames = json.loads(file.read())
    name = getGroupNameFromUser(groupNames)
    groupNames.append(name)
    with open("backend/groupNames.json", "w") as file:
        file.write(json.dumps(groupNames))
    location = getLocationFromUser()
    group = {
        "name": name,
        "faction": faction,
        "location": location,
        "units": units
    }
    # Save group to groups.json
    with open("backend/groups.json", "r") as file:
        allGroups = json.loads(file.read())
    allGroups.append(group)
    with open("backend/groups.json", "w") as file:
        file.write(json.dumps(allGroups))