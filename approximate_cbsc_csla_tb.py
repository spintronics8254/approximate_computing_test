import approximate_cbec_csla
import exact_cbec_csla


N = 8
l = 4
k = int(N/l)
# Testing Sequences
num_error = 0
for i in range(0,2**N):
    for j in range(0,2**N):
        a_dec = i
        b_dec = j
        sum_exact = a_dec + b_dec
        #sum_approx = approximate_cbec_csla.approx_cbec_csla1(a_dec, b_dec, N, l, k)
        sum_approx = exact_cbec_csla.cbec_csla(a_dec, b_dec, N, l, k)
        ED = sum_exact - sum_approx
        if ED != 0:
            #print(a_dec,b_dec,sum_exact,sum_approx)
            num_error = num_error + 1
ER = num_error / (256*256) * 100
print(ER)