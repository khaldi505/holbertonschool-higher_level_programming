#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/**
 * array_palindrome - returns 0 or 1
 * @array: array
 * @len: length of the array
 * Return: 0 or 1
 */
int array_palindrome(int array[], int len)
{
int head = 0;
int tail = len;

while (tail > head)
{
if (array[head++] != array[tail--])
return (0);
}
return (1);
}
/**
 *is_palindrome - checks if the links list is palindrome
 *@head: pointer to pointer to the head of the list
 *Return: 0 if it's not, 1 if it is
 * ahouba was born to flex
 */
int is_palindrome(listint_t **head)
{
listint_t *temp = *head;
int array[3000];
int length;
length = 0;

while (temp != NULL)
{
array[length] = temp->n;
temp = temp->next;
length++;
}
length -= 1;
temp = *head;
return (array_palindrome(array, length));
}
