#include <Python.h>

/**
 * print_python_list_info - print python inputs in c
 * @p: OyObject list
 */
void print_python_list_info(PyObject *p)
{
	int size, space, x;
	PyObject *obj;

	size = Py_SIZE(p);
	space = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = 8\n", space);
	for (x = 0; x < size; x++)
	{
	printf("Element %d: ", x);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
