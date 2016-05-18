function [X] = my_dft(x)
    % Initialize variables
    X = zeros(size(x));
    N = length(x);

    % Discrete Fourier transform
    for k = 0:N-1
        for n = 0:N-1
            X(k+1) += x(n+1)*exp(-j*k*n*2*pi/N);
        end
    end
endfunction
