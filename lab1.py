
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError
   if len(int_list) == 0:
      return None
   max = int_list[0];
   for int in int_list:
      if int > max:
         max = int;
   return max

def reverse_rec(int_list):   # must use recursion
   if int_list == None:
      raise ValueError
   if int_list == []:
      return []
   return [int_list[len(int_list) - 1]] + reverse_rec(int_list[0:len(int_list) - 1])
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""

def bin_search(target, low, high, int_list):  # must use recursion
   if int_list == None:
      raise ValueError
   mid = int((low + high) / 2)

   print(low, "[", int_list[low], "]", " ", mid, "[", int_list[mid], "]", " ", high, "[", int_list[high], "]")

   if target == int_list[mid]:
      print("return", mid, "target", target)
      return mid
   elif target > int_list[mid]:
      print ("target >",target)
      bin_search(target, mid, high, int_list)
   elif target < int_list[mid]:
      print("target <",target)
      bin_search(target, low, mid, int_list)
   else:
      print("return None")
      return None
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   pass
