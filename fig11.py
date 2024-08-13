import matplotlib.pyplot as plt
import numpy as np

block_heights = [10 ** 1, 10 ** 2, 1000, 10000, 100000]
throughput_mpt = {
    10: [21100.32, 11400.04, 7900.22],
    100: [21300.58, 12100.64, 8500.77],
    1000: [21700.26, 11000.32, 6400.83],
    10000: [21000.95, 7300.59, 4500.23],
    100000: [21000.53, 4100.45, 1800.85]
}
throughput_cmi = {
    10: [9600.35, 3500.90, 2200.94],
    100: [7800.04, 4200.10, 3400.34],
    1000: [7300.05, 4100.66, 2800.10],
    10000: [9800.03, 1000.59, 600.40],
    100000: [8700.64, 0, 0]
}
throughput_cole = {
    10: [44600.99, 23800.69, 15900.48],
    100: [45100.78, 23200.82, 15600.52],
    1000: [45100.94, 22300.68, 14800.23],
    10000: [45200.65, 18100.93, 12100.40],
    100000: [45500.20, 13200.42, 8100.72]
}
throughput_cole_star = {
    10: [41000.43, 23600.61, 16200.40],
    100: [44900.02, 23300.74, 15800.79],
    1000: [45000.94, 22000.22, 14700.60],
    10000: [45100.75, 17800.25, 11000.21],
    100000: [45300.03, 9300.95, 4900.78]
}

throughput_data = [throughput_mpt, throughput_cmi, throughput_cole, throughput_cole_star]
colors = ['purple', 'blue', 'green', 'cyan']
labels = ['MPT', 'CMI', 'COLE', 'COLE*']
hatches = ['x', '', 'x', '']
bar_width = 0.15
fig, axes = plt.subplots(1, len(block_heights), figsize=(15, 6), sharey=True)
for i, block_height in enumerate(block_heights):
    r1 = np.arange(len(throughput_mpt[block_height]))
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width for x in r2]
    r4 = [x + bar_width for x in r3]
    axes[i].bar(r1, throughput_mpt[block_height], color=colors[0], width=bar_width, edgecolor='grey', hatch=hatches[0],
                label=labels[0])
    axes[i].bar(r2, throughput_cmi[block_height], color=colors[1], width=bar_width, edgecolor='grey', hatch=hatches[1],
                label=labels[1])
    axes[i].bar(r3, throughput_cole[block_height], color=colors[2], width=bar_width, edgecolor='grey', hatch=hatches[2],
                label=labels[2])
    axes[i].bar(r4, throughput_cole_star[block_height], color=colors[3], width=bar_width, edgecolor='grey',
                hatch=hatches[3], label=labels[3])

    for j, val in enumerate(throughput_cmi[block_height]):
        if val == 0:
            axes[i].scatter(r2[j], 10, color='red', marker='x', s=100,
                            zorder=5)
    axes[i].set_title(f'Block Height {block_height}', fontsize=18)
    axes[i].set_xlabel('Workloads', fontsize=18)
    axes[i].set_xticks([r + 1.5 * bar_width for r in range(len(throughput_mpt[block_height]))])
    axes[i].set_xticklabels(['RO', 'RW', 'WO'], fontsize=18)
    axes[i].set_yscale('log')
    axes[i].set_ylim(10, 10 ** 5)
axes[0].set_ylabel('Throughput (TPS)', fontsize=18)
axes[0].legend(loc='upper right')
plt.tight_layout()
plt.show()
