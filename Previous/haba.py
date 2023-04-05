import library

def haba(a_dec, b_dec, N, l, k):
    a_bin = library.decimal_to_binary(a_dec, N)
    b_bin = library.decimal_to_binary(b_dec, N)
    sum_bin = []
    for i in range(N):
        sum_bin.append(-1)

    for i1 in range(0, k):
        a_bin_sub = a_bin[i1 * l:(i1 + 1) * l]
        b_bin_sub = b_bin[i1 * l:(i1 + 1) * l]
        if i1 == 0:
            carry_in_i1 = 0
            sum_carry = 0
        else:
            propagate_product = 0
            for i2 in range(0, l):
                propagate_i2 = library.xor2(a_bin_sub[i2], b_bin_sub[i2])
                propagate_product = propagate_i2 * propagate_product
            if propagate_product == 0:
                carry_in_i1 = next_carry_out_i2
                sum_carry = carry_out_i2
            else:
                carry_in_i1 = next_carry_out_i2
                sum_carry = next_carry_out_i2

        for i2 in range(0, l):
            generate_i2 = library.and2(a_bin_sub[i2], b_bin_sub[i2])
            propagate_i2 = library.xor2(a_bin_sub[i2], b_bin_sub[i2])
            if i2 == 0:
                previous_sum_carry = sum_carry
                previous_carry_out_i2 = carry_in_i1
                carry_out_i2 = generate_i2 + propagate_i2 * previous_carry_out_i2
                sum_bin[i1 * l + i2] = library.xor2(propagate_i2, previous_sum_carry)
            else:
                previous_carry_out_i2 = carry_out_i2
                carry_out_i2 = generate_i2 + propagate_i2 * previous_carry_out_i2
                sum_bin[i1 * l + i2] = library.xor2(propagate_i2, previous_carry_out_i2)
            if i2 == l-1:
                next_carry_out_i2 = generate_i2

        if i1 == (k-1):
            sum_bin.append(carry_out_i2)

    sum = library.binary_to_decimal(sum_bin, N + 1)
    return sum


# Primary Defined Value
N = 8
l = 2
k = int(N/l)

# Testing Template
a_dec = 255
b_dec = 140
sum_exact = a_dec + b_dec
sum_approx = haba(a_dec, b_dec, N, l, k)

print(sum_exact,sum_approx)