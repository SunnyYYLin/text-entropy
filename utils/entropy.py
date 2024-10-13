import math
from collections import Counter
import matplotlib.pyplot as plt
from tqdm import tqdm

def cal_entropy(data: list[str]|str, verbose: bool = True) -> float:
    print("Counting data...")
    counter = Counter(data)
    total = len(data)
    entropy = 0
    for count in tqdm(counter.values(), desc="Calculating Entropy", disable=not verbose):
        prob = count / total
        entropy -= prob * math.log2(prob)
    return entropy

def cal_incremental_entropy(counter: Counter, total: int) -> float:
    """
    计算当前计数器状态下的熵值
    """
    entropy = 0
    for count in counter.values():
        prob = count / total
        entropy -= prob * math.log2(prob)
    return entropy

def entropy_curve(data: list[str], step: int) -> tuple[list[int], list[float]]:
    # 累积计数器和初始熵值
    counter = Counter()
    total = 0
    entropy_list = []
    data_sizes = []

    # 遍历数据并按步长增加数据量
    for size in tqdm(range(0, len(data), step), desc="Calculating Entropy Curve"):
        # 更新累积计数器并记录新的数据量
        new_data = data[size:size + step]
        counter.update(new_data)
        total += len(new_data)

        # 计算当前数据量的熵值
        entropy = cal_incremental_entropy(counter, total)
        data_sizes.append(total)
        entropy_list.append(entropy)

    return data_sizes, entropy_list