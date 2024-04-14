#include <cs50.h>
#include <stdio.h>
#include <math.h>

// sum digits of number provided
int addDigits(int num)
{
    int digit = 0;
    int totalDigits = log10(num) + 1;
    int output = 0;

    for (int i = 0; i < totalDigits; i++)
    {
        digit = num % 10;
        output += digit;
        num = num / 10;
    }
    return output;
}

// check if provided num is valid value
// num = number to search for; values = array of possible values
int checkValues(int num, int values[], int arrSize)
{
    for (int i = 0; i < arrSize; i++)
    {
        if (values[i] == num)
        {
            return 1;
        }
    }
    return 0;
}


int main(void)
{
    long c;
    int clen;
    // establish output variable
    string output = "INVALID\n";

    // get input from user for CC number
    c = get_long("Number: ");
    clen = log10(c) + 1;

    // valid CC lengths
    int lengths[] = {13, 15, 16};
    // get size of above array
    int len = sizeof(lengths) / sizeof(lengths[0]);
    if (checkValues(clen, lengths, len))
    {
        int count = 0;
        int sum = 0;
        long n = c;
        int total = 0;
        int temp;

        while (n > 0)
        {
            if (count % 2 != 0)
            {
                // get last ODD digit and multiply by 2
                temp = (n % 10) * 2;
                // sum the digits of the above operation and add to evens counter
                total += addDigits(temp);
            }
            else
            {
                // get the last EVEN digit
                temp = n % 10;
                // add digit to odds counter
                total += temp;
            }

            count++;
            // reduce the number we're evaluating by 1
            n = n / 10;
        }

        if (total % 10 == 0)
        {
            // get first 2 digits of given number
            int firstDigits = c / pow(10, clen - 2);

            // Amex - len: 15; Starts with: 34, 37
            // MC - len: 16; Starts with: 51, 52, 53, 54, 55
            // Visa - len 13, 16; Starts with: 4
            if (clen == 13 || clen == 16)
            {
                int validDigits[] = {4};
                len = sizeof(validDigits) / sizeof(validDigits[0]);

                // visa just starts with 4, so div our 2 digits by 10 to get the first digit (int value ignores decimal)
                if (checkValues(firstDigits / 10, validDigits, len))
                {
                    // valid Amex
                    output = "VISA\n";
                }
            }
            if (clen == 15)
            {
                int validDigits[] = {34,  37};
                len = sizeof(validDigits) / sizeof(validDigits[0]);

                if (checkValues(firstDigits, validDigits, len))
                {
                    // valid Amex
                    output = "AMEX\n";
                }
            }
            if (clen == 16)
            {
                int validDigits[] = {51, 52, 53, 54, 55};
                len = sizeof(validDigits) / sizeof(validDigits[0]);

                // if (checkValues(firstDigits, (const int []){51, 52, 53, 54, 55}, len))
                if (checkValues(firstDigits, validDigits, len))
                {
                    printf("Got here\n");
                    // valid MC
                    output = "MASTERCARD\n";
                }
            }
        }
    }
    printf("%s", output);
    return 0;
}