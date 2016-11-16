##Quicksort
This algorithm solves the same problem as Merge Sort, namely sorts an unsorted array of length n.
The runtime is the same as Merge Sort, O(n log n), but unlike Merge Sort Quicksort is upper bounded
with a runtime of O(n*n). The reason for this discrepancy is that the runtime of Quicksort is 
dependent on our selection of a pivot point. The pivot point is an element in the array that 
we choose to compare every other element in the partitioned array to. If the element we are comparing
to the pivot is smaller than the pivot we move it up towards the front of the array. Once the pivot
has been compared to every other element in the array we swap the pivot with the last number
we found to be smaller than the pivot. This ensures that the pivot is now in its proper place in the array.

After putting the pivot in it's proper spot we have all the numbers smaller than the pivot to the left
and all the numbers larger to the right. We partition the array with all the numbers smaller than the pivot
in their own subarray and all the numbers larger in their own subarray. We pick a new pivot from each of
these subarrays and we repeat the process. This process continues until we reach the base case (array of
length one and everything has been properly sorted).

The runtime of this algorithm is dependent upon the choice of the pivot. The worst case would be if we choose
the pivot as the smallest or largest element in the array. This is because the subarray split we would get
would be very lopsided, namely every element would be on one side. If we can choose the median element however
the algorithm would run in O(n log n). We cannot guarantee a selection of the median but if we can expect a 
25 - 75 split on average then we can achieve this blazingly fast speed. We are able to do this by selecting
a split at random. Linearity of Expectation guarantees that with a sufficiently large n we can expect a 25 - 75
split on average.