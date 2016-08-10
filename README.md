# Linear-Sort
Basic O(n) sorting algorithm

  When I was first learning about sorting alogrithms I wanted to see if I could beat the algorithms that we were learning in class by
writing a sorting algorithm that worked in O(n) time. This is the algorithm that I came up with, written in Python.

  I later learned that this is a essentially a simplified version of a well known algorithm called Bucket Sort. An algorithm that only
works with data sets that have an equivalence class relation (reflexive, symetric, and transative), or that do not need to be fully sorted. 

  Although this is an algorithm that works in linear time, it is not as efficient as the Timsort algorithm which takes advantage
of CPU architecture in order to run at optimal speeds. In this repository you will see a screenshot of the benchmarks between my
algorithm and the Timsort (I called it pysort because it is the default built in Python sorting algorithm).
