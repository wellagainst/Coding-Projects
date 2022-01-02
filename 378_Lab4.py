#import package to draw the plot
import numpy as np
import matplotlib.pyplot as plt

#create a class City and define the initiation method to be ready to assign values to attributes (question 1)
class City:
    def __init__(self, name, label, latitude, longitude, population):
        #specify the attributes
        self.name=name
        self.label=label
        self.latitude=latitude
        self.longitude=longitude
        self.population=population
    #define two methods (behavior of the class)
    def printDistance(self, othercity):
        #import math package to calculate the distance
        import math
        #transform string into float numbers for two cities
        self_lat=math.radians(float(self.latitude))
        self_lon=math.radians(float(self.longitude))
        othercity_lat=math.radians(float(othercity.latitude))
        othercity_lon=math.radians(float(othercity.longitude))
        #calculate the distance between two cities
        d = math.acos(math.sin(self_lat)*math.sin(othercity_lat) + math.cos(self_lat)*math.cos(othercity_lat)*math.cos(self_lon-othercity_lon))
        spherical_distance=round(6300*d)
        print("the distance between ", self.label, " and ", othercity.label, " is ", str(spherical_distance), " km")

    def printPopChange(self, year1, year2):
        pop_data=self.population
        #make sure we have both years
        if year1 in pop_data and year2 in pop_data:
            #get one city's population values in two different years
            year1_pop=float(pop_data[year1])
            year2_pop=float(pop_data[year2])
            #calculate the change between years and print the change in population for users
            #here I use abs because the concept "change" itself does not have negative or positive values. It is just change.
            difference=abs(year1_pop-year2_pop)
            print("The population change is ", difference, " million.")
        #if one or more year(s) is not in our data, just let the user know
        else:
            print("Sorry, the year(s) you input does not exist in our file.")
        



if __name__=='__main__':
    #open and read in CityPop csv file (and close it after use)
    readFileName='CityPop.csv'
    with open(readFileName, 'r') as f:
        #split a big string into a list of strings
        header=f.readline().strip().split(',')
        #city_list is to store city instances for the City class (for question 2)
        #city_pop: a dictionary with all cities are the keys and city's population values as list (for question 3)
        city_list=[]
        city_pop={}
        for line in f:
            #split each line(one big string) of CityPop as records (lists of strings);
            #find each attribute's position in the header, and get the value in each record at that position
            record=line.strip().split(',')
            city_name=record[header.index('city')]
            city_label=record[header.index('label')]
            city_latitude=record[header.index('latitude')]
            city_longitude=record[header.index('longitude')]
            
            #temporary dictionary to store the year and corresponding population
            pop_dict={}
            #the first year appears at the 5th position in the header
            for i in range(5, len(header)):
                #populate the pop_dict with attributes as keys and population as values;
                #double for loops to get all population values 
                pop_dict[header[i]]=record[i]
                #populate city_pop dictionary with city labels as keys and population as values
                #this is for the plotting of any city's population values
                city_pop[city_label]=record[5:]
        
            #assign values to attributes of the class to create instance; add instance to the class
            city_instance=City(name=city_name, label=city_label, latitude=city_latitude, longitude=city_longitude, population=pop_dict)
            city_list.append(city_instance)
            print(city_instance.__dict__)


    #Question 2    
    #test two methods
    city_list[0].printDistance(city_list[1])
    city_list[0].printPopChange('yr1970','yr1990')



    #Question 3
    #set the attributes from 5th position of the header to end of the header as values on x-axis
    #select Tokyo and Moscow; set their respective population values on y-axis values
    x=header[5:]
    y_Tokyo=city_pop['Tokyo']
    y_Moscow=city_pop['Moscow']
    #plot population values in blue stars and red dots
    plt.plot(x,y_Moscow,'b*')
    plt.plot(x,y_Tokyo,'ro')
    #add legend, location of the legend, x label and y label
    plt.legend(['population of Moscow', 'population of Tokyo'], loc='upper left')
    plt.xlabel('X-Axis: Year')
    plt.ylabel('Y-Axis: Population')
    plt.show()
    
    
    
    

    
