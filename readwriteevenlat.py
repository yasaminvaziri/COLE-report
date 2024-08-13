import matplotlib.pyplot as plt
import numpy as np


block_heights = [10, 100, 1000, 10000, 100000]

latencies_cole_star = [3.94, 3.94, 4.21, 5.26, 10.28]
latencies_cole = [3.90, 3.97, 4.14, 5.17, 7.22]
latencies_mpt = [8.49, 7.91, 8.75, 13.25, 23.75]
latencies_cmi = [27.58, 23.44, 23.69, 94.08, 0]

latency_data = [latencies_mpt, latencies_cole, latencies_cole_star, latencies_cmi]
colors = ['purple', 'green', 'cyan', 'yellow']

plt.figure(figsize=(10, 6))
box = plt.boxplot(latency_data, patch_artist=True, showfliers=False)
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
plt.yscale('log')
plt.ylim(1, 100000)
markers = ['o', 's', '^', 'D', 'v']
for i, height in enumerate(block_heights):
    plt.plot([1, 2, 3, 4], [latencies_mpt[i], latencies_cole[i], latencies_cole_star[i], latencies_cmi[i]],
             marker=markers[i], linestyle='', label=f'Block Height {height}')

plt.xticks([1, 2, 3, 4], ['MPT', 'COLE', 'COLE*', 'CMI'])
plt.ylabel('Latency (ms)')
plt.xlabel('Algorithm')
plt.title('Latency vs. Block Height (Write-Read even Workload)')

plt.legend(title="Block Heights")
plt.show()
