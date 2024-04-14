#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <malloc.h>

int main(void)
{
    int spaces;
    int hashes;
    int h;

    do
    {
        h = get_int("Height: ");
    }
    while (h < 1 || h > 8);

    for (int i = 0; i < h; i++)
    {
        // set vars for number of hashes and leading spaces
        spaces = h - (i + 1);
        hashes = h - spaces;

        // print leading spaces
        while (spaces > 0)
        {
            printf(" ");
            spaces--;
        }

        int temp = hashes;

        // print hashes representing pyramid
        while (temp > 0)
        {
            printf("#");
            temp--;
        }

        // print gutter
        printf("  ");

        // print right side of pyramid
        while (hashes > 0)
        {
            printf("#");
            hashes--;
        }

        // start new row
        printf("\n");
    }
}