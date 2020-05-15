# python3


def parent(i):
    return int((i - 1) / 2)


def leftchild(i):
    return 2 * i + 1

def rightchild(i):
    return 2 * i + 2

def siftup(H, i):
    while i > 0 and H[parent(i)] > H[i]:
        H[parent(i)], H[i] = H[i], H[parent(i)]
        i = parent(i)
def siftdown(H, i):
    min = i
    if leftchild(i) <= len(H)-1 and H[leftchild(i)] < H[min]:
        min = leftchild(i)
    if rightchild(i) <= len(H)-1 and H[rightchild(i)] < H[min]:
        min = rightchild(i)
    if i != min:
        H[i], H[min] = H[min], H[i]
        return i, min








def build_heap(H):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    # swaps = []
    # for i in range(len(data)):
    #     for j in range(i + 1, len(data)):
    #         if data[i] > data[j]:
    #             swaps.append((i, j))
    #             data[i], data[j] = data[j], data[i]
    # return swaps

    swaps = []
    size = len(H)-1
    i = int(size/2)
    while i >= 0 :
        j =i
        while rightchild(i) <= size:
            pair = siftdown(H, i)
            if pair != None:
                swaps.append(pair)
                i = pair[1]
        i = j-1
    return  swaps



def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
