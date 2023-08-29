def longest_collatz(input_array):
    def even(item):
        item = item / 2
        return item
    
    def odd(item):
        item = (3 * item) + 1
        return item
    
    nl = 0
    nc = 0
    for i in input_array:
        temp_i = i
        counter = 0
        while i != 1:
            counter += 1
            if int(i)%2==0:
                i = even(i)
                
                
            else:
                i = odd(i)
        if counter > nc:
            nc = counter
            nl = temp_i
        
    
    return nl
    
        
        
