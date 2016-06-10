%module yafft

//
// C declarations
//
%{
    #define SWIG_FILE_WITH_INIT
    #include "src/yafft.h"
%}

//
// SWIG directives
//
%include "numpy.i"

%init %{
    import_array();
%}

%numpy_typemaps(complex_float, NPY_CFLOAT, int)

%apply (complex_float* INPLACE_ARRAY1, int DIM1) {(complex_float* data, unsigned int size)};

%include "src/yafft.h"
