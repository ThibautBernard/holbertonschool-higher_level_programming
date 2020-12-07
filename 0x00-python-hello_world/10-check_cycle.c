#include "lists.h"

/**
 * check_cycle - check if there is a loop
 * @list: the linked list
 * Return: 0 if not, 1 if there is a loop
 */
int check_cycle(listint_t *list)
{
	listint_t *fast;

	fast = list;
	while (list && fast && fast->next->next)
	{
		if (list == fast->next->next)
			return (1);
		list = list->next;
		fast = fast->next->next;
	}
	return (0);
}
