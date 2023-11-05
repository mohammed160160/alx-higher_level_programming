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
int element = 0, dif = 0, middle = 0;
listint_t *start, *lengthfinder;

if (head == NULL || *head == NULL) /*if the list is empty*/
{
	return (1);
}

start = *head;
lengthfinder = *head;

while (lengthfinder->next != NULL)
{
lengthfinder = lengthfinder->next;
length++;
}

int array[length];

for (e = 0; e < length; e++)
{
array[e] = start->n;
start = start->next;
}

middle = length / 2;

for (dif = 0; e < middle; e++)
{
if (array[dif] != arrays[length - (dif + 1)])
	{
	return (0);
	}
}
return (1);
}
