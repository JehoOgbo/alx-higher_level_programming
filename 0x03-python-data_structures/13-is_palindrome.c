#include "lists.h"

/**
 * reverse - reverses the order of elements in a listint_t list
 *
 * @head: pointer to a pointer to the first element of the list
 *
 * Return: pointer to the first element of the reversed list
 */
listint_t *reverse(listint_t **head)
{
	/* create a pointer to temporarily store addresses */
	/* create a  pointer to the first element of the new list */
	/* temporarily store the addresses in temp & */
	listint_t *prev;
	listint_t *next;

	prev = NULL;
	next = NULL;

	while (*head != NULL)
	{
		next = (*head)->next;	/*set to point to next node of list*/
		(*head)->next = prev;	/*set head next to prev address*/
		prev  = *head;	/* set prev address to head */
		*head = next;	/* set head to the next address */
	}
	*head = prev;	/* set head to prev address not null */
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is palindrome
 *
 * @head: pointer to the first node of the list
 * Return: 0 if no palindrome and 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *p, *q, *second;

	if (!(*head) || (*head)->next == NULL)
		return (1);
	if ((*head)->next->next == NULL)
	{
		if ((*head)->n != (*head)->next->n)
			return (0);
		else
			return (1);
	}
	p = *head;
	q = *head;
	while (q)  /* split the linked list in the middle */
	{
		p = p->next->next;
		if (p->next == NULL)  /* if odd forget the middle */
		{
			second = q->next;  /* make second linked list */
			break;
		}
		if (p->next->next == NULL)
		{
			second = q->next->next;
			break;
		}
		q = q->next;
	}
	second = reverse(&second);  /* reverse second linked list */
	q = *head;  /* set q back to the beginning */
	while (second->next)  /* while there is n value attached */
	{
		if (second->n != q->n)  /* check if the values are the same */
		{
			return (0);  /* return 0 for the same value */
		}
		second = second->next;  /* run along both linked lists */
		q = q->next;
	}
	return (1);
}
