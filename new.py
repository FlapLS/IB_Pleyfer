from decimal import *
from utils import to_text

N1 = 380077454101
N2 = 380903460337
N3 = 383306345689

C1 = '''
120321295984 
116941070964 
156315192664 
260149644765 
357688967002 
165841867143 
349826484990 
337993834720 
117681826230 
36279369135 
124613350713 
106958422772

'''

C2 = '''
261990433834
232071459327
305414687540
348455852917
206680974925
327578130329
5548686870
295985428633
157420509616
256913681356
271869775627
310864218021

'''

C3 = '''
322305651846
286065905390
188633713225
131649116365
253206684415
46677871611
65268441973
317133281785
52226297600
255637668770
201873507225
260192105953

'''

print(f'N1 = {N1}\nN2 = {N2}\nN3 = {N3}\nC1 = {C1}\nC2 = {C2}\nC3 = {C3}\n')

M0 = N1 * N2 * N3
m1 = N2 * N3
m2 = N1 * N3
m3 = N2 * N1
n1 = pow(m1, -1, N1)
n2 = pow(m2, -1, N2)
n3 = pow(m3, -1, N3)

print(f'M0 = N1 * N2 * N3 = {M0}')
print(f'm1 = N2 * N3 = {m1}\nm2 = N1 * N3 = {m2}\nm3 = N2 * N1 = {m3}\n')
print(f'n1 ≡ m1^(-1) (mod N1) = {n1}\nn2 ≡ m2^(-1) (mod N2) = {n2}\nn3 ≡ m3^(-1) (mod N3) = {n3}\n')

c1 = tuple(map(int, C1.split()))
c2 = tuple(map(int, C2.split()))
c3 = tuple(map(int, C3.split()))

full_message = ''
for i in range(len(c1)):
    S = (c1[i] * n1 * m1) + (c2[i] * n2 * m2) + (c3[i] * n3 * m3)
    summodM0 = S % M0
    message = round(summodM0 ** (Decimal(1 / 3)))
    print(f'S{i} = c1[{i}]*n1*m1 + c2[{i}]*n2*m2 + c3[{i}]*n3*m3 = {S}')
    print(f'summodM0[{i}] = S{i} % M0 = {summodM0}\nmessage{i} = summodM0[{i}]^(1/3) = {message}\n')
    full_message += to_text(message)

print(f'\nfull_message = {full_message}')