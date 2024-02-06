# Working with lists

Write two functions that will add or take away an element from a list.

## Adding to a list
Your function should 

1. be called `addToList`
2. take two input arguments: `mylist`, the list you want to edit and `x` the
   element you want to add to the list
3. return the extended list

Thus
      
      print(addToList([1, 2, 3], 4))
should print out `[1, 2, 3, 4]`

## Truncating a list
Your function should

1. be called `truncateList`
2. take two input arguments: `mylist`, the list you want to edit and `N` the
   number of elements you want to remove from the end
3. if `N` is larger than the number of elements in the list, your function
   should return the `mylist` unedited.

Thus 
   
      print(truncateList([1, 2, 3], 1))
should print out `[1, 2]` (we're removing the last element), but

      print(truncateList([1, 2, 3], 4))
should print out `[1, 2, 3]` (we asked to remove four elements, but there are
only three, so the list is returned, unedited).
