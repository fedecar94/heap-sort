def heapify(array, last, pivot):
    largest = pivot
    left = 2 * pivot + 1
    right = 2 * pivot + 2

    if left < last and array[pivot] < array[left]:
        largest = left

    if right < last and array[largest] < array[right]:
        largest = right

    if largest != pivot:
        array[pivot], array[largest] = array[largest], array[pivot]
        heapify(array, last, largest)


def heap_sort(array):
    size = len(array)

    for pivot in range(size // 2, -1, -1):
        heapify(array, size, pivot)

    for last in range(size - 1, 0, -1):
        array[last], array[0] = array[0], array[last]

        heapify(array, last, 0)


if __name__ == '__main__':
    import random

    randomlist = [random.randint(1, 30) for x in range(0, 10)]

    print(randomlist)
    heap_sort(randomlist)
    print(randomlist)
