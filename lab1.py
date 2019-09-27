
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""

   if int_list == None: #base case
      raise ValueError
   if len(int_list) == 0: #base case
      return None
   max = int_list[0]; #initialize max to first value instead of 0, in the case that the max is a negative # in which case 0 would not work and would already be greater than the max value of the list and result in an error
   for int in int_list: #loop throgh list
      if int > max: #if new max is found set max value
         max = int;
   return max #after looping through all numbers return max

def reverse_rec(int_list): # must use recursion
   if int_list == None: #base case
      raise ValueError
   if int_list == []: #base case
      return []
   return [int_list[len(int_list) - 1]] + reverse_rec(int_list[0:len(int_list) - 1]) # creates new list with the ending of the list as the first value and concatenates with another list (which is given by recursively running the function)
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""

def bin_search(target, low, high, int_list):  # must use recursion
   if int_list == None:
      raise ValueError #base case
   mid = int((low + high) / 2) #calculate middle of resized list given high and low

   if target == int_list[mid]: #if the target value is in middle of the list return the index of middle
      return mid
   elif target == int_list[mid + 1]: #used when there are 2 "middle" values depending on current list size / returns index of "middle"
      return mid + 1
   elif low == mid: #base case (kinda) / when the search is stuck between 2 values returns None, meaning the value is not in the list
      # print("return None") #debug code
      return None
   elif target > int_list[mid]: #binary up and down search functionality
      # print(low, "[", int_list[low], "]", " ", mid, "[", int_list[mid], "]", " ", high, "[", int_list[high], "]") #debug code
      return bin_search(target, mid, high, int_list)
   elif target < int_list[mid]:
      # print(low, "[", int_list[low], "]", " ", mid, "[", int_list[mid], "]", " ", high, "[", int_list[high], "]") #debug code
      return bin_search(target, low, mid, int_list)


   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
