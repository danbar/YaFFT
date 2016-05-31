/*
 * yafft.c
 *
 */

#include <limits.h>
#include <math.h>

#include "yafft.h"


/*
 * Bit Twiddling Hacks
 * https://graphics.stanford.edu/~seander/bithacks.html
 *
 */
static inline unsigned int reverse_bits(unsigned int v, const unsigned int bits) {
	unsigned int r = v; // r will be reversed bits of v; first get LSB of v
	int s = bits - 1; // extra shift needed at end

	for (v >>= 1; v; v >>= 1) {
		r <<= 1;
		r |= v & 1;
		s--;
	}
	r <<= s; // shift when v's highest bits are zero
	return r;
}


static inline void swap(complex float* a, complex float* b) {
	complex float c = *a;
	*a = *b;
	*b = c;
}


/**
 *
 */
void fft(complex float* data, const unsigned int n) {
	// Initialize variables
	const unsigned int log2n = log2(n);

	// Bit reversal
	for (unsigned int i = 0; i < n; i++) {
	    unsigned int j = reverse_bits(i, log2n);
	    if (i < j) {
	        swap(&data[i], &data[j]);
	    }
	}

	// Danielson-Lanczos lemma
	// ...
}
