#Linear Search
state = True

def main():
    target = int(input("What value would you like to search for?: "))
    linear_search(target)
    
data_set = [7,12,346,788,776,33,52,55,4,357,8888,654,3332,445,1]


def linear_search(target):
    pointer  = 0
    for item in data_set:
        if item == target:
            print (target,"value found at", pointer)
            
            
        elif item != target:
            pointer += 1
            
        
    if target not in data_set:
        print ("Value isn't in dataset.")
   
while state == True:
    main()
   
