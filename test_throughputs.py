import json
import os

def compute_throughput_and_latency(ts_file_path):
    with open(ts_file_path, "r") as f:
        blocks = [json.loads(line) for line in f.readlines()]
    total_transactions = len(blocks)

    total_time_ns = blocks[-1]["end_ts"] - blocks[0]["start_ts"]
    total_time_sec = total_time_ns / 1e9
    throughput = total_transactions / total_time_sec
    total_latency_ns = sum(block["elapse"] for block in blocks)
    average_latency_ms = (total_latency_ns / total_transactions) / 1e6
    return throughput, average_latency_ms

def compute_for_specific_file():
    # example path:
    ts_file_path = "/home/yasmine/cole/exp/readonly/readonly-non_learn_cmi-1k-fan4-ratio4-mem64-ts.json"

    if os.path.exists(ts_file_path):
        throughput, average_latency_ms = compute_throughput_and_latency(ts_file_path)
        print(f"Throughput: {throughput:.2f} transactions/second")
        print(f"Average Latency: {average_latency_ms:.2f} ms")
    else:
        print(f"Timestamp file not found: {ts_file_path}")

if __name__ == "__main__":
    compute_for_specific_file()
