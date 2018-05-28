'''
Carla Salguero
worked With Rachel Levy 
Part 4: List Functions

'''
#1. 
# function:    listlen
# INPUT:       a list
# PROCESSING:  determines the size of the list
# OUTPUT:      an integer representing the size of the list

def listlen(list): 
    amount = 0 #set up the accumulator as zero. 
    for element in list: 
        amount +=1 #adds it by once for each. 
    return amount

mylist = [10,30,30]
x = listlen(mylist)
print(x)


#2.        
# function:    listmax
# INPUT:       a list
# PROCESSING:  obtains the largest element in the list
# OUTPUT:      returns the largest element in the list

def listmax(list):
    max = list[0] #defines what the max is. 
    for i in range(0,len(list)):
        if list[i] > max:
            max = list[i] #is the max at that particular point. 
    return max
        
mylist = [10, 20, 30, 5, 3]
x = listmax(mylist)
print (x)
print (mylist)

#3. 
# function:    listcopy
# INPUT:       a list
# PROCESSING:  creates a new list which serves as a copy of the supplied list
# OUTPUT:      returns a new copy of the list

def listcopy(list):
    copy = []
    for i in range (0,len(list)):
        copy += [list[i]] #builds up the list by using += []
    return copy



mylist = [10, 20, 30]
x = listcopy(mylist)
print (x)

#4. 
# function:    listappend
# INPUT:       a list and an element to add to the list (any data type)
# PROCESSING:  creates a new list which includes the new element appended
#              to the end of the list
# OUTPUT:      returns a new copy of the list

def listappend(list, element):
    list += [element] #adds the list by the element. (append)
    return list

mylist = [10, 20, 30]
x = listappend(mylist, 999)
print (x)

#5. 
# function:    listinsert
# INPUT:       a list, a location (integer) and a data 
#              element (can be a string, float, Boolean or 
#              int)
# PROCESSING:  inserts the supplied data element into the 
#              list at the desired location
# OUTPUT:      return a new copy of the list that contains
#              the inserted element


#5
def listinsert (list, location, element):
    return list[:location:] + [element] + list[location:] #the location on the list. 

mylist = [10, 20, 30]
x = listinsert(mylist, 1, 999)
print (x)
print (mylist)



#6.
# function:    listremove
# INPUT:       a list and a data element (can be a string, 
#              float, Boolean or int)
# PROCESSING:  removes all occurrences of the supplied 
#              data element from the list.  You can assume 
#              that the data element is present in the list 
#              somewhere.
# OUTPUT:      return a new copy of the list with the
#              desired element removed


#6
def listremove(list,element):
    newlist = [] #an empty list. 
    for i in list: #for every "i" in that list 
        if i != element: 
            newlist += [i] #add the list by += []
    return newlist

mylist = [10, 20, 30]
x = listremove(mylist, 20)
print (x)
print (mylist)



#7.
# function:    listreverse
# INPUT:       a list
# PROCESSING:  creates a copy of the supplied list that
#              contains the same elements as the original
#              list, but in reverse order
# OUTPUT:      return a new copy of the list in reverse order


def listreverse(l):
    ln = listlen(l) 
    a = [0]*ln
    for i in range(ln):
        a[ln-i-1]=l[i]
    return a

mylist = [10, 20, 30]
x = listreverse(mylist)
print (x)
print (mylist)



