import numpy as np
import matplotlib.pyplot as plt

# f(x, y) = ax^2 + by^2 + cxy + dx + ey + f


def make_function(a, b, c, d, e, f):
    return {'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f}


def calculate_gradient(x, y, coefficient):
    return [
        2.0 * coefficient['a'] * x + coefficient['c'] * y + coefficient['d'],
        2.0 * coefficient['b'] * y + coefficient['c'] * x + coefficient['e']
    ]


def get_function_value(x, y, function):
    return function['a'] * x ** 2 + \
        function['b'] * y ** 2 + \
        function['c'] * x * y + \
        function['d'] * x + \
        function['e'] * y + \
        function['f']


def get_function_points_value(x, y, function):
    res = []
    for i in range(len(x)):
        res.append(get_function_value(x[i], y[i], function))
    return res


def dichotomy(x, y, grad, function):
    left = 0.0001
    right = 0.09
    eps = 0.00001
    while abs(right - left) > eps:
        a = (left * 2 + right) / 3
        b = (left + right * 2) / 3
        f_a = get_function_value(x - a * grad[0], y - a * grad[1], function)
        f_b = get_function_value(x - b * grad[0], y - b * grad[1], function)
        if f_a < f_b:
            right = b
        else:
            left = a
    return (left + right) / 2


def constant_learning_rate(x, y, grad, function):
    return 0.06


def gradient_descent(start_x, start_y, function, learning_rate, eps):
    prev_x = start_x
    prev_y = start_y
    condition = 1
    res = [(start_x, start_y)]

    while condition:
        grad = calculate_gradient(prev_x, prev_y, function)
        alpha = learning_rate(prev_x, prev_y, grad, function)
        new_x = prev_x - alpha * grad[0]
        new_y = prev_y - alpha * grad[1]
        res += [(new_x, new_y)]
        if abs(prev_x - new_x) <= eps and abs(prev_y - new_y) <= eps:
            break
        prev_x = new_x
        prev_y = new_y
    return res


f1 = make_function(1.0, 1.0, 0.0, 0.0, 0.0, 0.0)
f2 = make_function(2.0, 6.0, 0.0, 15.0, 2.0, 0.0)

epsilon = 0.00001

res1 = gradient_descent(-5.0, -5.0, f1, constant_learning_rate, epsilon)
res2 = gradient_descent(-5.0, -5.0, f1, dichotomy, epsilon)

# draw function graph
t = np.linspace(-20, 10, 100)
X, Y = np.meshgrid(t, t)
Z = np.array(get_function_points_value(X, Y, f2))
fig, ax1 = plt.subplots(1)
fig = plt.figure().add_subplot(projection='3d')
fig.plot_surface(X, Y, Z)
##

points = np.array(res2)
# draw gradient move
ax1.plot(points[:, 0], points[:, 1], 'o-')
ax1.grid()
ax1.contour(X, Y, Z, levels=sorted([get_function_value(p[0], p[1], f2) for p in points]))
##

plt.show()
