# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])



#Define Min_Heap_Customized
def parent(i):
    return int((i - 1)/2)

def left_child(i):
    return 2*i + 1

def right_child(i):
    return 2*i + 2

def Siftdown(H, i):
    min = i
    if left_child(i) <= len(H)-1 and H[left_child(i)].next_free_time < H[i].next_free_time:
        min = left_child(i)
    if right_child(i) <= len(H)-1 and H[right_child(i)].next_free_time < H[i].next_free_time:
        min = right_child(i)
    if i != min:
        H[i], H[min] = H[min], H[i]


def Getdirection(H, i):
    min = i
    if left_child(i) <= len(H) - 1 and H[left_child(i)].next_free_time < H[i].next_free_time:
        min = left_child(i)
    if right_child(i) <= len(H) - 1 and H[right_child(i)].next_free_time < H[i].next_free_time:
        min = right_child(i)
    return min


def build_Min_Heap(Array):
    size = int(len(Array)/2)
    for i in range(size-1, -1, -1):
        Siftdown(Array, i)



def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    # result = []
    # next_free_time = [0] * n_workers
    # for job in jobs:
    #     next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
    #     result.append(AssignedJob(next_worker, next_free_time[next_worker]))
    #     next_free_time[next_worker] += job
    #################################################
    # Define Worker Pri_Queue
    Worker = namedtuple("Worker", ["Label", "next_free_time"])
    Workers = []
    result = []
    for i in range(0, n_workers):
        Workers.append(Worker(i, 0))
    build_Min_Heap(Workers)
    for job in jobs:
        result.append(Workers[0])
        work_1 = Workers[0]
        Workers[0].next_free_time = Workers[0].next_free_time + job
        k = 0
        while right_child(k) <= len(Workers)-1:
            min = Getdirection(Workers, k)
            Siftdown(Workers, k)
            k = min




    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.Label, job.next_free_time)


if __name__ == "__main__":
    main()
