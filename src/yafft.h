/* yafft.h
 *
 * Yet another FFT - A lightweight C library for the Fast Fourier Transform.
 *
 */

#ifndef YAFFT_H_
#define YAFFT_H_

#include <complex.h>

void fft(complex float* data, const unsigned int n);

#endif /* YAFFT_H_ */
