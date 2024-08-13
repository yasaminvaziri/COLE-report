import os
import json


workloads = ["readwriteeven"]
# indexes = ["mpt", "cole", "cole_star", "non_learn_cmi"]
indexes = ["cole_star", "non_learn_cmi"]
scales = [1000, 10000, 100000, 1000000, 10000000]
# scales = [1000]

def get_storage_data(workload, index, scale, fanout, ratio, mem_size):
    #  JSON file name
    file_name = f"./{workload}/{workload}-{index}-{scale // 1000}k-fan{fanout}-ratio{ratio}-mem{mem_size}-storage.json"
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            storage_data = json.load(f)
            return storage_data.get("total_size", 0)
    return None


storage_results = {}
# loop through each workload, index, and scale to extract storage data
for workload in workloads:
    storage_results[workload] = {}
    for index in indexes:
        storage_results[workload][index] = {}
        for scale in scales:
            if index == "non_learn_cmi" and scale == 10000000:
                continue
            fanout_default = 4
            ratio_default = 4
            mem_size = 450000 if index in ["cole", "cole_star"] else 64
            storage_size = get_storage_data(workload, index, scale, fanout_default, ratio_default, mem_size)
            if storage_size is not None:
                storage_results[workload][index][scale] = storage_size
            else:
                storage_results[workload][index][scale] = "Database path not found or storage file not generated"
# print
for workload, indexes_data in storage_results.items():
    print(f"Workload: {workload}")
    for index, scales_data in indexes_data.items():
        print(f"  Index: {index}")
        for scale, storage_size in scales_data.items():
            if storage_size == "Database path not found or storage file not generated":
                print(f"    Scale: {scale}, {storage_size}")
            else:
                print(f"    Scale: {scale}, Storage Size: {storage_size / (1024 * 1024):.2f} MB")
