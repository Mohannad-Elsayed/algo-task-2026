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
    int result = iterative1Bruteforce((int *)A, N);
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
