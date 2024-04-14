#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
}
node;

int main(void)
{
    // List of size
    node *list = NULL;

    // Add a number to list
    node *n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }

    n -> number = 1;
    n -> next = NULL;

    // Update list to point to new node
    list = n;

    // Add a number to list
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        free(list);
        return 1;
    }
    n -> number = 2;
    n -> next = NULL;
    // Add new node to linked list
    list -> next = n;

    // Add a number to list
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        free(list -> next);
        free(list);
        return 1;
    }
    n -> number = 3;
    n -> next = NULL;
    list -> next -> next = n;

    // Print numbers
    for (node *tmp = list; tmp != NULL; tmp = tmp -> next)
    {
        printf("%i\n", tmp -> number);
    }

    // Free list
    while (list != NULL)
    {
        // Create temp pointer to store new address
        node *tmp = list -> next;
        // Since we've moved the pointer, we can now free the old list address
        free(list);
        // Update address stored at list
        list = tmp;
        // Keep iterating until the node we're at is null, meaning we're at the last one in the linked list
    }
    return 0;
}