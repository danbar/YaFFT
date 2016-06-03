/* yafft.c
 *
 * Yet another FFT - A lightweight C library for the Fast Fourier Transform.
 *
 */

#include <math.h>

#include "yafft.h"

#define PI 3.14159265358979323846
typedef enum radix_type {RADIX_2} radix_type;


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
    complex float W = cexpf(-I*2*PI*k/(1 << stage));
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
 * Fast Fourier Transform
 */
void fft(complex float* data, const unsigned int n) {
    // Initialize variables
    const unsigned int num_stages = log2(n);

    // Bit reversal
    for (unsigned int i = 0; i < n; i++) {
        unsigned int j = reverse_bits(i, num_stages);
        if (i < j) {
            swap(&data[i], &data[j]);
        }
    }

    // Danielson-Lanczos lemma
    for (unsigned int stage = 1; stage <= num_stages; stage++) {
        unsigned int step_size = 1 << stage;

        for (unsigned int offset = 0; offset < n; offset += step_size) {
            for (unsigned int k = 0; k < (step_size >> 1); k++) {
                // Twiddle factor
                complex float W = twiddle_factor(k, stage, n);

                // Butterfly
                int i = offset + k;
                int j = i + (step_size >> 1);

                data[j] *= W;
                butterfly(&data[i], &data[j], RADIX_2);
            }
        }
    }
}
