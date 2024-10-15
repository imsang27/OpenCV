import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1차원 가우시안 함수
def gaussian_1d(x, sigma):
    return (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(- (x**2) / (2 * sigma**2))

# 2차원 가우시안 함수
def gaussian_2d(x, y, sigma):
    return (1 / (2 * np.pi * sigma**2)) * np.exp(- (x**2 + y**2) / (2 * sigma**2))

# 1차원 가우시안 그리기
x = np.linspace(-6, 6, 100)
sigma = 1.0
y_1d = gaussian_1d(x, sigma)

plt.figure(figsize=(10, 5))

# 1차원 가우시안 함수 그래프
plt.subplot(1, 2, 1)
plt.plot(x, y_1d, color='b')
plt.title('1D')
plt.grid(True)

# 2차원 가우시안 그리기
x_2d = np.linspace(-6, 6, 100)
y_2d = np.linspace(-6, 6, 100)
X, Y = np.meshgrid(x_2d, y_2d)
Z = gaussian_2d(X, Y, sigma)

# 3D 그래프 생성
ax = plt.subplot(1, 2, 2, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title('2D')

plt.tight_layout()
plt.show()