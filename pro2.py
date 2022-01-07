import csv

pokenum= input(">")

pokedex= {}
with open("pokedex.txt","r") as pokedata:
    for x in csv.DictReader(pokedata):
        pokedex.update({x["#"]:x["Name"]})

with open("pokedex.txt","r") as pokedata:
    for x in csv.DictReader(pokedata):
        # value of pokenum is now 39
        pokedict= dict(x)
        if int(pokenum) <= 15:
            pokethief = "39"
            # pokedict-name == current pokemon is in the loop
            print(f"{pokedex[pokethief]} has taken your Pokemon!")
            break
        if pokedict["#"] == pokenum: # only true if it's pokemon 39
            print(f"{pokedict['Name']} is {pokedict['Legendary']}")