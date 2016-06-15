
#include <stdio.h>
#include <math.h>

#include <yafft.h>

/*
 * A simple example which computes the FFT of a sine.
 * The sine is given as
 *
 *   x[n] = sin(2*pi*f/fs*n),
 *
 * where the frequency f = 50Hz and the sampling frequency fs = 400Hz.
 *
 */
int main() {
    // Use designated initializers to fill array.
    complex_float sine[] = {
        {.real = +0.0},
        {.real = +1.0/sqrt(2)},
        {.real = +1.0},
        {.real = +1.0/sqrt(2)},
        {.real = +0.0},
        {.real = -1.0/sqrt(2)},
        {.real = -1.0},
        {.real = -1.0/sqrt(2)}
    };

    // Compute FFT (by using decimation-in-time radix 2 algorithm)
    fft_radix2(sine, 8, DECIMATION_IN_TIME);

    // Print double-sided amplitude spectrum
    printf("double-sided amplitude spectrum:\n");

    for (int i = 0; i < 8; i++) {
        printf("%f\n", sqrt(pow(sine[i].real, 2) + pow(sine[i].imag, 2)));
    }

    return 0;
}
