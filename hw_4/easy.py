import threading
import multiprocessing
from time import time

def n_fibbonachi(n):
    res = []
    for i in range(1, n + 1):
        if i == 1:
            res.append(0)
        elif i == 2:
            res.append(1)
        else:
            res.append(res[len(res) - 1] + res[len(res) - 2])
            
    res = res[-3:]

    return res

if __name__ == '__main__' :

    k = 120000

    start_time_threading = time()

    threads = []
    for _ in range(10):
        thread = threading.Thread(target=n_fibbonachi, args=(k,))
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()

    time_threading = time() - start_time_threading
    print(time_threading)

    start_time_multiprocessing = time()

    procs = []
    for _ in range(10):
        proc = multiprocessing.Process(target=n_fibbonachi, args=(k,))
        procs.append(proc)
        proc.start()
        
    for proc in procs:
        proc.join()

    time_processing = time() - start_time_multiprocessing
    print(time_processing)

    with open('artifacts/time_results.txt', 'w') as fout:
        fout.write(f'counting fibbonachi number {k}\n')
        fout.write(f'time for threading: {time_threading}\n')
        fout.write(f'time for multiprocessing: {time_processing}\n')
        
