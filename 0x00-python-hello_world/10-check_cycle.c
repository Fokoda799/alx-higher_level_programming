#include "lists.h"

/**
* check_cycle - check if linked list has a cycel.
* @list: linked list header.
* Return: 1 if it has a cycle, 0 if not.
*/
int check_cycle(listint_t *list)
{
	listint_t *tree = list;
	listint_t *one = list;

	while (tree != NULL && tree->next != NULL && tree->next->next != NULL)
	{
		tree = tree->next->next->next;
		one = one->next;
		if (tree == one || tree->next == one)
			return (1);
	}
	return (0);
}
