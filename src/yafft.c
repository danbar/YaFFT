/* yafft.c
 *
 * Yet another FFT - A lightweight C library for the Fast Fourier Transform.
 *
 */

#include <math.h>

#include "yafft.h"

#define TWO_PI 6.2831853071795862

#define CADD(x, y) ((complex_float) {(x).real + (y).real, \
                                     (x).imag + (y).imag})
#define CSUB(x, y) ((complex_float) {(x).real - (y).real, \
                                     (x).imag - (y).imag})
#define CMUL(x, y) ((complex_float) {(x).real*(y).real - (x).imag*(y).imag, \
                                     (x).real*(y).imag + (x).imag*(y).real})


/*
 * Bit Twiddling Hacks
 * https://graphics.stanford.edu/~seander/bithacks.html
 *
 */
static unsigned int reverse_bits(unsigned int v, const unsigned int num_bits) {
    unsigned int r = v;   // r will be reversed bits of v
    int s = num_bits - 1; // extra shift needed at end

    for (v >>= 1; v; v >>= 1) {
        r <<= 1;
        r |= v & 1;
        s--;
    }
    r <<= s;                  // shift when v's highest bits are zero
    r &= (1 << num_bits) - 1; // mask out non-significant bits
    return r;
}


/*
 * Generate twiddle factors
 */
void generate_twiddle_factors(complex_float* data, const unsigned int size, const unsigned int n) {
    for (unsigned int k = 0; k < size; k++) {
        data[k].real = cos(TWO_PI*k/n);
        data[k].imag = -sin(TWO_PI*k/n);
    }
}


/*
 * Swap two complex numbers
 */
static inline void swap_complex_numbers(complex_float* a, complex_float* b) {
    complex_float c = *a;
    *a = *b;
    *b = c;
}


/*
 * Butterfly
 */
static void butterfly(complex_float* x, complex_float* y, const radix_type radix) {
    switch (radix) {
    case RADIX_2: {
        complex_float z = *x;
        *x = CADD(z, *y);
        *y = CSUB(z, *y);
        break;
    }
    }
}


/*
 * Decimation-in-Time (DIT) Fast Fourier Transform (FFT)
 */
static void fft_dit(
        complex_float* data,
        const unsigned int size,
        const unsigned int stages,
        const complex_float* twiddle_factor
) {
    unsigned int i, j;

    // Bit reversal
    for (i = 0; i < size; i++) {
        j = reverse_bits(i, stages);
        if (i < j) {
            swap_complex_numbers(&data[i], &data[j]);
        }
    }

    // FFT Stages
    unsigned int sample_step_size;
    unsigned int twiddle_step_size = size >> 1;

    for (int m = 1; m <= stages; m++) {
        sample_step_size = 1 << m;
        unsigned int separator = sample_step_size >> 1;

        // N-point FFTs
        for (unsigned int offset = 0; offset < size; offset += sample_step_size) {
            for (unsigned int k = 0; k < separator; k++) {
                // Twiddle factor
                complex_float W = twiddle_factor[k*twiddle_step_size];

                // Indices
                i = offset + k;
                j = i + separator;

                // Butterfly
                data[j] = CMUL(data[j], W);
                butterfly(&data[i], &data[j], RADIX_2);
            }
        }
        twiddle_step_size >>= 1;
    }
}


/*
 * Decimation-in-Frequency (DIF) Fast Fourier Transform (FFT)
 */
static void fft_dif(
        complex_float* data,
        const unsigned int size,
        const unsigned int stages,
        const complex_float* twiddle_factor
) {
    unsigned int i, j;

    // FFT Stages
    unsigned int sample_step_size;
    unsigned int twiddle_step_size = 1;

    for (int m = stages; m >= 0; m--) {
        sample_step_size = 1 << m;
        unsigned int separator = sample_step_size >> 1;

        // N-point FFTs
        for (unsigned int offset = 0; offset < size; offset += sample_step_size) {
            for (unsigned int k = 0; k < separator; k++) {
                // Twiddle factor
                complex_float W = twiddle_factor[k*twiddle_step_size];

                // Indices
                i = offset + k;
                j = i + separator;

                // Butterfly
                butterfly(&data[i], &data[j], RADIX_2);
                data[j] = CMUL(data[j], W);
            }
        }
        twiddle_step_size <<= 1;
    }

    // Bit reversal
    for (i = 0; i < size; i++) {
        j = reverse_bits(i, stages);
        if (i < j) {
            swap_complex_numbers(&data[i], &data[j]);
        }
    }
}


/**
 * Fast Fourier Transform (FFT)
 */
void fft(complex_float* data, const unsigned int size, const decimation_type decimation) {
    // Number of Stages
    const unsigned int stages = log2(size);

    // Twiddle factors
    complex_float twiddle_factor[size >> 1];
    generate_twiddle_factors(twiddle_factor, size >> 1, size);

    // FFT
    switch (decimation) {
        case DECIMATION_IN_TIME:
            fft_dit(data, size, stages, twiddle_factor);
            break;
        case DECIMATION_IN_FREQUENCY:
            fft_dif(data, size, stages, twiddle_factor);
            break;
    }
}
