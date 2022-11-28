#include "lists.h"

/**
 * check_cycle - check a listint_t list for existence of a cycle
 * @list: head pointer of the list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *lead;

	if (!list)
		return (0);

	/* go through list & compare each pointer with all after it */
	/* if they are the same, return 1 */
	while (list->next)
	{
		lead = list->next;
		while (lead->next)
		{
			if (lead->next == list->next)
				return (1);
			lead = lead->next;
		}
		list = list->next;
	}
	/* if the end of the list is reached, return 0 */
	return (0);
}
