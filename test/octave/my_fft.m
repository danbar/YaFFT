function [x] = my_fft(x)
    % Zero padding
    x(end+1:2^nextpow2(length(x))) = 0;

    % Initialize variables
    N = length(x);
    
    % Bit reversal
    x = bitrevorder(x);

    % Danielson-Lanczos lemma
    for stage = 1:log2(N)      
        step_size = 2^stage;    
    
        for offset = 0:step_size:N-1           
            for k = 0:step_size/2-1

                % Twiddle factor
                W = twiddle_factor(k, stage, N);

                % Butterfly
                ind0 = offset+k+1;
                ind1 = offset+k+1+step_size/2;
                
                [x(ind0) x(ind1)] = butterfly(x(ind0), x(ind1)*W, 'radix2');
            
            end
        end 
        
    end
endfunction

function W = twiddle_factor(k, stage, N)
    W = exp(-j*2*pi*k/2^stage);
end
