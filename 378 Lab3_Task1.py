import os
os.path.exists("CityPop.csv")

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
        print(city_dict)
        csv_dict[record[city_index]]=city_dict
    f.close()
        
    for k,v in csv_dict.items():
        print(k, v)        
        
        

if __name__=="__main__":


    
    readFileName = "CityPop.csv"
    csv_reader()


