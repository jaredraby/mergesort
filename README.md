# mergesort
Merge sort implementation in python

Bottom Up implementation of merge sort

**Requirements**  
The mergesort will take in an array and sort the values in ascending order.


**Functionality**

mergesort(array)  
  * Break down the entire array into mod 2 groups
    * Create a loop variable, tracking the number of times the sort fucntion has been called
    * Loop while loop variable < log2(n) rounded down where n is number elements in an array
      * :
      * Call sorting function which keeps track of left an right array value indices
        * Loop
          * Create a right array and left arround index value to strack the index of compared values
          * Compare each value and put them back into the original array 
        * End loop

