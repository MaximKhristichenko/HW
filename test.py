n = int(input())
tasks = []
for _ in range(n):
    t, d = map(int, input().split())
    tasks.append((t,d))

# Сортируем по дедлайну
tasks.sort(key=lambda x: x[1])

heap = Heap([])
total_time = 0

for t, d in tasks:
    heap.append(t)
    total_time += t
    if total_time > d:
        removed = heap.get_max()   # удаляем самую долгую задачу
        heap.pop()
        total_time -= removed

print(heap.size)