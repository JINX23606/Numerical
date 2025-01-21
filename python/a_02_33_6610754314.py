#Exercise 1
y = ["a", "b", "c"]
z = [1, 2, 3]
# your code here
y.append(z) #add [1,2,3] in y by list variable
y.extend(z) #add 1,2,3 in y list by integer variable
print(y)
#-------------------------------------
#Exercise 2
print(list(range(1,11)))
print(list(range(2,11,2)))
#-------------------------------------
#Exercise 3
t = (1,2,3,4,5)
#t[0] = 100 #error
#t.append("! !") #error
#t.sort() #error
#t.reverse() #error #cannot change tuple date
print(t)
#-------------------------------------
#Exercise 4
foo = ("good","luck!")
mimic_enumarate = list(zip(range(len(foo)),foo))
real_enumarate = list(enumerate(foo))
is_it_equal = mimic_enumarate == real_enumarate
print(is_it_equal)
#-------------------------------------
#Exercise 6
australia_data = {
    'country':'Australia',
    'area_km2':7741220.0,
    'major_lake':['Lake Eyre','Lake Torrens','Lake Gairdner','Lake Mackay','Lake Frome','Lake Amadeus'],
    'population':26768598,
    'real_gdp_growthrate_in_year_percent':{
        2023:3.02,
        2022:4.27,
        2021:2.11
    },


}
print(australia_data)