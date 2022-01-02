import math

def csv_reader():
    f=open(readFileName,"r")
    header=f.readline()
    #print(type(header))--str
    header=header.strip().split(',')
    #print(type(header))
    
    city_index=header.index('city')
    #print(city_index)
    
    csv_dict={}
    for line in f:
        record=line.strip().split(",")
        city_dict={}
        for j in range(0, len(header)):
            city_dict[header[j]]=record[j]
        csv_dict[record[city_index]]=city_dict
    f.close()
    return csv_dict, city_dict    
    #for k,v in csv_dict.items():
     #   print(k, v)        
        
        

if __name__=="__main__":


    
    readFileName = "CityPop.csv"
    csv_dict, city_dict=csv_reader()



    cities=input('Please input two city names: ')
    cities=cities.strip().split(',')
    city_0=cities[0]
    city_1=cities[1]
    if city_0 and city_1 in csv_dict.keys():
        x_0=csv_dict[city_0]['latitude']
        y_0=csv_dict[city_0]['longitude']
        x_1=csv_dict[city_1]['latitude']
        y_1=csv_dict[city_1]['longitude']
    
        lat_0 = math.radians(float(x_0))
        long_0 = math.radians(float(y_0))
        lat_1 = math.radians(float(x_1))
        long_1 = math.radians(float(y_1))
        
        d = math.acos(math.sin(lat_0)*math.sin(lat_1) + math.cos(lat_0)*math.cos(lat_1)*math.cos(long_0-long_1))
        spherical_distance=round(6300*d)
        print(spherical_distance)
    else:
        print('One or both cities not in the list')
        
