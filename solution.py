from collections import deque


def find_minimum_energy_needed(nb_intersection, shortcuts):
    dist = [-1] * (nb_intersection + 1)

    q = deque()
    dist[1] = 0
    q.append(1)

    while q:
        k = q.popleft()

        if k + 1 <= nb_intersection and dist[k + 1] == -1:
            dist[k + 1] = dist[k] + 1
            q.append(k + 1)

        if dist[shortcuts[k - 1]] == -1:
            dist[shortcuts[k - 1]] = dist[k] + 1
            q.append(shortcuts[k - 1])

        if k - 1 > 0 and dist[k - 1] == -1:
            dist[k - 1] = dist[k] + 1
            q.append(k - 1)

    for energy in range(1, nb_intersection + 1):
        print(dist[energy], end=" ")


if __name__ == "__main__":
    nb_intersection = int(input())
    shortcuts = list(map(int, input().split()))
    find_minimum_energy_needed(nb_intersection, shortcuts)
