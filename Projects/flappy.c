// Flappy Bird
// Build from src directory with the following command:
// gcc -std=c17 flappy.c -ID:/msys64/mingw64/include -LD:/msys64/mingw64/lib -Wall -lmingw32 -lSDL2main -lSDL2 -o ..\build\flappy

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

#define WIDTH 80
#define HEIGHT 20

// Initial position of the bird
#define X_POSITION (WIDTH / 2)
#define Y_POSITION (HEIGHT / 2)

// Initial velocity of the bird
#define INITIAL_VELOCITY 0

// Gravity constant
#define GRAVITY 0.5

// Pipe constants
#define PIPE_GAP 5
#define PIPE_WIDTH 3
#define MIN_PIPE_HEIGHT 3
#define MAX_PIPE_HEIGHT (HEIGHT - PIPE_GAP - MIN_PIPE_HEIGHT)

char screen[HEIGHT][WIDTH];

struct Bird {
  int x;
  int y;
  double velocity;
};

struct Pipe {
  int x;
  int top_height;
  int bottom_height;
};

void update_screen(struct Bird *bird, struct Pipe *pipe) {
  for (int i = 0; i < HEIGHT; i++) {
    for (int j = 0; j < WIDTH; j++) {
      screen[i][j] = ' ';
    }
  }

  // Draw the bird
  screen[bird->y][bird->x] = '*';

  // Draw the pipe
  for (int i = 0; i < pipe->top_height; i++) {
    screen[i][pipe->x] = '|';
  }
  for (int i = pipe->top_height + PIPE_GAP; i < HEIGHT; i++) {
    screen[i][pipe->x] = '|';
  }
}

void print_screen() {
  for (int i = 0; i < HEIGHT; i++) {
    for (int j = 0; j < WIDTH; j++) {
      printf("%c", screen[i][j]);
    }
    printf("\n");
  }
}

void update_bird(struct Bird *bird) {
  // Update the bird's position
  bird->y += bird->velocity;
  bird->velocity += GRAVITY;

  // Make sure the bird stays within the screen
  if (bird->y < 0) {
    bird->y = 0;
  }
  if (bird->y >= HEIGHT) {
    bird->y = HEIGHT - 1;
  }
}

bool check_collision(struct Bird *bird, struct Pipe *pipe) {
  // Check if the bird has collided with the pipe
  if (bird->x == pipe->x && (bird->y <= pipe->top_height || bird->y >= pipe->top_height + PIPE_GAP)) {
    return true;
  }
  return false;
}

int main(int argc, char *argv[]) {
  srand(time(NULL));

  struct Bird bird = {
    .x = X_POSITION,
    .y = Y_POSITION,
  .velocity = INITIAL_VELOCITY
};

struct Pipe pipe = {
  .x = WIDTH - 1,
  .top_height = rand() % (MAX_PIPE_HEIGHT - MIN_PIPE_HEIGHT + 1) + MIN_PIPE_HEIGHT
};
pipe.bottom_height = HEIGHT - pipe.top_height - PIPE_GAP;

char input;
bool running = true;

while (running) {
  update_screen(&bird, &pipe);
  print_screen();

  // Update the pipe position
  pipe.x--;
  if (pipe.x < 0) {
    pipe.x = WIDTH - 1;
    pipe.top_height = rand() % (MAX_PIPE_HEIGHT - MIN_PIPE_HEIGHT + 1) + MIN_PIPE_HEIGHT;
    pipe.bottom_height = HEIGHT - pipe.top_height - PIPE_GAP;
  }

  // Update the bird
  update_bird(&bird);

  // Check for collision
  if (check_collision(&bird, &pipe)) {
    running = false;
  }

  printf("Press SPACE to flap, Q to quit: ");
  input = getchar();
  if (input == ' ') {
    bird.velocity = -3;
  }
  if (input == 'Q') {
    running = false;
  }
}

printf("Game Over!\n");

return 0;
}
