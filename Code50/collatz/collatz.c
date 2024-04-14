// Collatz Conjecture
// if n is 1, stop
// otherwise, if n is even repeat on n/2
// otherwise if n is odd, repeat on 3n + 1

#include <stdio.h>

int collatz(int n);

int main()
{
    int n = 0;
    while (n < 1)
    {
        printf("Enter a positive number: ");
        scanf("%d", &n);
    }

    printf("%i steps to get back to 1.\n", collatz(n));

    return 0;
}

int collatz(int n)
{
    if (n == 1)
        return 0;

    return 1 + (n % 2 == 0 ? collatz((n/2)) : collatz((3 * n + 1)));
}