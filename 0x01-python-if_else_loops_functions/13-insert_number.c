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
	listint_t *node, *ptr;
	int i = 0;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;

	if (head == NULL)
		return (NULL);
	ptr = *head;
	if (ptr == NULL)
	{
		node->next = NULL;
		ptr = node;
	}
	while (ptr->next != NULL)
	{
		if (number < ptr->next->n || number < ptr->n)
		{
			if (i == 0)
			{
				node->next = *head;
				*head = node;
				break;
			}
			node->next = ptr->next;
			ptr->next = node;
			break;
		}
		ptr = ptr->next;
		i++;
	}
	if (ptr->next == NULL)
	{
		node->next = NULL;
		ptr->next = node;
	}
	return (node);
}
