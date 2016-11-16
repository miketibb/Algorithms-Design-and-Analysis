##Merge Sort
Merge sort is the first algorithm covered in the course. It takes an unordered array of length n and sorts in O(n log n) time.
It accomplishes this feat by recursively dividing the array into smaller and smaller halves until we arrive at the
base case which is an array of length 1. Because the algorithm recursively divides the problem into smaller and smaller
subproblems this is the first of several divide and conquer algorithms that are covered in the course. This project has
2 main objectives, one is to created a sorted array but the other is to count the number of split inversion.

After the the program has recursively divided the array into smaller and smaller left and right halves it will compare
the values stored in the left half to the values stored in the right half. It loops through both left and right halves, comparing the values of each.
If the value under inspection in the left half is less than the value in the right half the algorithm simply places that value into the sorted array. If, however, the value
in the right half is less than the value in the left half the algorithm places the value of right half into the sorted list and 
adds one plus the length of the uninspected elements in left half to the inversions counter. If an element in right half is
larger than an element in left half it is known as a split inversion and because we are guaranteed that that each half 
will be orderer (the base case being an array of length one which is already sorted) we can be assured that all the elements
after the current element under inspection in left half will also be larger than the element under inspection in right half. The algorithm
 works its way back up from the base cases inspecting larger and larger halves at each step.

The running time of this algorithm is O(n log n) because it creates log n layers of subproblems and the process of
sorting at each layer is done in linear time.
