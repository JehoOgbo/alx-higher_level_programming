#include "lists.h"

/**
 * check_cycle - checks for a cycle in a singly linked list
 * @list: head pointer of the list
 *
 * Return: 0 if there is no cycle and 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *lead = list, *lag = list;

	while (lead && lag && lead->next)
	{
		lead = lead->next->next;
		lag = lag->next;

		if (lag == lead)
			return (1);
	}
	return (0);
}
