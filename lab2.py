import numpy as np
import matplotlib.pyplot as plt

# 生成信号参数
fs = 500  # 采样频率 (Hz)
T = 1.0   # 信号持续时间 (秒)
t = np.linspace(0, T, int(fs * T), endpoint=False)

# 生成合成信号：50Hz + 120Hz 正弦波叠加
f1, f2 = 50, 120
signal = np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)

# 计算 FFT
N = len(signal)
fft_result = np.fft.fft(signal)
fft_freq = np.fft.fftfreq(N, d=1.0 / fs)
fft_magnitude = np.abs(fft_result) / N

# 只取正频率部分（DC 和 Nyquist 分量不乘以 2）
positive_freq_idx = fft_freq >= 0
fft_freq_positive = fft_freq[positive_freq_idx]
fft_magnitude_positive = fft_magnitude[positive_freq_idx].copy()
fft_magnitude_positive[1:-1] *= 2

# 绘图
plt.figure(figsize=(12, 5))

# 时域信号
plt.subplot(1, 2, 1)
plt.plot(t[:200], signal[:200])
plt.title('Time Domain Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# 频域信号
plt.subplot(1, 2, 2)
plt.plot(fft_freq_positive, fft_magnitude_positive)
plt.title('Frequency Domain (FFT)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.xlim(0, 200)

plt.tight_layout()
plt.show()
