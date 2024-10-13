from collections import Counter

def pdf_curve(data: list[str], lower: int, upper: int) -> tuple[list[int], list[float]]:
    counter = Counter(data)
    sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    sorted_counter = sorted_counter[lower:upper]
    rank = [i for i in range(lower, upper)]
    total_count = sum([count for _, count in sorted_counter])
    freq = [count / total_count for _, count in sorted_counter]
    return rank, freq

def vocab_size_curve(data: list[str], step: int) -> tuple[list[int], list[int]]:
    vocab = set()
    vocab_sizes = []
    data_sizes = []
    for size in range(step, len(data), step):
        vocab.update(data[size-step:size])
        vocab_sizes.append(len(vocab))
        data_sizes.append(size)
    return data_sizes, vocab_sizes