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

## 2. Non-recursive Algorithm: Using a Frequency Array
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

## 3. Recursive Algorithm: Divide and Conquer
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
### Time Complexity Analysis

**Time Complexity:** $O(N \log N)$

The recursion logic evenly divides the array space precisely into logical halves, generating a recursion tree defining bounded $\log N$ depth frames. At each internal block, evaluating counts requires looping subsets in linear time bound $O(N)$ with `countOccurrencesRange()`. Hence, evaluated strictly dynamically matching standard Master Theorem characteristics, this forms the recurrence relation:

$$T(N) = 2T(N/2) + O(N)$$

---

$$T(N) = aT(N/b) + f(N)$$

* $a = 2$
* $b = 2$
* $f(N) = O(N) = \Theta(N^c)$ where $c = 1$

leaf-growth factor $\log_b a$:
$$\log_b a = \log_2 2 = 1$$

Comparing the non-recursive work exponent ($c$) to $\log_b a$:
$$c = \log_b a \quad (1 = 1)$$

**Case 2** of the Master Theorem. Evaluates to:
$$T(N) = \Theta(N^{\log_b a} \log N) = \Theta(N^1 \log N)$$

Thus, the final complexity resolves broadly to bounded $O(N \log N)$.

---

## Algorithm 2 vs. Recursive Algorithm Comparison

| Criteria | Algorithm 2: Using a Frequency Array | Algorithm 4: Divide and Conquer |
| :--- | :--- | :--- |
| **1- Algorithm Approach** | Iterative (Hash Map) | Recursive (Divide and Conquer) |
| **2- Time Complexity** | Expected $O(N)$, Worst-case $O(N^2)$ | $O(N \log N)$ |
| **3- Advantages** | <ul><li>Very fast average-case performance bounding to $O(N)$.</li><li>Simple code logic that translates easily across modern languages.</li></ul> | <ul><li>Guaranteed strict worst-case limits capping at $O(N \log N)$.</li><li>Does not suffer from hash-collision degradation vulnerabilities.</li></ul> |
| **4- Disadvantages** | <ul><li>Worst-case performance can degrade to $O(N^2)$ with severe hashing collisions.</li><li>Needs explicit allocation per unique element inducing overhead.</li></ul> | <ul><li>Recursive operations add sequential stack overhead limiting runtime performance.</li><li>Average mathematical cost of $O(N \log N)$ is slower than linear approaches.</li></ul> |
