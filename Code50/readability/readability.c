#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int main(void)
{
    string text = get_string("Text: ");
    int len = strlen(text);
    float letters = 0;
    float words = 0;
    float sentences = 0;

    for (int i = 0; i < len; i++)
    {
        char chr = toupper(text[i]);

        // 65 - 90 inclusive
        if (chr > 64 && chr < 91)
        {
            letters++;
        }

        // period, question mark, exclamation point
        else if (chr == 46 || chr == 63 || chr == 33)
        {
            if (i == len - 1)
            {
                words++;
            }

            sentences++;
        }

        // spaces
        else if (chr == 32 && text[i - 1] != 32)
        {
            words++;
        }
    }

    letters = letters / words * 100;
    sentences = sentences / words * 100;

    // L = letters per 100 words; S = sentences per 100 words
    int index = (int)rintf(0.0588 * letters - 0.296 * sentences - 15.8);

    printf(index < 1 ? "Before Grade 1\n" : index >= 16 ? "Grade 16+\n" : "Grade %i\n", index);

    return 0;
}