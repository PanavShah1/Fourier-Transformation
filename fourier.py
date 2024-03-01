import numpy as np

y = np.array([np.gcd(i, i+100) for i in range(0, 100)])
# y = np.array([2*np.pi/i for i in range(1, 10)])
l = len(y)

f_matrix = np.zeros((l, l), dtype=np.complex128)

# print(l)
# print(f_matrix)


for i in range(l):
    for j in range(l):
        f_matrix[i][j] = np.exp(-1j*(i*j) * 2*np.pi/l)
# print(f_matrix)


coeff = np.zeros(0, dtype=np.complex128)
cos_coeff = np.zeros(0, dtype=np.float128)
sin_coeff = np.zeros(0, dtype=np.float128)


for row in f_matrix:
    dot = np.dot(row, y)*1/l
    # print(dot)
    coeff = np.append(coeff, dot)
    cos_coeff = np.append(cos_coeff, np.real(dot))
    sin_coeff = np.append(sin_coeff, -np.imag(dot))
print(f"coeff : {coeff}")
print(f"sin coeff : {sin_coeff}")
print(f"cos coeff : {cos_coeff}")



def calculate(t):
    sum = 0
    sum_cos = 0 
    sum_sin = 0
    for i in range(l):
        sum+=coeff[i]*np.exp(i*1j*t)
        sum_cos+= cos_coeff[i] * np.cos(i*t)
        sum_sin+= sin_coeff[i] * np.sin(i*t)
    print(f"sum : {sum}")
    # print(f"sum2 : {sum2}")
    value = sum
    real = np.real(value)
    imaginary = np.imag(value)
    return(real, imaginary, sum_cos, sum_sin)
    # print(real+imaginary)

scale = 1
sin_coeff = sin_coeff * scale
cos_coeff = cos_coeff * scale

print(sin_coeff)
print(cos_coeff)

print(f"claculate ")
real, imaginary, sum_cos, sum_sin = calculate(np.pi*7/4)
print(real)
print(imaginary)
print(real-imaginary)
print(sum_cos)
print(sum_sin)
print(sum_cos+sum_sin)



sin_str = ''
for i in range(l):
    if abs(sin_coeff[i]) > 0.001:
        sin_str += str(round(sin_coeff[i], 3)) + 'sin' + str(i) + f'x*2\pi/{l} + '

cos_str = ''
for i in range(l):
    if abs(cos_coeff[i]) > 0.001:
        cos_str += str(round(cos_coeff[i], 3)) + 'cos' + str(i) + f'x*2\pi/{l} + '

print(sin_str, cos_str)



