#include <stdio.h>

typedef struct {
    int index;
    int count;
} Result;

int countOccurrencesRange(int A[], int candidate, int start, int end) {
    int count = 0;
    for (int i = start; i <= end; i++) {
        if (A[i] == candidate) {
            count++;
        }
    }
    return count;
}

Result getDominatorRecursiveUtil(int A[], int start, int end) {
    if (start == end) {
        Result res = {start, 1};
        return res;
    }

    int mid = start + (end - start) / 2;
    Result leftRes = getDominatorRecursiveUtil(A, start, mid);
    Result rightRes = getDominatorRecursiveUtil(A, mid + 1, end);

    if (leftRes.index != -1 && rightRes.index != -1 && A[leftRes.index] == A[rightRes.index]) {
        Result res = {leftRes.index, leftRes.count + rightRes.count};
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
        Result res = {leftRes.index, leftCount};
        return res;
    }
    if (rightCount > size / 2) {
        Result res = {rightRes.index, rightCount};
        return res;
    }

    Result res = {-1, 0};
    return res;
}

int iterative4DivideAndConquer(int A[], int N) {
    if (N == 0) {
        return -1;
    }

    Result res = getDominatorRecursiveUtil(A, 0, N - 1);
    return res.index;
}

void printArray(const int A[], int N) {
    printf("[");
    for (int i = 0; i < N; i++) {
        printf("%d", A[i]);
        if (i < N - 1) {
            printf(", ");
        }
    }
    printf("]");
}

void runCase(const int A[], int N, int caseNumber) {
    int result = iterative4DivideAndConquer((int *)A, N);
    printf("Case %d\n", caseNumber);
    printf("Array: ");
    printArray(A, N);
    printf("\n");

    if (result != -1) {
        printf("Result: dominator index = %d, value = %d\n", result, A[result]);
    } else {
        printf("Result: no dominator\n");
    }

    printf("\n");
}

int main(void) {
    const int case1[] = {3, 4, 3, 2, 3, -1, 3, 3};
    const int case2[] = {1, 2, 3, 4, 5};
    const int case3[] = {2, 2, 2, 2, 1, 3};

    runCase(case1, sizeof(case1) / sizeof(case1[0]), 1);
    runCase(case2, sizeof(case2) / sizeof(case2[0]), 2);
    runCase(case3, sizeof(case3) / sizeof(case3[0]), 3);

    return 0;
}
