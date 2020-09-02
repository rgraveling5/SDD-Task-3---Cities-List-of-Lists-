
#Cities (Lists of Lists)

#Rachael graveling
#02/09/2020

#A programmer wants to allow the user to enter and display the following information on cities in Europe. It could eventually store details on 250 locations, but for now we will work with only 3 entries. city, country, population (millions), main language
#glasgow scotland 0.5 england, faro portugal 1.0 portuguese, edinbugrh scotland 0.4 english

#create list for an individual city
ind_city = []

#create list of the lists of cities
all_cities = []
for i in range (3):
  #input info into ind_city
  ind_city.append(input("City name: "))
  ind_city.append(input("Country: "))
  ind_city.append(input("Population: "))
  ind_city.append(input("Main Language: "))
  all_cities.append(ind_city)

for city in (ind_city):
  print (city)


