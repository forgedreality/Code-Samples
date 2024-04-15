// Build from src directory with the following command:
// gcc -std=c17 starfield.c -ID:/msys64/mingw64/include -LD:/msys64/mingw64/lib -Wall -lmingw32 -lSDL2main -lSDL2 -o ..\build\starfield
#include <stdio.h>
#include <SDL2/SDL.h>
#include <stdlib.h>
#include <math.h>

// Window dimensions
const int WIDTH = 320;
const int HEIGHT = 200;

// The distance from the viewer to the plane
const int VIEWER_DISTANCE = 200;

// The distance between grid lines
const int GRID_SPACING = 10;


// Converts 3D coordinates to 2D screen coordinates using a perspective projection
void perspective_projection(int x, int y, int z, int* screen_x, int* screen_y, int viewer_distance, int tilt_angle) {
    // Calculate the projection of the 3D point onto the 2D screen
    float projection = (float)viewer_distance / (viewer_distance + z);
    *screen_x = (int)(x * projection);
    *screen_y = (int)(y * projection);
    // Tilt the plane by the specified angle
    *screen_x += (int)(*screen_y * tan(tilt_angle * M_PI / 180));
    printf("%d, %d\n", *screen_x, *screen_y);
}

int main(int argc, char* argv[]) {
    // Initialize SDL
    if (SDL_Init(SDL_INIT_VIDEO) != 0) {
        printf("Error initializing SDL: %s\n", SDL_GetError());
        return 1;
    }

    // Create the window
    SDL_Window* window = SDL_CreateWindow("Plane", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, WIDTH, HEIGHT, SDL_WINDOW_SHOWN);
    if (window == NULL) {
        printf("Error creating window: %s\n", SDL_GetError());
        SDL_Quit();
        return 1;
    }

    // Create the renderer
    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);
    if (renderer == NULL) {
        printf("Error creating renderer: %s\n", SDL_GetError());
        SDL_DestroyWindow(window);
        SDL_Quit();
        return 1;
    }

    // Set the renderer color to white
    SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);

    // Main loop
    int quit = 0;
    while (!quit) {
        // Clear the screen
        SDL_RenderClear(renderer);

        // Draw the plane
        for (int y = 0; y < HEIGHT/2; y++) {
            for (int x = 0; x < WIDTH; x++) {
                // Calculate the 3D coordinates of the current point
                int z = 0;
                // Convert the 3D coordinates to 2D screen coordinates
                int screen_x, screen_y;
                perspective_projection(x, y, z, &screen_x, &screen_y, VIEWER_DISTANCE, 45);
                // Draw a line from the current point to the point to the right of it
                SDL_RenderDrawLine(renderer, screen_x, screen_y, screen_x + 10, screen_y);
            }
        }

        // Draw the grid lines
        for (int y = 0; y < HEIGHT/2; y += GRID_SPACING) {
            for (int x = 0; x < WIDTH; x += GRID_SPACING) {
                // Calculate the 3D coordinates of the current point
                int z = 0;
                // Convert the 3D coordinates to 2D screen coordinates
                int screen_x, screen_y;
                perspective_projection(x, y, z, &screen_x, &screen_y, VIEWER_DISTANCE, 45);
                // Draw a line from the current point to the point to the right of it
                SDL_RenderDrawLine(renderer, screen_x, screen_y, screen_x + GRID_SPACING, screen_y);
                // Draw a line from the current point to the point below it
                SDL_RenderDrawLine(renderer, screen_x, screen_y, screen_x, screen_y + GRID_SPACING);
            }
        }

        // Update the screen
        SDL_RenderPresent(renderer);

        // Check for events
        SDL_Event event;
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                quit = 1;
            }
        }
    }

    // Clean up
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}