import matplotlib.pyplot as plt
import numpy as np

block_heights = [10, 100, 1000, 10000, 100000]
throughput_data = {
    "mpt": [21100.32, 21300.58, 21700.26, 21000.95, 21000.53],
    "non_learn_cmi": [9600.35, 7800.04, 7300.05, 9800.03, 8700.64],
    "cole": [44600.99, 45100.78, 45100.94, 45200.65, 45500.20],
    "cole_star": [41000.43, 44900.02, 45000.94, 45100.75, 45300.03]
}

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.2
positions = np.arange(len(block_heights))
colors = ['purple', 'green', 'orange', 'yellow']

hatches = ['x', 'x', '\\', '/']

for i, (index, color, hatch) in enumerate(zip(throughput_data, colors, hatches)):
    ax.bar(positions + i * bar_width, throughput_data[index], bar_width, label=index, color=color, hatch=hatch)

ax.set_xlabel('Block Height', fontsize=16)
ax.set_ylabel('Throughput (Transactions/Second)', fontsize=16)
ax.set_title('Throughput vs. Block Height (Read Only)', fontsize=18)
ax.set_xticks(positions + bar_width * 1.5)
ax.set_xticklabels(block_heights, fontsize=14)
ax.set_yscale('log')
ax.set_yticklabels(['10', '10^1', '10^2', '10^3', '10^4', '10^5'], fontsize=14)
ax.set_ylim(10, 10**5)
ax.legend(title='Index', fontsize=14, title_fontsize=16, bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
