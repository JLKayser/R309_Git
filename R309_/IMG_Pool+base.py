import time
import threading
import concurrent.futures
import requests
import multiprocessing

'''def task():
    print(f"Task starts for 1 second")
    time.sleep(1)
    print(f"Task ends")
if __name__ == '__main__':
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)
    p1.start()
    p2.start()
    p1.join() # obliger d'attendre sinon le multiprocessing execute directement sans attendre la fin.
    p2.join()
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")'''

'''if __name__ == '__main__':
    try:
        a = float(input("a: "))
        b = float(input("b: "))
        res = a/b
    except:
        print("An exception occurs")
    else:
        print(res)'''


'''def task(i):
    print(f"Task {i} starts")
    time.sleep(1)
    print(f"Task {i} ends")
start = time.perf_counter()
for i in range(11):
    thread = threading.Thread(target=task,args=[i])
    thread.start()
    thread.join() #attendre la fin du thread
end = time.perf_counter()
print(f"Tasks ended in {round(end - start, 2)} second(s)")'''



img_urls = ['https://www.fredzone.org/wp-content/uploads/2017/12/Bob-leponge.jpg']

def download_image(img_url):   # pool de threads
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[len(img_url.split('/'))-1]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")
start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)
    end = time.perf_counter()
print(f"Tasks ended in {round(end - start, 2)} second(s)")




