%module yafft

// SWIG Libraries
%include <carrays.i>
%include <complex.i>

%array_functions(float complex, data)

%{
    // Declarations
    #include <complex.h>
    #include <stdint.h>
%}



%inline %{
    extern void fft(float complex *data, const unsigned long N);
%}

