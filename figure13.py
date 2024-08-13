import matplotlib.pyplot as plt
import numpy as np


size_ratios = [2, 4, 6, 8, 10, 12]

throughput_cole = [23600.84, 22200.74, 19600.36, 16100.67, 9900.08, 8500.23]
throughput_cole_star = [24700.40, 21800.97, 19500.49, 20300.11, 23300.34, 19800.76]
plt.figure(figsize=(7, 6))
x = np.arange(len(size_ratios))
width = 0.35
plt.bar(x - width/2, throughput_cole, width, label='COLE', color='purple', hatch='x')
plt.bar(x + width/2, throughput_cole_star, width, label='COLE*', color='green', hatch='/')
plt.yscale('log')
plt.ylim(1, 10**5)
plt.ylabel('Throughput (TPS)')
plt.xlabel('Size Ratio')
plt.xticks(x, size_ratios)
plt.legend(loc='upper right')
plt.title('Throughput vs. Size Ratio (Small Bank)')
plt.show()
