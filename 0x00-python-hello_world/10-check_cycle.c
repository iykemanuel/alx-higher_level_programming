#include "lists.h"

/**
 * check_cycle - checks for a loop in a linked list
 * @list: points to beginning of list
 * Return: 0 if no cycle, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *snail, *cheetah;

	snail = list;
	cheetah = list;
	while (snail && cheetah && cheetah->next)
	{
		cheetah = cheetah->next->next;
		snail = snail->next;
		if (snail == cheetah)
			return (1);
	}
	return (0);
}
