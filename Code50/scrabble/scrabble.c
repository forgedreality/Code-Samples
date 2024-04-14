#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    printf(score1 == score2 ? "Tie!\n" : "Player %i wins!\n", score1 > score2 ? 1 : 2);
    return 0;
}

int compute_score(string word)
{
    int len = strlen(word);
    int score = 0;
    for (int i = 0; i < len; i++)
    {
        int p = POINTS[toupper(word[i]) - 65];
        score += p < 26 && p >= 0 ? POINTS[toupper(word[i]) - 65] : 0;
    }

    return score;
}
