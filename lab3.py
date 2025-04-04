import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox
from PyQt6.QtGui import QFont


class SignalViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置字体
        font = QFont("Arial", 10)
        self.setFont(font)

        main_layout = QVBoxLayout()

        # 幅值和周期输入
        input_layout = QHBoxLayout()
        amplitude_label = QLabel('Amplitude:')
        self.amplitude_input = QLineEdit()
        period_label = QLabel('Period:')
        self.period_input = QLineEdit()
        input_layout.addWidget(amplitude_label)
        input_layout.addWidget(self.amplitude_input)
        input_layout.addWidget(period_label)
        input_layout.addWidget(self.period_input)
        main_layout.addLayout(input_layout)

        # 信号类型选择
        self.signal_type_selector = QComboBox()
        self.signal_type_selector.addItems(['Discrete Signal', 'Periodic Signal'])
        main_layout.addWidget(self.signal_type_selector)

        # 生成信号按钮
        generate_button = QPushButton('Generate Signal')
        generate_button.clicked.connect(self.generate_signal)
        main_layout.addWidget(generate_button)

        self.setLayout(main_layout)
        self.setWindowTitle('Signal Viewer')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def generate_signal(self):
        try:
            amplitude = float(self.amplitude_input.text())
            period = float(self.period_input.text())
            signal_type = self.signal_type_selector.currentText()

            if signal_type == 'Discrete Signal':
                # 简单离散信号示例
                signal = amplitude * np.array([1, 2, 3, 4, 5])
                plt.stem(signal)
                plt.title('Discrete Signal')
            elif signal_type == 'Periodic Signal':
                # 简单周期信号示例（正弦波）
                t = np.linspace(0, 2 * np.pi, 100)
                signal = amplitude * np.sin(2 * np.pi * (1 / period) * t)
                plt.plot(t, signal)
                plt.title('Periodic Signal')

            plt.xlabel('Sample')
            plt.ylabel('Amplitude')
            plt.show()
        except ValueError:
            print("Please enter valid amplitude and period!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = SignalViewer()
    sys.exit(app.exec())
    