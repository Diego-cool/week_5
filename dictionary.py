# dictionary = a collection of {key: value} pairs 
#              ordered and changeable. No duplicates
capitals={"USA": "Washington D.C",
          "India" : "New delhi", 
          "China" : "Beijing",
          "Russia" : "Moscow"}
#print(dir(capitals))  gives the attributes for the dictionary
#print(help(capitals))  gives back documentation
#if capitals.get("Russia"):
 #   print("that capital exists")
#else: 
#   print("That capital doesnt exist")

#capitals.update({"Germay": "Berlin"})
#capitals.update({"USA": "Detroit"})
#capitals.pop("China")
#print (capitals) 
#capitals.popiteam()#removes last iteam in dictionary
#capitals.clear()# Clears dictionary
#keys = capitals.keys()

#values= capitals.values()


#for key in capitals.keys():
#    print(key)

#for value in capitals.values():
#print(values)
#items= capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")