import matplotlib.pyplot as plt
import numpy as np

# Block heights corresponding to each scale
block_heights = [10, 100, 1000, 10000, 100000]

# Latencies data for each algorithm
latencies_cole_star = [2.21, 1.98, 1.97, 1.97, 1.96]
latencies_cole = [2.01, 1.97, 1.96, 1.96, 1.95]
latencies_mpt = [4.51, 4.44, 4.36, 4.50, 4.51]
latencies_cmi = [10.15, 12.57, 13.44, 9.96, 11.17]

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
plt.title('Latency vs. Block Height (Read Only Workload)')
plt.legend(title="Block Heights")
plt.show()
