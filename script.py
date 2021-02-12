from collections import Counter #import the Counter function from collections
#file='/home/ishma/Desktop/ishma.log'
def popularishma(file):
    y = [] #empty list
    topten = [] #empty list
    with open(file) as ff: #open the ishma log
        lines = ff.readlines() #read the lines into a list
        for l in lines:
            y.append(l.strip('\n').split()[-2]) """iterate the line list convert string items into
                                                lists and remmove "\n" and append ishma_id value to the y list"""
            
        num = dict(Counter(y)) """use the Counter function to check the 
                                occurence of all the items in the y list and convert to a dictionary"""
        for i in range(10): #iterate the dictionary 10 times
            max_key = max(num, key=num.get) #getting the key with the highest value
            topten.append(max_key) #append the max_key to the topten list
            num.pop(max_key) #remove the max_key:value from the dictionary so we could get the next highest
        return topten #return the list with top ten Keys
