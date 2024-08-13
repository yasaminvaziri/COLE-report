import matplotlib.pyplot as plt
import numpy as np

block_heights = [10, 100, 1000, 10000, 100000]

latencies_mpt = [5.63, 6.89, 9.09, 14.10, 31.80]
latencies_cole = [4.02, 4.28, 4.87, 5.95, 9.84]
latencies_cole_star = [3.83, 4.36, 4.89, 4.71, 4.09]
latencies_cmi = [9.29, 11.36, 15.04, 75.62, 0]

latency_data = [latencies_mpt, latencies_cole, latencies_cole_star, latencies_cmi]
colors = ['purple', 'green', 'cyan', 'yellow']

plt.figure(figsize=(10, 6))
box = plt.boxplot(latency_data, patch_artist=True, showfliers=False)

for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.yscale('log')
plt.ylim(1, 10**5)
markers = ['o', 's', '^', 'D', 'v']
for i, height in enumerate(block_heights):
    plt.plot([1, 2, 3, 4], [latencies_mpt[i], latencies_cole[i], latencies_cole_star[i], latencies_cmi[i]],
             marker=markers[i], linestyle='', label=f'Block Height {height}')

plt.xticks([1, 2, 3, 4], ['MPT', 'COLE', 'COLE*', 'CMI'])
plt.ylabel('Latency (ms)')
plt.xlabel('Algorithm')
plt.title('Latency vs. Block Height (SmallBank)')
plt.legend(title="Block Heights")

plt.show()
