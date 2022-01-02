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
    return header, csv_dict    
    #for k,v in csv_dict.items():
     #   print(k, v)        
        
        

if __name__=="__main__":
    
    readFileName = "CityPop.csv"
    header, csv_dict=csv_reader()

    years=input('Please specify two years in yr0000 format: ')
    years=years.strip().split(',')
    year_0=years[0]
    year_1=years[1]

    out_header = ['id', 'city', 'population_change']
    if year_0 and year_1 in header:
        with open("CityPopChange.csv", 'w') as outfile:
            outfile.write(','.join(out_header)+'\n')
            for city in csv_dict:
                pop_difference=abs(float(csv_dict[city][year_0])-float(csv_dict[city][year_1]))
                outfile.write(','.join([csv_dict[city]['id'], city, str(pop_difference)])+'\n')
    else:
        print('The year(s) you input is not in the list.')
            
            


