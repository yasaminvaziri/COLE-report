import matplotlib.pyplot as plt
import numpy as np

block_heights = [10, 100, 1000, 10000, 100000]
throughput_data = {
    "mpt": [11400.04, 12100.64, 11000.32, 7300.59, 4100.45],
    "non_learn_cmi": [3500.90, 4200.10, 4100.66, 1000.59, 0],
    "cole": [23800.69, 23200.82, 22300.68, 18100.93, 13200.42],
    "cole_star": [23600.61, 23300.74, 22000.22, 17800.25, 9300.95]
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
ax.set_title('Throughput vs. Block Height (read write even)', fontsize=16)
ax.set_xticks(positions + bar_width * 1.5)
ax.set_xticklabels(block_heights)
ax.set_yscale('log')
ax.set_ylim(10, 10**5)

ax.legend(title='Index')

plt.tight_layout()
plt.show()
