#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - inserts a node with the value stored in the variable "number"
 * @head: A pointer to the first node of the linked list
 * @number: The number that will be added in the new node
 * Return: The address of the new node or 0
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *node, *current;

if (head == NULL) /*if the list is empty*/
{ return (NULL); }

node = malloc(sizeof(listint_t));
if (node == NULL)
{ return (NULL); }

node->n = number;
node->next = NULL;

if (*head == NULL) /*If the pointer to head is NULL*/
{
*head = node;
return (*head);
}

current = *head;

if (number <= current->n)/*Placing the number at the start of the list*/
{
node->next = current;
*head = node;
return(*head);
}	


return (node);
}
