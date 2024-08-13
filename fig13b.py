import matplotlib.pyplot as plt
import numpy as np

# Size Ratios
size_ratios = [2, 4, 6, 8, 10, 12]

# Latency data (ms)
latencies_cole = [
    [4.02, 4.28, 4.87, 5.95, 9.84]
]
latencies_cole_star = [
    [3.83, 4.36, 4.89, 4.71, 4.09]
]

# Expand latency data to match the number of size ratios
latencies_cole = latencies_cole * len(size_ratios)
latencies_cole_star = latencies_cole_star * len(size_ratios)

# Increase the figure size
plt.figure(figsize=(12, 8))

# Colors for the box plots
colors = ['purple', 'green']

# Create the first boxplot for COLE
box1 = plt.boxplot(latencies_cole, positions=np.array(size_ratios) - 0.2, widths=0.4, patch_artist=True, showfliers=True)
for patch in box1['boxes']:
    patch.set_facecolor(colors[0])

# Create the second boxplot for COLE*
box2 = plt.boxplot(latencies_cole_star, positions=np.array(size_ratios) + 0.2, widths=0.4, patch_artist=True, showfliers=True)
for patch in box2['boxes']:
    patch.set_facecolor(colors[1])

plt.yscale('log')
plt.ylim(1, 10**5)

plt.ylabel('Latency (ms)', fontsize=16)
plt.xlabel('Size Ratio', fontsize=16)
plt.xticks(size_ratios, size_ratios, fontsize=14)
plt.yticks(fontsize=14)
plt.title('Latency vs. Size Ratio (Small Bank)', fontsize=18)

plt.legend([box1["boxes"][0], box2["boxes"][0]], ['COLE', 'COLE*'], loc='upper right', fontsize=14)

plt.show()
