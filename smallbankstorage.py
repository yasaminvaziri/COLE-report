import matplotlib.pyplot as plt
import numpy as np

data = {
    "mpt": {
        10: 0.39,
        100: 7.07,
        1000: 108.67,
        10000: 1465.25,
        100000: 19046.84
    },
    "non_learn_cmi": {
        10: 0.61,
        100: 9.41,
        1000: 125.43,
        10000: 1734.58
    },
    "cole": {
        10: 0.15,
        100: 1.51,
        1000: 15.06,
        10000: 120.68,
        100000: 1125.18
    },
    "cole_star": {
        10: 0.15,
        100: 1.51,
        1000: 15.06,
        10000: 228.15,
        100000: 1575.77
    }
}

scales = [10, 100, 1000, 10000, 100000]
index_methods = list(data.keys())
n_indexes = len(index_methods)
bar_width = 0.2
x = np.arange(len(scales))
plt.figure(figsize=(12, 8))
colors = ['purple', 'lightgreen', 'yellow', 'orange']
hatches = ['x', 'x', '/', '\\', '\\']
for i, index_method in enumerate(index_methods):
    storage_sizes = [data[index_method].get(scale, 0) for scale in scales]
    bars = plt.bar(x + i * bar_width, storage_sizes, width=bar_width, color=colors[i % len(colors)], hatch=hatches[i],
                   label=index_method)
    for j, height in enumerate(storage_sizes):
        if height == 0:
            plt.scatter(x[j] + i * bar_width, 1, color='red', marker='x', s=100,
                        zorder=5)
plt.xlabel('Block height', fontsize=16)
plt.ylabel('Storage Size (MB)', fontsize=16)
plt.title('Storage Size vs. Across Block Height (Small Bank)', fontsize=16)
plt.xticks(x + bar_width * (n_indexes - 1) / 2, scales, fontsize=16)
plt.yscale('log')
plt.yticks(fontsize=16)
plt.legend(title="Indexing Method", fontsize=16, title_fontsize=16)
plt.show()
