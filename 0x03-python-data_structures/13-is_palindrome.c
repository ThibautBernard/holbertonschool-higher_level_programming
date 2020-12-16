#include "lists.h"
/**
 * lenth_linked_list - count length linked list
 * @head: head
 * Return: length
 */
int lenth_linked_list(listint_t *head)
{
	int length_linked = 0;

	while (head)
	{
		length_linked++;
		head = head->next;
	}
	return (length_linked);
}
/**
 * linked_into_array - transform linked list into array
 * @head: node
 * @length: length of the llinked list
 * Return: array
 **/
char *linked_into_array(listint_t *head, int length)
{
	char *array;
	int i = 0;

	array = malloc(sizeof(char) * length + 1);
	if (array == NULL)
		return (NULL);
	while (head)
	{
		array[i] = head->n;
		i++;
		head = head->next;
	}
	return (array);
}
/**
 * is_palindrome - check if linked list palindrome
 * @head: linked list
 * Return: 0 if not, 1 if are
 **/
int is_palindrome(listint_t **head)
{
	int length_linked, t = 0, i = 0, counter = 0;
	char *array;

	length_linked = lenth_linked_list(*head);
	if (length_linked == 0)
		return (1);
	array = linked_into_array(*head, length_linked);
	i = length_linked - 1;
	while (array[i] && i + 1 > length_linked / 2)
	{
		if (array[i] == array[t])
			counter++;
		i--;
		t++;
	}
	if (counter == length_linked / 2)
	{
		free(array);
		return (1);
	}
	free(array);
	return (0);
}
