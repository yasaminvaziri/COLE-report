import matplotlib.pyplot as plt
import numpy as np

tx_in_block = 100
data = {
    "mpt": {
        "scale": [1000, 10000, 100000, 1000000, 10000000],
        "storage": [217.79, 218.52, 218.57, 219.00, 223.38]
    },
    "non_learn_cmi": {
        "scale": [1000, 10000, 100000, 1000000, 10000000],
        "storage": [229.89, 228.39, 229.60, 233.74, 0]
    },
    "cole": {
        "scale": [1000, 10000, 100000, 1000000, 10000000],
        "storage": [25.74, 25.74, 25.74, 25.74, 25.74]
    },
    "cole_star": {
        "scale": [1000, 10000, 100000, 1000000, 10000000],
        "storage": [25.74, 25.74, 25.74, 25.74, 25.74]
    }
}

for index in data:
    data[index]['block_height'] = [s // tx_in_block for s in data[index]['scale']]
fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.18
positions = np.arange(len(data['cole']['block_height']))
colors = ['purple', 'green', '#FFC107', 'yellow']
hatches = ['x', 'x', '\\', '/']
for i, (index, color, hatch) in enumerate(zip(data, colors, hatches)):
    bars = ax.bar(positions + i * bar_width, data[index]['storage'], bar_width, label=index, color=color, hatch=hatch)
    for j, storage_value in enumerate(data[index]['storage']):
        if storage_value == 0:
            ax.scatter(positions[j] + i * bar_width, 10 ** -1, color='red', marker='x', s=200, zorder=5)
ax.set_xlabel('Block Height', fontsize=16)
ax.set_ylabel('Storage Consumption (MB)', fontsize=16)
ax.set_title('Block Height vs Storage Consumption (Read-Only)', fontsize=16)

ax.set_xticks(positions + bar_width * 1.5)
ax.set_xticklabels(data['cole']['block_height'])
ax.set_yscale('log')

ax.set_ylim(10**-1, 10**5)
ax.legend(title='Index')
plt.tight_layout()
plt.show()
