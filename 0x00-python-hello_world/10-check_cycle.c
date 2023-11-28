#include "lists.h"


int check_cycle(listint_t *list)
{
	listint_t *tree = list;
	listint_t *one = list;

	while(tree != NULL && tree->next != NULL && tree->next->next != NULL)
	{
		tree = tree->next->next->next;
		one = one->next;
		if (tree == one || tree->next == one)
			return (1);
	}
	return (0);
}
