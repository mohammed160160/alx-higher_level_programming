#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - prints all elements of a listint_t list
 * @head: pointer to head of list
 * Return: 1 if palindrome 0 if else
 */

int is_palindrome(listint_t **head)
{
int e = 0, dif = 0, length = 0;
listint_t *start, *lengthfinder;

if (head == NULL || *head == NULL)
{
	return (1);
}

start = *head;
lengthfinder = *head;

while (lengthfinder != NULL)
{
length++;
lengthfinder = lengthfinder->next;
}

int *array;

array = malloc(length *sizeof(int));

for (e = 0; e < length; e++)
{
array[e] = start->n;
start = start->next;
}

for (dif = 0; dif < (length / 2); dif++)
{
	if (array[dif] != array[length - (dif + 1)])
	{
	free(array);
	return (0);
	}
}

free(array);
return (1);
}
