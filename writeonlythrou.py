import matplotlib.pyplot as plt
import numpy as np

block_heights = [10, 100, 1000, 10000, 100000]
throughput_data = {
    "mpt": [7900.22, 8500.77, 6400.83, 4500.23, 1800.85],
    "non_learn_cmi": [2200.94, 3400.34, 2800.10, 600.40, 0],
    "cole": [15900.48, 15600.52, 14800.23, 12100.40, 8100.72],
    "cole_star": [16200.40, 15800.79, 14700.60, 11000.21, 4900.78]


}

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.2
positions = np.arange(len(block_heights))
colors = ['purple', 'green', 'orange', 'yellow']
hatches = ['x', 'x', '\\', '/']
for i, (index, color, hatch) in enumerate(zip(throughput_data, colors, hatches)):
    ax.bar(positions + i * bar_width, throughput_data[index], bar_width, label=index, color=color, hatch=hatch)
    for j, value in enumerate(throughput_data[index]):
        if value == 0:
            ax.scatter(positions[j] + i * bar_width, 10, color='red', marker='x', s=200, zorder=5)
ax.set_xlabel('Block Height', fontsize=16)
ax.set_ylabel('Throughput (Transactions/Second)', fontsize=16)
ax.set_title('Throughput vs. Block Height (write only)', fontsize=16)

ax.set_xticks(positions + bar_width * 1.5)
ax.set_xticklabels(block_heights)
ax.set_yscale('log')
ax.set_ylim(10, 10**5)
ax.legend(title='Index')
plt.tight_layout()
plt.show()
