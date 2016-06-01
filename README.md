# YaFFT
Yet another FFT - A lightweight C library for the Fast Fourier Transform.

...

_YaFFT is currently under development!_

## Usage
The source code of YaFFT is located in the folder `src`.

If you want to use YaFFT within your project, 
you can simply copy the source code or build a shared library by executing
```
./waf configure build
```
from the top-level directory. The shared library is created in the folder `build`.

The functionality of YaFFT can be tested by executing
```
./waf test
```
from the top-level directory.

## Build Dependencies
* Python
* SWIG

## Additional Test Dependencies
* NumPy
* Octave (+ Signal Processing Package)
* Oct2Py

## Other FFT Libraries
* [Kiss FFT](http://kissfft.sourceforge.net)
* [FFTW](http://www.fftw.org)
* [FFTS](https://github.com/anthonix/ffts)

