# dictionaries.py

from itertools import combinations


def demo():
    """
    Demonstrate basic dectionary stuff
    """
    myDictionary = {"Cincinnati":"Bearcats", "Xavier":"Musketeers", "NKU":"Norse", "UC Clermont":"Cougars"}
    print(myDictionary)
    
    #iterate over dictionary by key
    for key in myDictionary.keys():
        print(key)
    
    # Iterate by key/value
    for item in myDictionary.items():
        print(item)
        
    # Iterate by value
    for value in myDictionary.values():
        print(value)


    # add a key/value pair to the dictionary 
    myDictionary["Michigan State"] = "Spartans"
    
    print(len(myDictionary))
    
    # Cause an exception Add try/except logic to gracefully handle this 
    try:
        print(myDictionary["Ohio State"])  
    except:
        print("Ohio State is an invalid key ")
    
    #remove Xaiver by key and print the enitre dictionary
    
    myDictionary.pop('Xavier')
    print(myDictionary)
    
    #Create another dictonary called newTeams. 
    #Add several key value pairs 
    #Combine that with myDictionary and print the results

    newTeams = {"Penn State": "Nittany Lions", "Florida":"Gators", "Clemson":"Tigers"}

    myDictionary.update(newTeams)    
    print(myDictionary)
    
    """
    #Brute force 
    for key in newTeams.key():
        myDictionary[key] = newTeams[key]
    print(myDictionary)
    """