def fre(my_list):
    #using empty dictionary
    freq={}
    for item in my_list:
        if(item in freq):
            freq[item]+=1
        else:
            freq[item]=1
    for key,value in freq.items():
        print(f"{key}:{value}")

my_list=[1, 2, 3, 4, 4, 3, 5, 6]

fre(my_list)