import timeit
a = []
for i in range(9):
    a.append(int(input('Введите элементы матрицы построчно: ')))
p = a[0]*a[4]*a[8]+a[1]*a[5]*a[6]+a[3]*a[7]*a[2]-(a[2]*a[4]*a[6]+a[1]*a[3]*a[8]+a[0]*a[5]*a[7])
if p == 0:
    print('Определитель равен 0. Обратной матрицы не существует')
else:
    f = [1/p*(a[4]*a[8]-a[7]*a[5]), -1/p*(a[3]*a[8]-a[6]*a[5]), 1/p*(a[3]*a[7]-a[6]*a[4])]
    b = [-1/p*(a[1]*a[8]-a[7]*a[2]), 1/p*(a[0]*a[8]-a[6]*a[2]), -1/p*(a[0]*a[7]-a[6]*a[1])]
    c = [1/p*(a[1]*a[5]-a[4]*a[2]), -1/p*(a[0]*a[5]-a[3]*a[2]), 1/p*(a[0]*a[4]-a[3]*a[1])]
    f[1], b[0] = b[0], f[1]
    f[2], c[0] = c[0], f[2]
    c[1], b[2] = b[2], c[1]
    print(f, b, c, sep='\n')
print(timeit.timeit())