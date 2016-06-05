/* yafft.c
 *
 * Yet another FFT - A lightweight C library for the Fast Fourier Transform.
 *
 */

#include <math.h>

#include "yafft.h"

#define PI 3.14159265358979323846


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
 * Swap two complex numbers
 */
static inline void swap(complex float* a, complex float* b) {
    complex float c = *a;
    *a = *b;
    *b = c;
}


/*
 * Twiddle factor
 */
static complex float twiddle_factor(const unsigned int k, const unsigned int stage, const unsigned int n) {
    complex float W = cexpf(-I*2*PI*k/n);
    return W;
}


/*
 * Butterfly
 */
static void butterfly(complex float* x, complex float* y, const radix_type radix) {
    switch (radix) {
    case RADIX_2: {
        complex float z = *x;
        *x = z + *y;
        *y = z - *y;
        break;
    }
    }
}


/*
 * Decimation-in-Time Fast Fourier Transform
 */
void fft_dit(complex float* data, const unsigned int size) {
    // Variables
    const unsigned int stages = log2(size);
    unsigned int i, j;

    // Bit reversal
    for (i = 0; i < size; i++) {
        j = reverse_bits(i, stages);
        if (i < j) {
            swap(&data[i], &data[j]);
        }
    }

    // Danielson-Lanczos Lemma
    for (unsigned int m = 1; m <= stages; m++) {
        unsigned int point_size = 1 << m;

        for (unsigned int offset = 0; offset < size; offset += point_size) {
            for (unsigned int k = 0; k < (point_size >> 1); k++) {
                // Twiddle factor
                complex float W = twiddle_factor(k, m, point_size);

                // Butterfly
                i = offset + k;
                j = i + (point_size >> 1);

                data[j] *= W;
                butterfly(&data[i], &data[j], RADIX_2);
            }
        }
    }
}


/**
 * Fast Fourier Transform
 */
void fft(complex float* data, const unsigned int size) {
    fft_dit(data, size);
}
