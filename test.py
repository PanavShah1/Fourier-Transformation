import numpy as np

l1 = np.array([1, 1, 1, 1])
l2 = np.array([1, -1j, -1, 1j])
l3 = np.array([1, -1, 1, -1])
l4 = np.array([1, 1j, -1, -1j])

y = np.array([2, 4, 6, 8])

c1 = np.dot(l1, y)
c2 = np.dot(l2, y)
c3 = np.dot(l3, y)
c4 = np.dot(l4, y)

def calculate(t):
    value = 1/4*(c1*np.exp(0j*t) + c2*np.exp(1j*t) + c3*np.exp(2j*t) + c4*np.exp(3j*t))
    # print(value)
    print()
    real = np.real(value)
    imaginary = np.imag(value)
    return (real+imaginary)


# def calculate(t):
#     value = 1/4*(c1*np.cos(t) + c2*np.cos(2*t) + c3*np.cos(3*t) + c4*np.cos(4*t)) + \
#             1j*1/4*(c1*np.sin(t) - c2*np.sin(2*t) + c3*np.sin(3*t) - c4*np.sin(4*t))
#     return value


print(c1)
print(c2)
print(c3)
print(c4)
print()
# print(np.exp(np.pi * 1j))
# print(calculate(np.pi*0))

for i in range(4):
    print(calculate(np.pi*i/2))

