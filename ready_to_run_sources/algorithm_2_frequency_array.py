def iterative4FrequencyArray(A, N):
    frequency = {}
    
    for i in range(N):
        if A[i] in frequency:
            frequency[A[i]] += 1
        else:
            frequency[A[i]] = 1
            
        if frequency[A[i]] > N / 2:
            return i
            
    return -1

n = int(input())
arr = list(map(int, input().split()))

print(iterative4FrequencyArray(arr, n))