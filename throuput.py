import matplotlib.pyplot as plt
import numpy as np


block_heights = [10, 100, 1000, 10000, 100000]
throughputs_mpt = [17100.97, 14000.81, 10700.44, 6900.75, 3100.18]
throughputs_cmi = [10500.34, 8600.44, 6500.45, 1300.19, 0]
throughputs_cole = [23600.84, 22200.74, 19600.36, 16100.67, 9900.08]
throughputs_cole_star = [24700.40, 21800.97, 19500.49, 20300.11, 23300.34]
bar_width = 0.15
log_block_heights = np.log10(block_heights)
positions_mpt = log_block_heights - bar_width * 1.5
positions_cmi = log_block_heights - bar_width * 0.5
positions_cole = log_block_heights + bar_width * 0.5
positions_cole_star = log_block_heights + bar_width * 1.5
plt.figure(figsize=(12, 6))
colors = ['purple', 'green', 'orange', 'yellow']
hatches = ['x', '', '\\', '//']
bars_mpt = plt.bar(positions_mpt, throughputs_mpt, width=bar_width, color=colors[0], hatch=hatches[0], label='MPT')
bars_cmi = plt.bar(positions_cmi, throughputs_cmi, width=bar_width, color=colors[1], hatch=hatches[1], label='CMI')
bars_cole = plt.bar(positions_cole, throughputs_cole, width=bar_width, color=colors[2], hatch=hatches[2], label='COLE')
bars_cole_star = plt.bar(positions_cole_star, throughputs_cole_star, width=bar_width, color=colors[3], hatch=hatches[3], label='COLE*')
for i, height in enumerate(throughputs_cmi):
    if height == 0:
        plt.scatter(positions_cmi[i], 1, color='red', marker='x', s=100, zorder=5)

plt.xlabel('Block Height', fontsize=16)
plt.ylabel('Throughput (transactions/second)', fontsize=16)
plt.title('Block Height vs Throughput', fontsize=16)
plt.yscale('log')
plt.yticks([1, 10, 100, 1000, 10000, 100000],
           ['10^0', '10^1', '10^2', '10^3', '10^4', '10^5'])
plt.xticks(log_block_heights, block_heights)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize='small')


plt.show()
