#include "lists.h"
#include <stdio.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: head node of the list; points to first element
 * @number: number to be added to the list
 *
 * Return: the address of the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *new = *head;

	if (!(*head))
	{
		printf("Good");
		return (NULL);
	}
	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;

	while (new)
	{
		if (number < new->next->n)
		{
			node->next = new->next;
			new->next = node;
			break;
		}
		if (number < new->n)
		{
			new = node;
			node = new;
			break;
		}
		new = new->next;
	}
	return (node);
}
