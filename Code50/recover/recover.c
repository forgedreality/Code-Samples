#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // if single argument not supplied
    if (argv[1] == NULL || argc != 2)
    {
        printf("Usage: %s raw_file\n", argv[0]);
        return 1;
    }

    // Remember filenames
    char *infile = argv[1];

    // Open input file
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        printf("Could not open %s.\n", infile);
        return 1;
    }

    // to keep track of the total matched
    int patternCount = 0;
    // to hold the filename
    char *fname;
    fname = malloc(8);
    FILE *img = NULL;

    int bSize = 512;
    unsigned char chunk[bSize];

    // search pattern
    unsigned char sig[] = {0xff, 0xd8, 0xff, 0xe0};
    // (chunk[3] & 0xf0 == sig[3]) -- bitwise operator to check fourth byte

    // while (!feof(inptr))
    while ((fread(chunk, sizeof(char), bSize, inptr) == bSize))
    {
        if (chunk[0] == sig[0] && chunk[1] == sig[1] && chunk[2] == sig[2] && (chunk[3] & 0xf0) == sig[3])
        {
            // set filename
            sprintf(fname, "%03i.jpg", patternCount);
            // close any previously opened files
            if (img != NULL)
            {
                fclose(img);
            }
            // create file to open
            img = fopen(fname, "w");
            patternCount++;
        }
        if (patternCount > 0)
        {
            fwrite(chunk, bSize, 1, img);
        }
    }

    fclose(inptr);
    fclose(img);
    free(fname);

    return 0;
}