// Implements a dictionary's functionality

#include <ctype.h>
#include <stdio.h>
#include <stdbool.h>
#include <strings.h>
#include <string.h>
#include <stdlib.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// void print_tree(node *root);

// Choose number of buckets in hash table
// first three characters, means AAA = [0][0][0]
const unsigned int N = 26 * 26 * 26;

// Hash table
node *table[N] = {NULL};

// keep track of dictionary size
unsigned int dictCount = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    unsigned int h = hash(word);
    node *root = table[h];

    while (root != NULL)
    {
        if (strcasecmp(root -> word, word) == 0)
        {
            return true;
        }
        root = root -> next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned int h = 0;
    int l = strlen(word);

    for (int i = 0; i < l; i++)
    {
        // hash based on the first three characters
        // more space, but more speed also
        if (i == 3 || strcmp(&word[i], "\0") == 0)
        {
            break;
        }

        // calculate where the word should go, while separating alphabetical characters from punctuation
        h += (unsigned int)(isalpha(word[i]) != 0 ? 1 : (toupper(word[i]) - 65)) * (i == 0 ? 26 * 26 : i == 1 ? 26 : 1);
    }
    return h;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Try to open dictionary
    FILE *dict = fopen(dictionary, "r");
    if (dict == NULL)
    {
        printf("Could not open %s.\n", dictionary);
        unload();
        return false;
    }

    // Load each word into hash table
    char foundWord[LENGTH + 1];
    // while (fread(&c, sizeof(char), 1, dict))

    while (fscanf(dict, "%s", foundWord) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            printf("Not enough memory to create node %s.\n", foundWord);
            return false;
        }

        strcpy(n -> word, foundWord);

        unsigned int pos = hash(foundWord);

        n -> next = table[pos] == NULL ? NULL : table[pos];
        table[pos] = n;

        dictCount++;
    }

    fclose(dict);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return dictCount;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        while (table[i] != NULL)
        {
            node *n = table[i];
            table[i] = table[i] -> next;
            free(n);
        }
    }
    return true;
}
