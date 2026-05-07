# Array Dominator Task (CS Helwan 2026).

## 1. Non-recursive Algorithm: Bruteforce Algorithm
<video controls width="100%" preload="metadata">
    <source src="./visuals/videos/1-%20BruteForce.mp4" type="video/mp4">
    <a href="./visuals/videos/1-%20BruteForce.mp4">Watch the BruteForce video</a>
</video>

### Pseudo code 
```
Function iterative1Bruteforce:
    Input: array A, integer N

    for i := 0 to N - 1 step 1 do
        candidate := A[i]
        count := 0
        for j := 0 to N - 1 step 1 do
            if A[j] = candidate then
                count := count + 1
        
        if count > N / 2 then
            return i
            
    return -1
```

### Implementation with C language.
```c
#include <stdio.h>

int iterative1Bruteforce(int A[], int N) {    
    for (int i = 0; i < N; i++) {
        int count = 0;
        for (int j = 0; j < N; j++) {
            if (A[j] == A[i]) {
                count++;
            }
        }
        if (count > N / 2) {
            return i;
        }
    }
    return -1;
}
```

### Analysis
Time Complexity: $O(N^2)$
We have two nested loops. The outer loop runs $N$ times, picking each element as a candidate. The inner loop also runs $N$ times, counting the occurrences of the candidate. This results in exactly $N \cdot N$ operations, so the time complexity is strictly $O(N^2)$.

---

## 2. Non-recursive Algorithm: Sort and Count Consecutive
<video controls width="100%" preload="metadata">
    <source src="./visuals/videos/2-%20SortAndCount.mp4" type="video/mp4">
    <a href="./visuals/videos/2-%20SortAndCount.mp4">Watch the SortAndCount video</a>
</video>

### Pseudo code
```
Function iterative2SortConsecutive:
    Input: array A, integer N

    if N = 0 then return -1
    if N = 1 then return 0

    // Create a copy of array A alongside original indices
    pairs := array of size N storing (value, original_index)
    sort pairs by value in ascending order

    count := 1
    for i := 1 to N - 1 step 1 do
        if pairs[i].value = pairs[i - 1].value then
            count := count + 1
            if count > N / 2 then
                return pairs[i].original_index
        else
            count := 1

    return -1
```

### Implementation with C language.
```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int val;
    int index;
} Pair;

int comparePairs(const void *a, const void *b) {
    int val1 = ((Pair *)a)->val;
    int val2 = ((Pair *)b)->val;
    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}

int iterative2SortConsecutive(int A[], int N) {
    if (N == 0) return -1;
    if (N == 1) return 0;

    Pair pairs[N];
    for (int i = 0; i < N; i++) {
        pairs[i].val = A[i];
        pairs[i].index = i;
    }

    qsort(pairs, N, sizeof(Pair), comparePairs);

    int count = 1;
    for (int i = 1; i < N; i++) {
        if (pairs[i].val == pairs[i - 1].val) {
            count++;
            if (count > N / 2) {
                int res = pairs[i].index;
                return res;
            }
        } else {
            count = 1;
        }
    }
    
    return -1;
}
```

### Analysis
Time Complexity: $O(N \log N)$
The algorithm relies on sorting the pairs which takes $O(N \log N)$ using a comparison-based sort. The subsequent linear scan loop executes at most $N-1$ iterations taking $O(N)$ time. The overall time complexity is dominated by the sorting step resulting in an overall time complexity of $O(N \log N)$.

---

## 3. Non-recursive Algorithm: Sort and Check Median
<video controls width="100%" preload="metadata">
    <source src="./visuals/videos/3-%20SortAndMedian.mp4" type="video/mp4">
    <a href="./visuals/videos/3-%20SortAndMedian.mp4">Watch the SortAndMedian video</a>
</video>

### Pseudo code
```
Function iterative3SortMedian:
    Input: array A, integer N

    if N = 0 then return -1
    
    pairs := array of size N storing (value, original_index)
    sort pairs by value in ascending order

    candidate := pairs[N / 2].value
    candidate_idx := pairs[N / 2].original_index

    count := 0
    for i := 0 to N - 1 step 1 do
        if A[i] = candidate then
            count := count + 1

    if count > N / 2 then
        return candidate_idx
        
    return -1
```

### Implementation with C language.
```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int val;
    int index;
} Pair;

int comparePairsMedian(const void *a, const void *b) {
    int val1 = ((Pair *)a)->val;
    int val2 = ((Pair *)b)->val;
    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}

int iterative3SortMedian(int A[], int N) {
    if (N == 0) return -1;

    Pair pairs[N];
    for (int i = 0; i < N; i++) {
        pairs[i].val = A[i];
        pairs[i].index = i;
    }

    qsort(pairs, N, sizeof(Pair), comparePairsMedian);

    int candidate = pairs[N / 2].val;
    int candidate_idx = pairs[N / 2].index;

    int count = 0;
    for (int i = 0; i < N; i++) {
        if (A[i] == candidate) {
            count++;
        }
    }

    if (count > N / 2) {
        return candidate_idx;
    }
    return -1;
}
```

### Analysis
Time Complexity: $O(N \log N)$
Similar to the previous solution, the time complexity is determined primarily by the chosen sorting algorithm, `qsort`, running in $O(N \log N)$. Extracting the median and validating it with a loop traversing $N$ elements in linear $O(N)$ time keeps the upper bound time complexity limited to $O(N \log N)$.

---

## 4. Non-recursive Algorithm: Using a Frequency Array
<video controls width="100%" preload="metadata">
    <source src="./visuals/videos/4-%20HashMap.mp4" type="video/mp4">
    <a href="./visuals/videos/4-%20HashMap.mp4">Watch the HashMap video</a>
</video>

### Pseudo code
```
Function iterative4FrequencyArray:
    Input: array A, integer N

    if N = 0 then return -1
    
    hash_map := empty hash table for counting
    
    for i := 0 to N - 1 step 1 do
        hash_map[A[i]] := hash_map[A[i]] + 1
        
        if hash_map[A[i]] > N / 2 then
            return i
            
    return -1
```

### Implementation with Python.
```python
def iterative4FrequencyArray(A):
    N = len(A)
    hash_map = {}
    
    for i in range(N):
        if A[i] in hash_map:
            hash_map[A[i]] += 1
        else:
            hash_map[A[i]] = 1
            
        if hash_map[A[i]] > N / 2:
            return i
            
    return -1
```

### Analysis
Time Complexity: Expected $O(N)$, Worst-case $O(N^2)$
We traverse all $N$ elements exactly one time. In a well-distributed hashmap, insertions, retrievals, and increment updates execute entirely in $O(1)$ expected constant time. Processing the $N$ elements linearly gives an aggregate required time bound to $O(N)$. If large scale repetitive hashing collisions occur, the hash chain iteration will degrade lookup to $O(N)$, hence leading to $O(N^2)$ complexity in the absolute worst-case scenario without a balanced self-adjusting structure.

---

## 5. Non-recursive Algorithm: Boyer-Moore Majority Vote Algorithm
<video controls width="100%" preload="metadata">
    <source src="./visuals/videos/5-%20BoyerMoore.mp4" type="video/mp4">
    <a href="./visuals/videos/5-%20BoyerMoore.mp4">Watch the BoyerMoore video</a>
</video>

### Pseudo code
```
Function iterative5BoyerMoore:
    Input: array A, integer N

    if N = 0 then return -1
    
    candidate := 0
    count := 0
    candidate_idx := -1
    
    for i := 0 to N - 1 step 1 do
        if count = 0 then
            candidate := A[i]
            candidate_idx := i
            count := 1
        else if A[i] = candidate then
            count := count + 1
        else
            count := count - 1
            
    total_count := 0
    for i := 0 to N - 1 step 1 do
        if A[i] = candidate then
            total_count := total_count + 1
            
    if total_count > N / 2 then
        return candidate_idx
        
    return -1
```

### Implementation with C language.
```c
#include <stdio.h>

int iterative5BoyerMoore(int A[], int N) {
    int candidate = 0;
    int count = 0;
    int candidate_idx = -1;

    for (int i = 0; i < N; i++) {
        if (count == 0) {
            candidate = A[i];
            candidate_idx = i;
            count = 1;
        } else if (A[i] == candidate) {
            count++;
        } else {
            count--;
        }
    }

    int total_count = 0;
    for (int i = 0; i < N; i++) {
        if (A[i] == candidate) {
            total_count++;
        }
    }

    if (total_count > N / 2) {
        return candidate_idx;
    }
    return -1;
}
```

### Analysis
Time Complexity: $O(N)$
The majority voting process traverses sequentially through the entire list of $N$ elements exactly twice (one pass for discovering the dominator algorithm candidate, and another independent sweep for verifying frequencies). Each array location implies minimal state check operations in $O(1)$ boundaries. Hence it operates strictly bound by a time complexity $O(N)$.

---

## 6. Recursive Algorithm: Divide and Conquer
<video controls width="100%" preload="metadata">
    <source src="./visuals/videos/6-%20DivideAndConquer.mp4" type="video/mp4">
    <a href="./visuals/videos/6-%20DivideAndConquer.mp4">Watch the DivideAndConquer video</a>
</video>

### Pseudo code
```
Structure Result: 
    integer index
    integer occurrences

Function countOccurrencesRange:
    Input: array A, candidate, start, end
    count := 0
    for i := start to end step 1 do
        if A[i] = candidate then
            count := count + 1
    return count

Function getDominatorRecursiveUtil:
    Input: array A, start, end
    Output: Result {index, occurrences}
    
    if start = end then
        return {start, 1}
        
    mid := start + (end - start) / 2
    
    leftRes := getDominatorRecursiveUtil(A, start, mid)
    rightRes := getDominatorRecursiveUtil(A, mid + 1, end)
    
    if leftRes.index != -1 and A[leftRes.index] = A[rightRes.index] then
        return {leftRes.index, leftRes.occurrences + rightRes.occurrences}
        
    leftCount := 0
    if leftRes.index != -1 then
        leftCount := countOccurrencesRange(A, A[leftRes.index], start, end)
        
    rightCount := 0
    if rightRes.index != -1 then
        rightCount := countOccurrencesRange(A, A[rightRes.index], start, end)
        
    if leftCount > (end - start + 1) / 2 then
        return {leftRes.index, leftCount}
    else if rightCount > (end - start + 1) / 2 then
        return {rightRes.index, rightCount}
        
    return {-1, 0}

Function recursive6DivideAndConquer:
    Input: array A, integer N
    if N = 0 then return -1
    res := getDominatorRecursiveUtil(A, 0, N - 1)
    return res.index
```

### Implementation with C language.
```c
#include <stdio.h>

typedef struct {
    int index;
    int count;
} Pair;

int countOccurrencesRange(int A[], int candidate, int start, int end) {
    int count = 0;
    for (int i = start; i <= end; i++) {
        if (A[i] == candidate) {
            count++;
        }
    }
    return count;
}

Pair getDominatorRecursiveUtil(int A[], int start, int end) {
    if (start == end) {
        Pair res = {start, 1};
        return res;
    }

    int mid = start + (end - start) / 2;
    Pair leftRes = getDominatorRecursiveUtil(A, start, mid);
    Pair rightRes = getDominatorRecursiveUtil(A, mid + 1, end);

    if (leftRes.index != -1 && rightRes.index != -1 && A[leftRes.index] == A[rightRes.index]) {
        Pair res = {leftRes.index, leftRes.count + rightRes.count};
        return res;
    }

    int leftCount = 0;
    if (leftRes.index != -1) {
        leftCount = countOccurrencesRange(A, A[leftRes.index], start, end);
    }

    int rightCount = 0;
    if (rightRes.index != -1) {
        rightCount = countOccurrencesRange(A, A[rightRes.index], start, end);
    }

    int size = end - start + 1;
    if (leftCount > size / 2) {
        Pair res = {leftRes.index, leftCount};
        return res;
    } else if (rightCount > size / 2) {
        Pair res = {rightRes.index, rightCount};
        return res;
    }

    Pair res = {-1, 0};
    return res;
}

int recursive6DivideAndConquer(int A[], int N) {
    if (N == 0) return -1;
    Pair res = getDominatorRecursiveUtil(A, 0, N - 1);
    return res.index;
}
```

### Analysis
Time Complexity: $O(N \log N)$
The recursion logic evenly divides the array space precisely into logical halves generating a recursion tree defining bounded $\log N$ depth frames. At each internal block, evaluating counts requires looping subsets in linear time bound $O(N)$ with `countOccurrencesRange()`. Hence evaluated strictly dynamically matching standard Master Theorem characteristics forms $T(N) = 2T(N/2) + O(N)$; resolving broadly to bounded $O(N \log N)$ complexity.

---

## Algorithm 4 vs. Recursive Algorithm Comparison

| Criteria | Algorithm 4: Using a Frequency Array | Algorithm 6: Divide and Conquer |
| :--- | :--- | :--- |
| **1- Algorithm Approach** | Iterative (Hash Map) | Recursive (Divide and Conquer) |
| **2- Time Complexity** | Expected $O(N)$, Worst-case $O(N^2)$ | $O(N \log N)$ |
| **3- Advantages** | <ul><li>Very fast average-case performance bounding to $O(N)$.</li><li>Simple code logic that translates easily across modern languages.</li></ul> | <ul><li>Guaranteed strict worst-case limits capping at $O(N \log N)$.</li><li>Does not suffer from hash-collision degradation vulnerabilities.</li></ul> |
| **4- Disadvantages** | <ul><li>Worst-case performance can degrade to $O(N^2)$ with severe hashing collisions.</li><li>Needs explicit allocation per unique element inducing overhead.</li></ul> | <ul><li>Recursive operations add sequential stack overhead limiting runtime performance.</li><li>Average mathematical cost of $O(N \log N)$ is slower than linear approaches.</li></ul> |
