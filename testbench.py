import bcsa
import approximate_cbec_csla
import acsa
import library


def tester1(N, l, k):
    # Testing Sequences
    num_error = 0
    ED_sum = 0
    RED_sum = 0
    NMED = 0
    MRED = 0
    if N == 8:
        number_ranges = 256
        test_numbers = 256*256
        for i in range(0,256):
            for j in range(0,256):
                a_dec = i
                b_dec = j
                sum_exact = a_dec + b_dec
                sum_approx = approximate_cbec_csla.approx_cbec_csla1(a_dec, b_dec, N, l, k)
                ED = abs(sum_exact - sum_approx)
                if ED != 0:
                    #print(a_dec,b_dec,sum_exact,sum_approx)
                    num_error = num_error + 1
                    ED_sum = ED_sum + ED/100
                    if sum_exact != 0:
                        RED_sum = RED_sum + ED/sum_exact
        ER = num_error / test_numbers * 100
        NMED = ED_sum/(test_numbers/100*number_ranges)*10000
        MRED = RED_sum/test_numbers*10000
        print("When N =", N, "and l =", l)
        print("ER   is", ER)
        print("NMED is", NMED)
        print("MRED is", MRED, "\n")
    else:
        number_ranges = 2**N
        test_numbers = 10000000
        simplify = 1000
        for i in range(0, test_numbers):
                a_dec = library.random_sequence_generator(N)
                b_dec = library.random_sequence_generator(N)
                sum_exact = a_dec + b_dec
                sum_approx =  approximate_cbec_csla.approx_cbec_csla1(a_dec, b_dec, N, l, k)
                ED = abs(sum_exact - sum_approx)
                if ED != 0:
                    #print(a_dec,b_dec,sum_exact,sum_approx)
                    num_error = num_error + 1
                    ED_sum = ED_sum + ED/simplify
                    RED_sum = RED_sum + ED / sum_exact
        ER = num_error / (test_numbers) * 100
        NMED = ED_sum/(number_ranges*test_numbers/simplify)*10000
        MRED = RED_sum / test_numbers * 10000
        print("When N =", N, "and l =", l)
        print("ER   is", ER)
        print("NMED is", NMED)
        print("MRED is", MRED, "\n")


def tester2(N, l, k):
    # Testing Sequences
    num_error = 0
    ED_sum = 0
    RED_sum = 0
    NMED = 0
    MRED = 0
    if N == 8:
        number_ranges = 256
        test_numbers = 256*256
        for i in range(0,256):
            for j in range(0,256):
                a_dec = i
                b_dec = j
                sum_exact = a_dec + b_dec
                sum_approx = approximate_cbec_csla.approx_cbec_csla2(a_dec, b_dec, N, l, k)
                ED = abs(sum_exact - sum_approx)
                if ED != 0:
                    #print(a_dec,b_dec,sum_exact,sum_approx)
                    num_error = num_error + 1
                    ED_sum = ED_sum + ED/100
                    if sum_exact != 0:
                        RED_sum = RED_sum + ED/sum_exact
        ER = num_error / test_numbers * 100
        NMED = ED_sum/(test_numbers/100*number_ranges)*10000
        MRED = RED_sum/test_numbers*10000
        print("When N =", N, "and l =", l)
        print("ER   is", ER)
        print("NMED is", NMED)
        print("MRED is", MRED, "\n")
    else:
        number_ranges = 2**N
        test_numbers = 10000000
        simplify = 1000
        for i in range(0, test_numbers):
                a_dec = library.random_sequence_generator(N)
                b_dec = library.random_sequence_generator(N)
                sum_exact = a_dec + b_dec
                sum_approx =  approximate_cbec_csla.approx_cbec_csla2(a_dec, b_dec, N, l, k)
                ED = abs(sum_exact - sum_approx)
                if ED != 0:
                    #print(a_dec,b_dec,sum_exact,sum_approx)
                    num_error = num_error + 1
                    ED_sum = ED_sum + ED/simplify
                    RED_sum = RED_sum + ED / sum_exact
        ER = num_error / (test_numbers) * 100
        NMED = ED_sum/(number_ranges*test_numbers/simplify)*10000
        MRED = RED_sum / test_numbers * 10000
        print("When N =", N, "and l =", l)
        print("ER   is", ER)
        print("NMED is", NMED)
        print("MRED is", MRED, "\n")


def tester_approx_cbec_csla3(N, l, k):
    # Testing Sequences
    num_error = 0
    ED_sum = 0
    RED_sum = 0
    NMED = 0
    MRED = 0
    if N == 8:
        number_ranges = 256
        test_numbers = 256*256
        for i in range(0,256):
            for j in range(0,256):
                a_dec = i
                b_dec = j
                sum_exact = a_dec + b_dec
                sum_approx = approximate_cbec_csla.approx_cbec_csla3(a_dec, b_dec, N, l, k)
                ED = abs(sum_exact - sum_approx)
                if ED != 0:
                    #print(a_dec,b_dec,sum_exact,sum_approx)
                    num_error = num_error + 1
                    ED_sum = ED_sum + ED/100
                    if sum_exact != 0:
                        RED_sum = RED_sum + ED/sum_exact
        ER = num_error / test_numbers * 100
        NMED = ED_sum/(test_numbers/100*number_ranges)*10000
        MRED = RED_sum/test_numbers*10000
        print("When N =", N, "and l =", l)
        print("ER   is", ER)
        print("NMED is", NMED)
        print("MRED is", MRED, "\n")
    else:
        number_ranges = 2**N
        test_numbers = 10000000
        simplify = 1000
        for i in range(0, test_numbers):
                a_dec = library.random_sequence_generator(N)
                b_dec = library.random_sequence_generator(N)
                sum_exact = a_dec + b_dec
                sum_approx =  approximate_cbec_csla.approx_cbec_csla3(a_dec, b_dec, N, l, k)
                ED = abs(sum_exact - sum_approx)
                if ED != 0:
                    print(a_dec,b_dec,sum_exact,sum_approx)
                    num_error = num_error + 1
                    ED_sum = ED_sum + ED/simplify
                    RED_sum = RED_sum + ED / sum_exact
        ER = num_error / (test_numbers) * 100
        NMED = ED_sum/(number_ranges*test_numbers/simplify)*10000
        MRED = RED_sum / test_numbers * 10000
        print("When N =", N, "and l =", l)
        print("ER   is", ER)
        print("NMED is", NMED)
        print("MRED is", MRED, "\n")


def tester_bcsa(N, l, k):
    # Testing Sequences
    num_error = 0
    ED_sum = 0
    RED_sum = 0
    NMED = 0
    MRED = 0
    print("input1", "input2", "exact", "approximate")
    if N == 8:
        number_ranges = 256
        test_numbers = 256*256
        for i in range(0,256):
            for j in range(0,256):
                a_dec = i
                b_dec = j
                sum_exact = a_dec + b_dec
                sum_approx = bcsa.bcsa(a_dec, b_dec, N, l, k)
                ED = abs(sum_exact - sum_approx)
                if ED != 0:
                    print(a_dec,b_dec,sum_exact,sum_approx)
                    num_error = num_error + 1
                    ED_sum = ED_sum + ED/100
                    if sum_exact != 0:
                        RED_sum = RED_sum + ED/sum_exact
        ER = num_error / test_numbers * 100
        NMED = ED_sum/(test_numbers/100*number_ranges)*10000
        MRED = RED_sum/test_numbers*10000
        print("When N =", N, "and l =", l)
        print("ER   is", ER)
        print("NMED is", NMED)
        print("MRED is", MRED, "\n")
    else:
        number_ranges = 2**N
        test_numbers = 10000000
        simplify = 1000
        for i in range(0, test_numbers):
                a_dec = library.random_sequence_generator(N)
                b_dec = library.random_sequence_generator(N)
                sum_exact = a_dec + b_dec
                sum_approx = bcsa.bcsa(a_dec, b_dec, N, l, k)
                ED = abs(sum_exact - sum_approx)
                if ED != 0:
                    #print(a_dec,b_dec,sum_exact,sum_approx)
                    num_error = num_error + 1
                    ED_sum = ED_sum + ED/simplify
                    RED_sum = RED_sum + ED / sum_exact
                    print(a_dec, b_dec, sum_exact, sum_approx)

        ER = num_error / (test_numbers) * 100
        NMED = ED_sum/(number_ranges*test_numbers/simplify)*10000
        MRED = RED_sum / test_numbers * 10000
        print("When N =", N, "and l =", l)
        print("ER   is", ER)
        print("NMED is", NMED)
        print("MRED is", MRED, "\n")


def tester_acsa(N, l, k):
    # Testing Sequences
    num_error = 0
    ED_sum = 0
    RED_sum = 0
    NMED = 0
    MRED = 0
    if N == 8:
        number_ranges = 256
        test_numbers = 256*256
        print("input1","input2","exact","approximate")
        for i in range(0,256):
            for j in range(0,256):
                a_dec = i
                b_dec = j
                sum_exact = a_dec + b_dec
                sum_approx = acsa.acsa(a_dec, b_dec, N, l, k)
                ED = abs(sum_exact - sum_approx)
                if ED != 0:
                    #print(a_dec,b_dec,sum_exact,sum_approx)
                    num_error = num_error + 1
                    ED_sum = ED_sum + ED/100
                    if sum_exact != 0:
                        RED_sum = RED_sum + ED/sum_exact
        ER = num_error / test_numbers * 100
        NMED = ED_sum/(test_numbers/100*number_ranges)*10000
        MRED = RED_sum/test_numbers*10000
        print("When N =", N, "and l =", l)
        print("ER   is", ER)
        print("NMED is", NMED)
        print("MRED is", MRED, "\n")
    else:
        number_ranges = 2**N
        test_numbers = 10000000
        simplify = 1000
        for i in range(0, test_numbers):
                a_dec = library.random_sequence_generator(N)
                b_dec = library.random_sequence_generator(N)
                sum_exact = a_dec + b_dec
                sum_approx = acsa.acsa(a_dec, b_dec, N, l, k)
                ED = abs(sum_exact - sum_approx)
                if ED != 0:
                    #print(a_dec,b_dec,sum_exact,sum_approx)
                    num_error = num_error + 1
                    ED_sum = ED_sum + ED/simplify
                    RED_sum = RED_sum + ED / sum_exact
        ER = num_error / (test_numbers) * 100
        NMED = ED_sum/(number_ranges*test_numbers/simplify)*10000
        MRED = RED_sum / test_numbers * 10000
        print("When N =", N, "and l =", l)
        print("ER   is", ER)
        print("NMED is", NMED)
        print("MRED is", MRED, "\n")
#N = 8
#l = 2
#k = int(N/l)

N_list = [8]
l_list = [2]


print("Proposed 2")
for N in N_list:
    for l in l_list:
        k = int(N/l)
        tester_bcsa(N,l,k)




