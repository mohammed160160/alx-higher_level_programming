#include <Python.h>

/**
 * print_python_list - print python inputs in c
 * @p: OyObject list
 */
void print_python_list(PyObject *p);
{
	int size, space, x;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	space = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", space);

	for (x = 0; x < size; x++)
	{
		type = list->ob_item[x]->ob_type->ob_name;
		printf("Element %d: %s\n", x, type);
		if (strcmp(type, "bytes") == 0)
		{ print_python_bytes(list->ob_item[x]); }
	}
}

/**
 * print_python_bytes - print python inputs in c
 * @p: OyObject list
 */

void print_python_bytes(PyObject *p)
{
	unsigned char i, size;
	long int stringsize;

	PyBytesObject *bytes = (PyListObject *)p;

	stringsize = ((PyVarObject *)p)->ob_size;

	printf("[.] Python list info\n");
	if (strcmp(o->ob_type->tp_name, "bytes") != 0)
	{
	printf("  [ERROR] Invalid Bytes Object\n");
	return;
	}

	printf("  size: %ld\n", stringsize);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (stringsize > 10)
	{ size = 10; }
	else
	{ size = stringsize + 1; }

	printf("  first %d bytes: ", size);

	for (i = 0; i < size; i++)
	{
	printf("%02hhx", bytes->ob_sval[i])
		if (i == size - 1)
		{ printf("\n"); }
		else
		{ printf(" "); }
	}
}













}
