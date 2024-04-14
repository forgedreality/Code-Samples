#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *x = malloc(3 * sizeof(int));
    if (x == NULL) return 1;

    x[0] = 73;
    x[1] = 74;
    x[2] = 33;

    free(x);
}