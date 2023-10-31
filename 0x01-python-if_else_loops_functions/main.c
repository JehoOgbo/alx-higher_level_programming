#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "lists.h"

int main(void)
{
	listint_t *head;

	head = NULL;
	print_listint(head);

	printf("--------------------\n");

	insert_node(&head, 972);

	print_listint(head);

	free_listint(head);

	return (0);
}
