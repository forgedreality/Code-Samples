#include <stdlib.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// use for constraining the input length
#define SIZE 26

// prototypes
int validateCipher(int len, string cipher);
char *toLower(char str[SIZE], size_t len);

int main(int argc, string argv[SIZE])
{
    // if no cipher supplied
    if (argv[1] == NULL || argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    // if the supplied cipher isn't the correct length
    if (strlen(argv[1]) != SIZE)
    {
        printf("Key must contain %i characters\n", SIZE);
        return 1;
    }

    // get the cipher to a string
    string c = argv[1];
    // get the length of the input
    size_t len = strlen(c);
    // convert the input cipher to lowercase to make comparisons easier
    // maybe not the right approach...?
    char *lc = toLower(c, len);

    // make sure the cipher has no duplicates and only contains alphabetical chars
    if (validateCipher(len, lc))
    {
        printf("Cipher \"%s\" is invalid.\n", c);
        return 1;
    }

    // get input message from user
    string input = get_string("plaintext: ");

    // get the length of the input message
    int ilen = strlen(input);
    // set up the output variable
    char output[ilen];
    // make sure we set the end flag in memory by inserting a null char at the end of this pointer
    output[ilen] = '\0';

    // iterate over the input
    for (int i = 0; i < ilen; i++)
    {
        // get current character
        char chr = input[i];
        // check if this character is uppercase or lowercase so we can output the correct case at the end
        int isUpper = chr >= 'A' && chr <= 'Z' ? 1 : 0;

        // lowercase the char so we can easily compare with the cipher
        chr = tolower(chr);
        // output a letter, or punctuation
        chr = chr - 97 >= 0 && chr - 97 <= 25 ? lc[chr - 97] : chr;
        // was the input character uppercase?  If so, return it as such.
        chr = isUpper ? toupper(chr) : chr;

        // set this character in the output array to our cipher result
        output[i] = chr;
    }

    // echo output
    printf("ciphertext: %s\n", output);
    // free memory
    free(lc);
    return 0;
}

// check whether or not the input cipher is valid
int validateCipher(int len, string cipher)
{
    for (int i = 0; i < len; i++)
    {
        char chr = cipher[i];
        // check for bad chars
        if (chr < 'A' || (chr > 'Z' && chr < 'a') || chr > 'z')
        {
            return 1;
        }

        for (int j = i + 1; j < len; j++)
        {
            // if there are duplicates, the cipher is invalid.  Exit out.
            if (cipher[i] == cipher[j])
            {
                return 1;
            }
        }
    }

    return 0;
}

// convert each input character to lowercase
char *toLower(char str[SIZE], size_t len)
{
    char *str_l = calloc(len + 1, sizeof(char));

    for (size_t i = 0; i < len; ++i)
    {
        str_l[i] = tolower((unsigned char)str[i]);
    }
    return str_l;
}