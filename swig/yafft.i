%module yafft

//
// C declarations
//
%{
    #define SWIG_FILE_WITH_INIT
    #include <complex.h>
    #include "src/yafft.h"
%}

//
// SWIG directives
//
%include <complex.i>
%include "numpy.i"

%init %{
    import_array();
%}

%numpy_typemaps(complex float, NPY_CFLOAT, int)
%numpy_typemaps(complex double, NPY_CDOUBLE, int)

%apply (complex float* INPLACE_ARRAY1, int DIM1) {(complex float* data, unsigned int n)};

%include "src/yafft.h"

