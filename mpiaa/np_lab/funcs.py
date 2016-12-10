from mpiaa.np import max_clique


def custom_sum(l, get_key=lambda item: item):
    result = 0
    for i in l:
        result += get_key(i)
    return result

def list_of_sums(l, get_key=lambda item: item):
    all_combinations = max_clique.all_combinations(l)
    max_comb = []
    max_profit = 0
    for current in all_combinations:
        current_profit = custom_sum(current, get_key)
        if current_profit > max_profit:
            max_comb = current
            max_profit = current_profit

    return max_profit, max_comb