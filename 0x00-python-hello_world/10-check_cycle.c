#include "lists.h"

/**
 * check_cycle - check if there is a loop
 * @list: the linked list
 * Return: 0 if not, 1 if there is a loop
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = list;
	fast = list;
	while (fast->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
