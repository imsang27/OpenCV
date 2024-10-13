import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, multivariate_normal

# 평균과 표준편차 설정
mu, sigma = 0, 2

# x 값 생성
x = np.linspace(-6, 6, 100)

# y 값 계산 (scipy.stats.norm.pdf 사용)
y = norm.pdf(x, mu, sigma)

# 그래프 그리기
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Probability density')

# 평균 벡터와 공분산 행렬 설정
mean = np.array([0, 0])
cov = np.array([[1, 0], [0, 2]])

# x, y 값 생성
x, y = np.meshgrid(np.linspace(-6, 6, 100), np.linspace(-6, 6, 100))

# 2차원 좌표를 1차원 벡터로 변환
pos = np.empty(x.shape + (2,))
pos[:, :, 0] = x
pos[:, :, 1] = y

# 확률 밀도 계산 (scipy.stats.multivariate_normal.pdf 사용)
rv = multivariate_normal(mean, cov)
z = rv.pdf(pos)

# 3차원 그래프 그리기
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis', linewidth=0)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
plt.show()