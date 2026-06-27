// C-2: Singly linked list of int with malloc/free. See ../c.md for the full task.
// prepend allocates a new node with malloc, stores the given value, links it before the current head, and returns the new 
// head, while free_list traverses the list, saving the next pointer before freeing each node to avoid memory leaks and use-after-free errors.
//
// Graded with: gcc -Wall -Wextra -fsanitize=address -g -o linkedlist c/linkedlist.c && ./linkedlist

#include <stdio.h>
#include <stdlib.h>

// TODO: define a node struct holding an int value and a pointer to the next node.
struct Node {
    int value;
    struct Node* next;
};
// TODO: node *prepend(node *head, int value)
//       allocate a new node with malloc, store value, link it at the front,
//       and return the new head.
struct Node* prepend(struct Node *head, int value){
    struct Node* n = malloc(sizeof(struct Node));
    n->value = value;
    n->next = head;
    return n;
}

// TODO: a function that prints the list in order (e.g. "3 -> 2 -> 1").
void printLinkedList(struct Node *head){
    while(head != NULL){
    printf("%d \n", head->value);
    head = head->next;
    }
    
}
// TODO: void free_list(node *head)  — free every node, leak-free.
void free_list(struct Node *head){
    struct Node* next = head->next;
    while(next != NULL){
        free(head);
        head = next;
        next = head->next;
        }
    free(head);
}

int main(void)
{
    // TODO: starting from an empty list, use prepend to build 3 -> 2 -> 1,
    // print it, then free the whole list.
    struct Node* head = NULL;
    head = prepend(head, 1);
    head = prepend(head, 2);
    head = prepend(head, 3);

    printLinkedList(head);
    free_list(head);
    return 0;
}
