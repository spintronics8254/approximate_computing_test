import library


def dynamic_cbec_csla1(a_dec, b_dec, N, l, k, control, mode):
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
            # ---------------- Dynamic Carry Mode 1 ----------------
            # Mode 1 : injecting 0
            if mode == 1:
                if control == 0:
                    if i1 < 3*k/4: carry_in_i1 = 0
                    else: carry_in_i1 = carry_i2_out
                elif control == 1:
                    if i1 < 2*k/4: carry_in_i1 = 0
                    else: carry_in_i1 = carry_i2_out
                elif control == 2:
                    if i1 < k/4: carry_in_i1 = 0
                    else: carry_in_i1 = carry_i2_out
                else:
                    carry_in_i1 = carry_i2_out
            # ---------------- Dynamic Carry Mode 2 ----------------
            # Mode 2 : injecting 1
            if mode == 2:
                if control == 0:
                    if i1 < 3*k/4: carry_in_i1 = 1
                    else: carry_in_i1 = carry_i2_out
                elif control == 1:
                    if i1 < 2*k/4: carry_in_i1 = 1
                    else: carry_in_i1 = carry_i2_out
                elif control == 2:
                    if i1 < k/4: carry_in_i1 = 1
                    else: carry_in_i1 = carry_i2_out
                else:
                    carry_in_i1 = carry_i2_out
            # ---------------- Dynamic Carry Control3 ----------------
            # Mode 3 : injecting the generate signal of a previous block's last input bits
            if mode == 3:
                if control == 0:
                    if i1 < 3*k/4: carry_in_i1 = carry_i2_control_mode3
                    else: carry_in_i1 = carry_i2_out
                elif control == 1:
                    if i1 < 2*k/4: carry_in_i1 = carry_i2_control_mode3
                    else: carry_in_i1 = carry_i2_out
                elif control == 2:
                    if i1 < k/4: carry_in_i1 = carry_i2_control_mode3
                    else: carry_in_i1 = carry_i2_out
                else:
                    carry_in_i1 = carry_i2_out
            # ---------------- Dynamic Carry Control4 ----------------
            # Mode 4 : injecting XORed the generate signal of a previous block's last(i-1)'th input bits
            # and the propagate signal of (i-2)'th bits
            if mode == 4:
                if control == 0:
                    if i1 < 3*k/4: carry_in_i1 = carry_i2_control_mode4
                    else: carry_in_i1 = carry_i2_out
                elif control == 1:
                    if i1 < 2*k/4: carry_in_i1 = carry_i2_control_mode4
                    else: carry_in_i1 = carry_i2_out
                elif control == 2:
                    if i1 < k/4: carry_in_i1 = carry_i2_control_mode4
                    else: carry_in_i1 = carry_i2_out
                else:
                    carry_in_i1 = carry_i2_out

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
                    carry_i2_control_mode3 = generate_i2
                    if generate_i2 == 0:
                        mode4_previous_bit_generate = library.and2(a_bin_sub[l-2], b_bin_sub[l-2])
                        carry_i2_control_mode4 = library.and2(mode4_previous_bit_generate,propagate_i2)
                    else:
                        carry_i2_control_mode4 = generate_i2
        if i1 == k-1:
            carry_out = carry_i2_out
            sum_bin.append(carry_out)

    sum = library.binary_to_decimal(sum_bin, N + 1)
    #print(sum_bin)
    return sum


# Primary Defined Value
N = 8
l = 2
k = int(N/l)


# Testing Template
a_dec = 110
b_dec = 113
con = 1
mode = 1

sum_exact = a_dec + b_dec
sum_approx = dynamic_cbec_csla1(a_dec, b_dec, N, l, k, con, mode)

a_bin = library.decimal_to_binary(a_dec,N)
b_bin = library.decimal_to_binary(b_dec,N)
sum_approx_bin = library.decimal_to_binary(sum_approx,N+1)
print("  ",a_bin,"\n"," ",b_bin,"\n","  ",sum_approx_bin)
