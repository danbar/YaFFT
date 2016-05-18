function [y0, y1] = butterfly(x0, x1, radix_type)

    switch radix_type
        case 'radix2'
            y0 = x0 + x1;
            y1 = x0 - x1;
            
        otherwise
            error('Invalid radix type!');
    endswitch
    
end
