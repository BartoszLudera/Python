def fun(N):
    binary_representation = bin(N)[2:].strip('0')

    if '0' not in binary_representation:
        return 0
    
    sequences_of_ones = binary_representation.split('1')
    max_zeros_length = max(len(seq) for seq in sequences_of_ones if seq)
    return max_zeros_length

print(fun(9))
print(fun(529))
print(fun(15))
print(fun(792))
