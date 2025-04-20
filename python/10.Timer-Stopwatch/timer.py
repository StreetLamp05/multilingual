"""
10. Timer/Stopwatch
- [ ] Use `time` module to track seconds
- [ ] Implement countdown or stopwatch mode
"""

import time
import threading
import re

def main():

    choice = input("Choose timer/ stopwatch mode (timer) (stopwatch):")
    if (choice == "timer"):
        duration = time_parser(input("How long should the timer be? mm:ss"))
        threading.Thread(target =start_timer(duration), daemon=True).start()
    elif (choice == "stopwatch"):
        stop_event = threading.Event()
        threading.Thread(target=start_stopwatch, args = (stop_event, ), daemon=True).start()
        input("Press enter to stop the stopwatch:\n")
        stop_event.set()
    else:
        print("invalid choice")



def start_stopwatch(stop_event):
    print("Starting stopwatch:")
    start_time = time.time()
    elapsed_time = 0
    while not stop_event.is_set():
        print("", end='\r')
        elapsed_time = time.time() - start_time
        time.sleep(1)
        print(f"Elapsed time: {"%.2f" % elapsed_time } seconds")
    return

def start_timer(duration : int):
    start_time = time.time()
    elapsed_time = 0
    while duration > elapsed_time:
        print(f"Remaining time: {"%.2f" % (int(duration) - int(elapsed_time))} seconds")
        elapsed_time = time.time() - start_time
        time.sleep(1)
    print(f"Timer for {duration} over!")
    return

"""
takes a time in format mm:ss and converts it into number of seconds
"""
def time_parser(time: str) -> int:
    seconds_pattern = r"^(\d+)$" # ss*
    min_pattern = r"^\d+:\d\d$" # mm:ss
    if re.match(seconds_pattern, time):
        return int(time)
    elif re.match(min_pattern, time):
        minutes, seconds = time.split(":")
        return int(minutes) * 60 + int(seconds)
    else:
        raise Exception("Invalid time format (seconds) or (mm:ss)")


if __name__ == "__main__":
    main()