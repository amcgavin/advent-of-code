import collections


import aocd


def part_1(data):
    graph = {}
    for line in data:
        s, r = line.split(":")
        graph[s.strip()] = tuple(x.strip() for x in r.split(" ") if x.strip())

    def dfs(node, seen):
        if node == "out":
            return 1
        if node in seen:
            return 0
        ns = frozenset(seen.union({node}))
        return sum(dfs(n, ns) for n in graph[node])

    return dfs("you", frozenset())


def part_2(data):
    graph = {}
    nodes = set()
    rev = collections.defaultdict(int)
    for line in data:
        s, r = line.split(":")
        s = s.strip()
        graph[s] = tuple(x.strip() for x in r.split(" ") if x.strip())
        nodes.add(s)
        for c in graph[s]:
            rev[c] += 1
            nodes.add(c)

    q = [n for n in nodes if rev[n] == 0]
    topo = []

    while q:
        node = q.pop(0)
        topo.append(node)
        for nn in graph.get(node, []):
            rev[nn] -= 1
            if rev[nn] == 0:
                q.append(nn)

    def dp_to(fr, to):
        dp = {n: 0 for n in nodes}
        dp[to] = 1

        for n in reversed(topo):
            if n == to:
                continue
            dp[n] = sum(dp[ne] for ne in graph.get(n, []))

        return dp[fr]

    return dp_to("svr", "fft") * dp_to("fft", "dac") * dp_to("dac", "out")


def main():
    data = [x for x in aocd.get_data(day=11, year=2025).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
