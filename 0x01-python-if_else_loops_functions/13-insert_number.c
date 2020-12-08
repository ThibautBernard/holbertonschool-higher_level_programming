#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert a new node in order sorted
 * @head: adress of the linked list
 * @number: number to add
 * Return: null or adress of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *actual, *next, *new_node;

	actual = *head;
	next = actual->next;
	new_node = malloc(sizeof(listint_t));
	if (actual->next == NULL)
	{
		new_node->next = actual->next;
		actual->next = new_node;
		new_node->n = number;
		return (new_node);
	}
	if (new_node == NULL)
		return (NULL);
	while (actual)
	{
		if (number < next->n)
		{
			new_node->next = actual->next;
			actual->next = new_node;
			new_node->n = number;
			return (new_node);
		}
		else if (next->next == NULL)
		{
			new_node->next = next->next;
			next->next = new_node;
			new_node->n = number;
			return (new_node);
		}
		actual = actual->next;
		next = next->next;
	}
	return (new_node);
}
