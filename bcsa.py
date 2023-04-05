import library


def bcsa(a_dec, b_dec, N, l, k):
    a_bin = library.decimal_to_binary(a_dec, N)
    b_bin = library.decimal_to_binary(b_dec, N)
    #print(a_bin)
    #print(b_bin)
    sum_bin = []
    for i in range(N):
        sum_bin.append(2)
    for i1 in range(0, k):
        a_bin_sub = a_bin[i1*l:(i1+1) * l]
        b_bin_sub = b_bin[i1*l:(i1+1) * l]
        for i2 in range(0, l):
            if l == 2:
                if i1 == 0:
                    carry_in_i1 = 0
                else:
                    kill = library.and2(library.not1(a_bin_sub[0]), library.not1(b_bin_sub[0]))
                    select = library.or2(kill, carry_Prdt_i1)
                    carry_in_i1 = library.mux3(carry_ADD_i1, carry_Prdt_i1, select)
                generate_i2 = library.and2(a_bin_sub[i2], b_bin_sub[i2])
                propagate_i2 = library.xor2(a_bin_sub[i2], b_bin_sub[i2])
                if i2 == 0:
                    sum_bin[i1 * l + i2] = library.xor2(propagate_i2, carry_in_i1)
                    carry_i2 = library.or2(generate_i2, library.and2(propagate_i2, carry_in_i1))
                    carry_next = library.or2(generate_i2, library.and2(propagate_i2, 0))
                else:
                    carry_Prdt_i1 = library.and2(a_bin_sub[i2], b_bin_sub[i2])
                    sum_bin[i1 * l + i2] = library.xor2(propagate_i2, carry_i2)
                    carry_ADD_i1 = library.and2(propagate_i2, carry_next)
                    if i1 == k - 1:
                        # kill = 1
                        # select = or2(kill, carry_Prdt_i1)
                        # carry_in = mux3(carry_ADD_i1, carry_Prdt_i1, select)
                        carry_out = library.or2(generate_i2, library.and2(propagate_i2, carry_i2))
                        sum_bin.append(carry_out)
            else:
                if i1 == 0:
                    carry_in_i1 = 0
                else:
                    kill = library.and2(library.not1(a_bin_sub[0]), library.not1(b_bin_sub[0]))
                    select = library.or2(kill, carry_Prdt_i1)
                    carry_in_i1 = library.mux3(carry_ADD_i1, carry_Prdt_i1, select)
                generate_i2 = library.and2(a_bin_sub[i2], b_bin_sub[i2])
                propagate_i2 = library.xor2(a_bin_sub[i2], b_bin_sub[i2])
                if i2 == 0:
                    sum_bin[i1 * l + i2] = library.xor2(propagate_i2, carry_in_i1)
                    carry_sub_i2 = library.or2(generate_i2, library.and2(propagate_i2, carry_in_i1))
                    carry_i2 = library.or2(generate_i2, library.and2(propagate_i2, 0))
                elif i2 == l - 1:
                    carry_Prdt_i1 = library.and2(a_bin_sub[i2], b_bin_sub[i2])
                    sum_bin[i1 * l + i2] = library.xor2(propagate_i2, carry_sub_i2)
                    carry_ADD_i1 = library.and2(propagate_i2, carry_i2)
                    if i1 == k - 1:
                        # kill = 1
                        # select = or2(kill, carry_Prdt_i1)
                        # carry_in = mux3(carry_ADD_i1, carry_Prdt_i1, select)
                        carry_out = library.or2(generate_i2, library.and2(propagate_i2, carry_sub_i2))
                        sum_bin.append(carry_out)
                else:
                    previous_carry_sub_i2 = carry_sub_i2
                    previous_carry_i2 = carry_i2
                    sum_bin[i1 * l + i2] = library.xor2(propagate_i2, previous_carry_sub_i2)
                    carry_sub_i2 = library.or2(generate_i2, library.and2(propagate_i2, previous_carry_sub_i2))
                    carry_i2 = library.or2(generate_i2, library.and2(propagate_i2, previous_carry_i2))
    #print(sum_bin)
    sum = library.binary_to_decimal(sum_bin, N+1)
    return sum


def bcsa_eru(a_dec, b_dec, N, l, k):
    a_bin = library.decimal_to_binary(a_dec, N)
    b_bin = library.decimal_to_binary(b_dec, N)
    #print(a_bin)
    #print(b_bin)
    sum_bin = []
    for i in range(N):
        sum_bin.append(2)
    for i1 in range(0, k):
        a_bin_sub = a_bin[i1*l:(i1+1) * l]
        b_bin_sub = b_bin[i1*l:(i1+1) * l]
        for i2 in range(0, l):
            if l == 2:
                if i1 == 0:
                    carry_in_i1 = 0
                else:
                    kill = library.and2(library.not1(a_bin_sub[0]), library.not1(b_bin_sub[0]))
                    select = library.or2(kill, carry_Prdt_i1)
                    carry_in_i1 = library.mux3(carry_ADD_i1, carry_Prdt_i1, select)
                generate_i2 = library.and2(a_bin_sub[i2], b_bin_sub[i2])
                propagate_i2 = library.xor2(a_bin_sub[i2], b_bin_sub[i2])
                if i2 == 0:
                    sum_bin[i1 * l + i2] = library.xor2(propagate_i2, carry_in_i1)
                    carry_i2 = library.or2(generate_i2, library.and2(propagate_i2, carry_in_i1))
                    carry_next = library.or2(generate_i2, library.and2(propagate_i2, 0))
                else:
                    carry_Prdt_i1 = library.and2(a_bin_sub[i2], b_bin_sub[i2])
                    sum_bin[i1 * l + i2] = library.xor2(propagate_i2, carry_i2)
                    carry_ADD_i1 = library.and2(propagate_i2, carry_next)
                    if i1 == k - 1:
                        # kill = 1
                        # select = or2(kill, carry_Prdt_i1)
                        # carry_in = mux3(carry_ADD_i1, carry_Prdt_i1, select)
                        carry_out = library.or2(generate_i2, library.and2(propagate_i2, carry_i2))
                        sum_bin.append(carry_out)
            else:
                if i1 == 0:
                    carry_in_i1 = 0
                else:
                    kill = library.and2(library.not1(a_bin_sub[0]), library.not1(b_bin_sub[0]))
                    select = library.or2(kill, carry_Prdt_i1)
                    carry_in_i1 = library.mux3(carry_ADD_i1, carry_Prdt_i1, select)
                generate_i2 = library.and2(a_bin_sub[i2], b_bin_sub[i2])
                propagate_i2 = library.xor2(a_bin_sub[i2], b_bin_sub[i2])
                if i2 == 0:
                    sum_bin[i1 * l + i2] = library.xor2(propagate_i2, carry_in_i1)
                    carry_sub_i2 = library.or2(generate_i2, library.and2(propagate_i2, carry_in_i1))
                    carry_i2 = library.or2(generate_i2, library.and2(propagate_i2, 0))
                elif i2 == l - 1:
                    carry_Prdt_i1 = library.and2(a_bin_sub[i2], b_bin_sub[i2])
                    sum_bin[i1 * l + i2] = library.xor2(propagate_i2, carry_sub_i2)
                    carry_ADD_i1 = library.and2(propagate_i2, carry_i2)
                    if i1 == k - 1:
                        # kill = 1
                        # select = or2(kill, carry_Prdt_i1)
                        # carry_in = mux3(carry_ADD_i1, carry_Prdt_i1, select)
                        carry_out = library.or2(generate_i2, library.and2(propagate_i2, carry_sub_i2))
                        sum_bin.append(carry_out)
                else:
                    previous_carry_sub_i2 = carry_sub_i2
                    previous_carry_i2 = carry_i2
                    sum_bin[i1 * l + i2] = library.xor2(propagate_i2, previous_carry_sub_i2)
                    carry_sub_i2 = library.or2(generate_i2, library.and2(propagate_i2, previous_carry_sub_i2))
                    carry_i2 = library.or2(generate_i2, library.and2(propagate_i2, previous_carry_i2))
    #print(sum_bin)
    sum = library.binary_to_decimal(sum_bin, N+1)
    return sum

# Primary Defined Value
N = 8
l = 4
k = int(N/l)

# Testing Template
a_dec = 239
b_dec = 1
sum_exact = a_dec + b_dec
sum_approx = bcsa(a_dec, b_dec, N, l, k)

#print(sum_exact,sum_approx)
