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

    while True:
        
        s=input('Please input a city name and a year in yr0000 format: ')
        if len(s)<1:
            break
        try:
            s=s.split(',') # example: 'Tokyo, yr2020' --> ['Tokyo', 'yr2020']
            city_name=s[0]
            year=s[1]

            if city_name in csv_dict.keys():
                if year in city_dict.keys():
                    print(csv_dict[city_name][year])
                else:
                    print("The year you input is not in the list.")
            else:
                print('The city you input is not in the list.')
        except:
            print('Try again.')

