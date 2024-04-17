# CMPS 2200 Assignment 3
## Answers

**Name:**_______Mengzhou Wang__________________


Place all written answers from `assignment-03.md` here for easier grading.

1.a,  for each time, find the largest number that is power of 2 but smaller then n. Since all coins is power of 2, it's include all value. In this way, it can produce as few coins as possible that sum to N

1.b, For each time, choosing the largest coin(2^k) can help us find the optmal choice for this substructure,which is we using the fewest coins to do that. Each time we find the largest coin value is a substructure for whole problem. For each substructure, we have optaml substructure properties can make whole solution is optmal.

1.c the work and span are both O(logn)

2.a for example, the denominations has coin 1, 3, 4, 5 if n=7 and we use same greedy algorithm. we will get the coin 5, 1, 1, but the optmal choice is 3, 4.

2.b optmal structure property in this problems is find possible solution that can get N if we add one more coin. To find the minimum coins we use for those possible solution is finding optmal structure. And each substructure have has to find their optmal substructure until we use 0 coin.

3.c work is O(n) span is O(n)