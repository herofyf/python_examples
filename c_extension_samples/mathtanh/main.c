#include <Windows.h>
#include <math.h>
#include <Python.h>

const double e = 2.7182818284590459045235;

double sin_h(double x) 
{
	return (1 - pow(e, (-2 * x))) / (2 * pow(e, -x));
}

double cos_h(double x) 
{
	return (1 + pow(e, (-2 * x))) / (2 * pow(e, -x));
}

PyObject *tan_h(PyObject *self, PyObject *o) 
{
	double x = PyFloat_AsDouble(o);
	double tanh_x = sin_h(x) / cos_h(x);
	return PyFloat_FromDouble(tanh_x);
}

// assembly target name 必须是superfastcode这是python规定的
static PyMethodDef superfastcode_methods[] = {
	{"fast_tanh", (PyCFunction)tan_h, METH_O, NULL},
	{NULL, NULL, NULL, NULL}
};

static PyModuleDef superfastcode_module = {
	PyModuleDef_HEAD_INIT,
	"superfastcode",
	"Provides some functions, but faster",
	-1,
	superfastcode_methods
};

// https://www.youtube.com/watch?v=D9RlT06a1EI&list=PLReL099Y5nRdLgGAdrb_YeTdEnd23s6Ff&index=9
PyMODINIT_FUNC PyInit_superfastcode() {
	PyObject *m;
	m = NULL;
	m = PyModule_Create(&superfastcode_module);
	if (m == NULL)
		return NULL;

	return m;
}


/*


from superfastcode import fast_tanh
fast_tanh(12)

# install:
$ (sudo) python setup.py install
 
 # uninstall:
 $ pip freeze | grep PATTERN_BASED_ON_PACKAGE_NAME
 # then remove with pip:
 $ (sudo) pip uninstall PACKAGE_NAME


 to solve the problem: thread status, no current state
 c/c++ -> code generation->runtime library->change "multi-threaded debug dll" to "multi-threaded dll"



*/