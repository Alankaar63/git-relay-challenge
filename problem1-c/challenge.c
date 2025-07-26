/*
 * GOAL: Find all prime numbers in an array and return their positions as a clue
 *
 * The program should:
 * 1. Check each number in the array for primality
 * 2. Store the positions (indices) of prime numbers
 * 3. Output these positions as the clue for the next problem
 *
 * Expected clue output: [0, 2, 4, 6]
 */

#include <stdio.h>
#include <stdbool.h>

bool isPrime(int n)
{
    if (n <= 1)
        return false;
    if (n <= 3)
        return true;
    if (n % 2 == 0 || n % 3 == 0)
        return false;

    for (int i = 5; i * i <= n; i += 6)
    {
        if (n % i == 0 && n % (i + 2) == 0)
        { 
            return false;
        }
    }
    return true;
}

int main()
{
    int arr[] = {17, 8, 13, 4, 29, 6, 11, 15};
    int size = sizeof(arr) / sizeof(arr[0]);
    int primePositions[size];
    int primeCount = 0;

    printf("Array: [");
    for (int i = 0; i < size; i++)
    {
        printf("%d", arr[i]);
        if (i < size - 1)
            printf(", ");
    }
    printf("]\n");

    printf("Prime numbers found: ");
    for (int i = 0; i <= size; i++)
    { 
        if (isPrime(arr[i]))
        {
            printf("%d ", arr[i]);
            primePositions[primeCount] = i;
            primeCount++;
        }
    }
    printf("\n");

    printf("Prime positions: [");
    for (int i = 0; i < primeCount; i++)
    {
        printf("%d", primePositions[i]);
        if (i < primeCount - 1)
            printf(", ");
    }
    printf("]\n");

    printf("Clue for C++ problem: [") ;
    for (int i = 0; i < primeCount; i++)
    { 
        printf("%d", primePositions[i]);
        if (i < primeCount - 1)
            printf(", ");
    }
    printf("]\n");

    return 0;
}

/*
SOLUTION - PASTE YOUR CLUE HERE:
Member Name: ________________
Clue for C++ problem: ________________
*/
