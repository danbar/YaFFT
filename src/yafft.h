/* yafft.h
 *
 * Yet another FFT - A lightweight C library for the Fast Fourier Transform.
 *
 */

#ifndef YAFFT_H_
#define YAFFT_H_

typedef struct complex_float {
    float real;
    float imag;
} complex_float;

typedef enum decimation_type {
    DECIMATION_IN_TIME,
    DECIMATION_IN_FREQUENCY
} decimation_type;

typedef enum radix_type {
    RADIX_2
} radix_type;

void fft(complex_float* data, const unsigned int size, const decimation_type decimation);

#endif /* YAFFT_H_ */
