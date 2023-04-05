import library


def approx_cbec_csla1(a_dec, b_dec, N, l, k):
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
    ##########################################
        else:
            #carry_in_i1 = carry_i2_out
            carry_in_i1 = 1
    ##########################################
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
                    carry_i2_out = library.or2(carry_constant_delay, carry_ripple_carry)
        if i1 == k-1:
            carry_out = carry_i2_out
            sum_bin.append(carry_out)

    sum = library.binary_to_decimal(sum_bin, N + 1)
    #print(sum_bin)
    return sum


def approx_cbec_csla2(a_dec, b_dec, N, l, k):
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
    ##########################################
        else:
            #carry_in_i1 = carry_i2_out
            carry_in_i1 = 0
    ##########################################
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
                    carry_i2_out = library.or2(carry_constant_delay, carry_ripple_carry)
        if i1 == k-1:
            carry_out = carry_i2_out
            sum_bin.append(carry_out)

    sum = library.binary_to_decimal(sum_bin, N + 1)
    #print(sum_bin)
    return sum


def approx_cbec_csla3(a_dec, b_dec, N, l, k):
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
            kill = library.and2(library.not1(a_bin_sub[0]), library.not1(b_bin_sub[0]))
            select = library.or2(kill, carry_Prdt_i1)
            carry_in_i1 = library.mux3(carry_i2_out, carry_Prdt_i1, select)

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
                carry_constant_delay = library.or2(generate_i2, library.and2(propagate_i2,previous_carry_constant_delay))
                sum_bin[i1 * l + i2] = library.xor2(previous_carry_ripple_carry, library.xor2(propagate_i2, previous_carry_constant_delay))
                carry_ripple_carry = library.and2(library.xor2(propagate_i2, previous_carry_constant_delay), previous_carry_ripple_carry)
                if i2 == l-1:
                    carry_i2_out = library.or2(carry_constant_delay, carry_ripple_carry)
                    carry_Prdt_i1 = generate_i2
        if i1 == k-1:
            carry_out = carry_i2_out
            sum_bin.append(carry_out)

    sum = library.binary_to_decimal(sum_bin, N + 1)
    #print(sum_bin)
    return sum


# Primary Defined Value
N = 8
l = 4
k = int(N/l)


# Testing Template
a_dec = 222
b_dec = 14
sum_exact = a_dec + b_dec
sum_approx = approx_cbec_csla3(a_dec, b_dec, N, l, k)
#print(sum_exact,sum_approx)
