
cost = {
    "helix": 60.0,
    "lucca": 67.0,
    "must": 23.0,
    "derian": 0.0
}

n = len(cost)

cost_each = {
    "helix": cost["helix"] / (n - 1),
    "lucca": cost["lucca"] / n,
    "must": cost["must"] / n,
    "derian": cost["derian"] / n
}