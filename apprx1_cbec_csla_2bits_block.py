import library


def approx1_cbec_csla(a_dec, b_dec, N, l, k):
    a_bin = library.decimal_to_binary(a_dec, N)
    b_bin = library.decimal_to_binary(b_dec, N)

    sum_bin = []
    for i in range(N):
        sum_bin.append(2)
    carry_out = 0

    for i1 in range(0, k):
        a_bin_sub = a_bin[i1 * l:(i1 + 1) * l]
        b_bin_sub = b_bin[i1 * l:(i1 + 1) * l]
        if i1 == 0:
            carry_in_i1 = 0
        else:
            # approximate method BCSA
            kill = library.and2(library.not1(a_bin_sub[0]), library.not1(b_bin_sub[0]))
            select = library.or2(kill, carry_approximate)
            carry_in_i1 = library.mux3(carry_ADD, carry_approximate, select)
            # carry_in_i1 = carry_i2_out

        for i2 in range(0, l):
            generate_i2 = library.and2(a_bin_sub[i2], b_bin_sub[i2])
            propagate_i2 = library.xor2(a_bin_sub[i2], b_bin_sub[i2])
            if i2 == 0:
                carry_constant_delay = generate_i2
                sum_bin[i1 * l + i2] = library.xor2(propagate_i2, carry_in_i1)
                carry_ripple_carry = library.and2(propagate_i2, carry_in_i1)
            else:
                previous_carry_constant_delay = carry_constant_delay
                previous_carry_ripple_carry = carry_ripple_carry
                carry_constant_delay = library.or2(generate_i2, library.and2(propagate_i2, previous_carry_constant_delay))
                sum_bin[i1 * l + i2] = library.xor2(previous_carry_ripple_carry, library.xor2(propagate_i2, previous_carry_constant_delay))
                carry_ripple_carry = library.and2(library.xor2(propagate_i2, previous_carry_constant_delay), previous_carry_ripple_carry)
                if i2 == l-1:
                    # approximate part
                    carry_i2_out = library.or2(carry_constant_delay, carry_ripple_carry)
                    carry_ADD = carry_constant_delay
                    carry_approximate = generate_i2
        if i1 == k-1:
            carry_out = carry_i2_out
            sum_bin.append(carry_out)

    sum = library.binary_to_decimal(sum_bin, N + 1)
    #print(sum_bin)
    return sum


def approx2_cbec_csla(a_dec, b_dec, N, l, k):
    a_bin = library.decimal_to_binary(a_dec, N)
    b_bin = library.decimal_to_binary(b_dec, N)

    sum_bin = []
    for i in range(N):
        sum_bin.append(2)
    carry_out = 0

    for i1 in range(0, k):
        a_bin_sub = a_bin[i1 * l:(i1 + 1) * l]
        b_bin_sub = b_bin[i1 * l:(i1 + 1) * l]
        if i1 == 0:
            carry_in_i1 = 0
        else:
            # approximate method BCSA
            kill = library.and2(library.not1(a_bin_sub[0]), library.not1(b_bin_sub[0]))
            select = library.or2(kill, carry_approximate)
            carry_in_i1 = library.mux3(carry_ADD, carry_approximate, select)
            # carry_in_i1 = carry_i2_out

        for i2 in range(0, l):
            generate_i2 = library.and2(a_bin_sub[i2], b_bin_sub[i2])
            propagate_i2 = library.xor2(a_bin_sub[i2], b_bin_sub[i2])
            if i2 == 0:
                carry_constant_delay = generate_i2
                sum_bin[i1 * l + i2] = library.xor2(propagate_i2, carry_in_i1)
                carry_ripple_carry = library.and2(propagate_i2, carry_in_i1)
            else:
                previous_carry_constant_delay = carry_constant_delay
                previous_carry_ripple_carry = carry_ripple_carry
                carry_constant_delay = library.or2(generate_i2, library.and2(propagate_i2, previous_carry_constant_delay))
                sum_bin[i1 * l + i2] = library.xor2(previous_carry_ripple_carry, library.xor2(propagate_i2, previous_carry_constant_delay))
                carry_ripple_carry = library.and2(library.xor2(propagate_i2, previous_carry_constant_delay), previous_carry_ripple_carry)
                if i2 == l-1:
                    # approximate part
                    carry_i2_out = library.or2(carry_constant_delay, carry_ripple_carry)
                    carry_ADD = carry_constant_delay
                    carry_approximate = generate_i2
        if i1 == k-1:
            carry_out = carry_i2_out
            sum_bin.append(carry_out)

    sum = library.binary_to_decimal(sum_bin, N + 1)
    #print(sum_bin)
    return sum


# Primary Defined Value
N = 16
l = 2
k = int(N/l)


# Testing Template
a_dec = 22
b_dec = 14141
sum_exact = a_dec + b_dec
sum_approx = approx1_cbec_csla(a_dec, b_dec, N, l, k)
print(sum_exact,sum_approx)
