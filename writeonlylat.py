import matplotlib.pyplot as plt
import numpy as np

block_heights = [10, 100, 1000, 10000, 100000]
latencies_cole_star = [5.83, 5.94, 6.40, 8.67, 19.65]
latencies_cole = [5.93, 6.01, 6.35, 7.85, 11.82]
latencies_mpt = [12.30, 11.30, 15.02, 21.58, 52.56]
latencies_cmi = [43.26, 28.76, 35.10, 155.85, 0]

latency_data = [latencies_mpt, latencies_cole, latencies_cole_star, latencies_cmi]

colors = ['purple', 'green', 'cyan', 'yellow']
plt.figure(figsize=(10, 6))
box = plt.boxplot(latency_data, patch_artist=True, showfliers=False)
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.yscale('log')
plt.ylim(1, 10**3)
markers = ['o', 's', '^', 'D', 'v']
for i, height in enumerate(block_heights):
    plt.plot([1, 2, 3, 4], [latencies_mpt[i], latencies_cole[i], latencies_cole_star[i], latencies_cmi[i]],
             marker=markers[i], linestyle='', label=f'Block Height {height}')

plt.xticks([1, 2, 3, 4], ['MPT', 'COLE', 'COLE*', 'CMI'])

plt.ylabel('Latency (ms)')
plt.xlabel('Algorithm')
plt.title('Latency vs. Block Height (Write Only Workload)')
plt.legend(title="Block Heights")
plt.show()
