#include <stdio.h>
extern struct timespec *ts;  /* removes unwanted error gives betty warning */
#include "Python.h"  /* so it gets the type PyObject */

/**
 * print_python_list_info - prints information about a list
 * @list: a list of type PyObject which must be casted to a PyListObject
 *
 * Return: void
 */
void print_python_list_info(PyObject *list)
{
	int i = 0;
	PyListObject *ll;

	/* to use a pyobject, it has to be casted to a Py_List_Object */
	ll = (PyListObject *)list;
	printf("[*] Size of the Python List = %ld\n", ll->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", ll->allocated);
	/*("[*] my tp_name is %s\n", ll->ob_base.ob_base.ob_type->tp_name);*/
	for (; i < ll->ob_base.ob_size; i++)
	{
		printf("Element %d: %s\n", i, ll->ob_item[i]->ob_type->tp_name);
	}
}
