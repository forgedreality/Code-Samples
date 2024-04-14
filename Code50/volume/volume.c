// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "rb");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "wb");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    int16_t c;
    int counter = 0;
    while (fread(&c, sizeof(int16_t), 1, input))
    {
        c = counter < HEADER_SIZE ? c : c * factor;
        fwrite(&c, sizeof(int16_t), 1, output);
        counter++;
    }

    // Close files
    fclose(input);
    fclose(output);
}
