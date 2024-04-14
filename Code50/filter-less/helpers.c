#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "helpers.h"

int min(int a, int b)
{
    return a > b ? b : a;
}

int max(int a, int b)
{
    return a > b ? a : b;
}

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    double avg;
    for (int y = 0; y < height; y++)
    {
        for (int x = 0; x < width; x++)
        {
            avg = round(((double)image[y][x].rgbtRed + (double)image[y][x].rgbtGreen + (double)image[y][x].rgbtBlue) / 3);
            image[y][x].rgbtRed = image[y][x].rgbtGreen = image[y][x].rgbtBlue = avg;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp;

    for (int y = 0; y < height; y++)
    {
        for (int x = 0; x < width / 2; x++)
        {
            temp = image[y][x];
            image[y][x] = image[y][(width - 1) - x];
            image[y][(width - 1) - x] = temp;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // int sep = 20;
    // grayscale(height, width, image);
    float sepiaRed;
    float sepiaGreen;
    float sepiaBlue;

    float r;
    float g;
    float b;

    for (int y = 0; y < height; y++)
    {
        for (int x = 0; x < width; x++)
        {
            r = image[y][x].rgbtRed;
            g = image[y][x].rgbtGreen;
            b = image[y][x].rgbtBlue;

            sepiaRed = .393 * r + .769 * g + .189 * b;
            sepiaGreen = .349 * r + .686 * g + .168 * b;
            sepiaBlue = .272 * r + .534 * g + .131 * b;

            sepiaRed = sepiaRed <= 255 ? sepiaRed : 255;
            sepiaGreen = sepiaGreen <= 255 ? sepiaGreen : 255;
            sepiaBlue = sepiaBlue <= 255 ? sepiaBlue : 255;

            image[y][x].rgbtRed = round(sepiaRed);
            image[y][x].rgbtGreen = round(sepiaGreen);
            image[y][x].rgbtBlue = round(sepiaBlue);

            // image[y][x].rgbtRed += (r + sep <= 255 ? sep : abs(r - 255));
        }
    }

    return;
}

// Blur image
void getAvg(RGBTRIPLE *avg, int pos[2], int height, int width, RGBTRIPLE image[height][width])
{
    // initialize rgb values with current pixel
    float r = (float)avg -> rgbtRed;
    float g = (float)avg -> rgbtGreen;
    float b = (float)avg -> rgbtBlue;

    // check in all directions, ignoring current pixel, since we already started with it above
    int dirs[8][2] =
    {
        {-1, -1}, {-1, 0}, {-1, 1},
        {0, -1}, {0, 1},
        {1, -1}, {1, 0}, {1, 1}
    };

    // keep a record of the valid (in-bounds) directions
    float dirsToCheck = 1;

    for (int i = 0; i < 8; i++)
    {
        // if the direction to look is in-bounds...
        if (pos[0] + dirs[i][0] >= 0 && pos[0] + dirs[i][0] < height &&
            pos[1] + dirs[i][1] >= 0 && pos[1] + dirs[i][1] < width
           )
        {
            // we found a valid pixel, so increment our total number checked
            dirsToCheck++;

            // add the current direction to the current pixel
            r += image[pos[0] + dirs[i][0]][pos[1] + dirs[i][1]].rgbtRed;
            g += image[pos[0] + dirs[i][0]][pos[1] + dirs[i][1]].rgbtGreen;
            b += image[pos[0] + dirs[i][0]][pos[1] + dirs[i][1]].rgbtBlue;
        }
    }

    // calculate averages based on total directions checked
    r = min(max(round(r /= dirsToCheck), 0), 255);
    g = min(max(round(g /= dirsToCheck), 0), 255);
    b = min(max(round(b /= dirsToCheck), 0), 255);

    // update our new averaged pixel
    avg -> rgbtRed = r;
    avg -> rgbtGreen = g;
    avg -> rgbtBlue = b;

    return;
}

void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // used for calculating average pixel
    RGBTRIPLE avg;

    // set up a temp pixel matrix so our calculations are based on the original image
    RGBTRIPLE temp[height][width];

    // save a new copy of image as temp per color.
    for (int y = 0; y < height; y++) //Loop for height of image.
    {
        for (int x = 0; x < width; x++) //Loop for width of image and save color values in temp.
        {
            temp[y][x] = image[y][x];
        }
    }


    // iterate over the image
    for (int y = 0; y < height; y++)
    {
        for (int x = 0; x < width; x++)
        {
            // record the current position so we can pass it to our average function
            int pos[] = {y, x};
            // get the rgb values from the current pixel
            avg = image[y][x];

            // update the averaged rgb values for the current and the surrounding pixels
            getAvg(&avg, pos, height, width, image);

            // set the averaged values for this current pixel in our temp matrix
            temp[y][x] = avg;
        }
    }

    for (int y = 0; y < height; y++)
    {
        for (int x = 0; x < width; x++)
        {
            // iterate over the original image and copy in our averaged values
            image[y][x].rgbtGreen = temp[y][x].rgbtGreen;
            image[y][x].rgbtBlue = temp[y][x].rgbtBlue;
            image[y][x].rgbtRed = temp[y][x].rgbtRed;
        }
    }

    return;
}

// Detect edges
void findEdge(RGBTRIPLE *temp, int pos[2], int height, int width, RGBTRIPLE image[height][width])
{
    // set up edge detection kernel
    int G[3][3] =
    {
        {-1, 0, 1},
        {-2, 0, 2},
        {-1, 0, 1}
    };

    // this one is not necessary, as it is just rotated 90 degrees to the first
    // int Gy[3][3] =
    // {
    //     {-1, -2, -1},
    //     { 0,  0,  0},
    //     { 1,  2,  1}
    // };

    // store in-bounds check just to simplify the if statement
    int isInBounds;
    int cmp;

    // set up floats for rgb values to prevent imprecision caused by ints
    float rx = 0;
    float gx = 0;
    float bx = 0;

    float ry = 0;
    float gy = 0;
    float by = 0;

    for (int h = 0; h < 3; h++)
    {
        cmp = (pos[0] - 1) + h;
        isInBounds = (cmp >= 0 && cmp < height) ? 1 : 0;
        if (isInBounds)
        {
            for (int w = 0; w < 3; w++)
            {
                cmp = (pos[1] - 1) + w;
                isInBounds = (cmp >= 0 && cmp < width) ? 1 : 0;
                if (isInBounds)
                {
                    // calculate products of surrounding pixel RGB values horizontally
                    rx += image[(pos[0] - 1) + h][(pos[1] - 1) + w].rgbtRed * G[h][w];
                    gx += image[(pos[0] - 1) + h][(pos[1] - 1) + w].rgbtGreen * G[h][w];
                    bx += image[(pos[0] - 1) + h][(pos[1] - 1) + w].rgbtBlue * G[h][w];

                    // ...and vertically
                    ry += image[(pos[0] - 1) + h][(pos[1] - 1) + w].rgbtRed * G[w][h];
                    gy += image[(pos[0] - 1) + h][(pos[1] - 1) + w].rgbtGreen * G[w][h];
                    by += image[(pos[0] - 1) + h][(pos[1] - 1) + w].rgbtBlue * G[w][h];

                    // temp is a pointer to the current pixel
                    // calculate its color based on the surrounding pixels
                    temp -> rgbtRed = (int)min(round(sqrtf(pow(ry, 2) + pow(rx, 2))), 255);
                    temp -> rgbtGreen = (int)min(round(sqrtf(pow(gy, 2) + pow(gx, 2))), 255);
                    temp -> rgbtBlue = (int)min(round(sqrtf(pow(by, 2) + pow(bx, 2))), 255);
                }
            }
        }
    }

    return;
}

// check for pixel contrast
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    // set up a temp pixel matrix so our calculations are based on the original image
    RGBTRIPLE timage[height][width];
    RGBTRIPLE temp;
    int pos[2] = {0};

    // blur(height, width, image);

    for (int y = 0; y < height; y++)
    {
        for (int x = 0; x < width; x++)
        {
            temp = image[y][x];
            pos[0] = y;
            pos[1] = x;


            findEdge(&temp, pos, height, width, image);

            timage[y][x] = temp;
        }
    }


    // for (int y = 0; y < height; y++)
    // {
    //     for (int x = 0; x < width; x++)
    //     {
    //         int pos[] = {y, x};

    //         temp[y][x] = findEdge(pos, height, width, temp);
    //     }
    // }

    for (int y = 0; y < height; y++)
    {
        for (int x = 0; x < width; x++)
        {
            image[y][x] = timage[y][x];
        }
    }

    return;
}
