import pandas as pd
import time
from datetime import date
import re

poke = pd.read_csv('pokemon_data.csv')

#print(poke.tail(5))
#print(poke.head(5))
#print(poke.columns)
poke_header = poke.columns # This is how you create a variable
#print(poke_header[4:]) #This is how you print out just the header.
#print(poke[["HP"]]) #This is how you print out an entire column
#print('This is a printout of just the fourth row (third row of data)')
#print("-" * 70)
#print(poke.iloc[2])
#for index , lines in poke.iterrows():
    #print(f"this is the index:{index} \n{lines}")

#print(poke.loc[poke['Type 1'] == "Fire"]) # This is a method of filtering your files
#print(poke.loc[poke['Type 1'] == "Fire"].describe())
#print(len(poke["Type 1"].unique()))

# Creating a file that holds the descriptive analysis of all numeric variables in the dataset
poke_types = poke["Type 1"].unique() #creates a list of the unique observations in the variable Type 1.
poke_anal = open(f"Pokemon_{date.today()}.txt","w")
data = ""
for types in range(len(poke["Type 1"].unique())):
    title = f"Pandas Descriptive analysis of the Pokemon Type {poke_types[types]}" +'\n'
    analysis = poke.loc[poke['Type 1'] == f"{poke_types[types]}"].describe()
    poke_anal.write(title)
    poke_anal.write(str(analysis) + "\n")
poke_anal.close()

max_hp = 0
for obs in poke["HP"]:
    if obs > max_hp:
        max_hp = obs
    else:
        max_hp = max_hp
print(f"max HP = {max_hp}")

print(poke.sort_values("Name")) # prints a sorted version of the dataset by the variable name
print(poke.sort_values("Name", ascending=False)) # prints a sorted version of the data set by the variable Name, in ascending order
print(poke.sort_values(["Type 1", "Speed"],  ascending=[1,0]))



# One method for adding variables
poke['Total'] = poke['HP'] + poke['Speed'] + poke['Attack'] + poke['Defense'] + poke['Sp. Atk'] + poke['Sp. Def']
print("this is the output for the newly created Total variable.")
# Another method for adding variables
poke["Total2"] = poke.iloc[:,4:10].sum(axis=1) #The first ":" means you want this to run over all of the columns axis = 1 tells python to add the colums horixontally, vs vertically
poke["per_of_max_hp"] = poke['HP'] / max_hp #f"{round((poke['HP'] / max_hp),2)}%"
print(poke['Total'])
print(poke['Total2'])



#print(poke.loc[poke["Name"].str.contains("Mega")])
#print(poke.loc[poke["Name"].str.contains("fire|grass",flags=re.I, regex=True)]) #flags =re.I says use re and ignore case
print(poke.loc[poke["Name"].str.contains("^pi\w+",flags=re.I, regex=True)])
#rename_poke = poke.loc[poke["Type 1"] == "Fire", "Type 1"] = "Flamer" #changing an observation
poke.loc[poke["Type 1"] == "Fire", "Type 1"] = "Flamer"

#Using one condition to modify / create a new variable
poke["The_Man"] = False
poke.loc[poke["per_of_max_hp"] > .6, "The_Man"] =  True

#--------------------------------Running Analysis--------------------------------

des = poke.groupby(['Type 1']).describe()
des.to_csv(f"Descriptives_{date.today()}.csv", sep=",")

mean = poke.groupby(['Type 1']).mean()
#print( poke.groupby(['Type 1']).max() ) # gets the max of each column
mean.to_csv(f"Means_{date.today()}.csv", sep=",")

#How to get frequencies and counts
poke['count'] = 1
print(poke.groupby('Type 1').count()['count'])
print(poke.groupby(['Type 1','The_Man']).count()['count'])
print(type(poke.groupby('Type 1').count()['count']))

# creating subsets of the data frame
poke_grass = poke.loc[poke["Type 1"] == "Grass"]
poke_grass_poi = poke.loc[(poke["Type 1"] == "Grass") & (poke["Type 2"] == "Poison") ]



#outputing
poke.to_csv(f"modified_{date.today()}.csv")

poke.to_csv(f"modifiied_{date.today()}.txt", sep="\t")

poke_grass.to_csv(f"modified_grass(only)_{date.today()}.csv")
poke_grass_poi.to_csv(f"modified_grass_poi_{date.today()}.csv")