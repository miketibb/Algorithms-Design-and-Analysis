# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 14:40:17 2016

@author: Jake
"""

import heapq

def maintain_median(nums):
    median = [nums[0]]
    lo_heap, hi_heap = [nums.pop(0)], []
    while nums:
        num = nums.pop(0)
        if num >= max(lo_heap):
            heapq.heappush(hi_heap, num)
        else:
            heapq.heappush(lo_heap, num)
        if len(lo_heap) > len(hi_heap) + 1:
            heapq.heappush(hi_heap, max(lo_heap))
            lo_heap.remove(max(lo_heap))
            heapq.heapify(lo_heap)
        if len(hi_heap) > len(lo_heap) + 1:
            heapq.heappush(lo_heap, min(hi_heap))
            hi_heap.remove(min(hi_heap))
            heapq.heapify(hi_heap)
        if len(lo_heap) >= len(hi_heap):
            median.append(max(lo_heap))
        else:
            median.append(hi_heap[0])
    return median
        
def main():
    file = open('Median.txt')
    nums = [int(line) for line in file]
    medians = maintain_median(nums)
    return sum(medians)%10000
    
if __name__ == '__main__':
    print(main())