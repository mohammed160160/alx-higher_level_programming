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
int length = 0, checker = 0;
listint_t *start, *end, *newend;

if (head == NULL) /*if the list is empty*/
{ return (1); }

start = *head;
end = *head;

while (end->next != NULL)
{
length++;
end = end->next;
}

for (checker = 0; checker >= (length / 2); checker++)
{
if (start->n != end->n)
{
return (0);
}
start = start->next;
newend = *head;
while (newend->next != end)
{
newend = newend->next;
}

end = newend;
}

return (1);
}
