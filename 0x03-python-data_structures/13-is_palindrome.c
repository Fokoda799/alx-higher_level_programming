#include "lists.h"

/**
* is_palindrome - check if the list is a palindrome
* @head: pointer to the head of the linked list
* Return: 1 if the list is a palindrome, 0 otherwise
*/
int is_palindrome(listint_t **head)
{
listint_t *slow = *head, *fast = *head;
listint_t *second_half, *temp, *temp1;

if (*head == NULL || (*head)->next == NULL)
return (1);

/* Find the middle of the list */
while (fast && fast->next)
{
slow = slow->next;
fast = fast->next->next;
}

/* Reverse the second half of the list */
second_half = reverse(&(slow->next));
temp1 = *head;
temp = second_half;

/* Compare the first and second halves of the list */
while (temp && temp1)
{
if (temp->n != temp1->n)
{
/* Restore the original list and return 0 if not a palindrome */
reverse(&second_half);
return (0);
}
temp = temp->next;
temp1 = temp1->next;
}

/* Restore the original list */
reverse(&second_half);
return (1);
}

/**
* reverse - reverse a linked list
* @head: pointer to the head of the linked list
* Return: pointer to the new head of the reversed list
*/
listint_t *reverse(listint_t **head)
{
listint_t *prev = NULL, *current = *head, *next_node = NULL;

while (current != NULL)
{
next_node = current->next;
current->next = prev;
prev = current;
current = next_node;
}

*head = prev;
return (*head);
}

