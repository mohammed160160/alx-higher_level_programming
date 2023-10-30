#include "lists.h"

/**
 * check_cycle - function that checks if there's a loop in the program.
 * @list:A pointer to the first element of the list
 * Return: 1 if there's a loop otherwise 0
 */

int check_cycle(listint_t *list)
{
listint_t *X = list;
listint_t *Y = list;

if (X == NULL || Y == NULL)
{
	return (0);
}

while (X != NULL && Y != NULL && Y->next != NULL)
{
X = X->next;
Y = Y->next->next;

	if (X == Y)
	{
	return (1);
	}
}

return (0);
}
