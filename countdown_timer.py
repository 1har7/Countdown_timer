import time
from threading import Thread, Event

class CountdownTimer(Thread):
    def __init__(self, duration):
        super().__init__()
        self.duration = duration  # Fixed assignment
        self.paused = False
        self.timer_running = False
        self._stop_event = Event()  # Fixed event initialization

    def run(self):
        self.timer_running = True
        start_time = time.time()
        end_time = start_time + self.duration

        while end_time - time.time() > 0 and not self._stop_event.is_set():
            if not self.paused:
                time_left = int(end_time - time.time())
                print(f"Time left: {time_left // 60:02d}:{time_left % 60:02d}")
                time.sleep(1)

        self.timer_running = False  # Mark timer as stopped


    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def reset(self):
        self.paused = False
        self.timer_running = False
        self._stop_event.set()

    def is_running(self):
        return self.timer_running

if __name__ == "__main__":
    timer = CountdownTimer(60)  # 60 seconds countdown
    timer.start()

    while timer.is_running():
        command = input("\nEnter command (p for pause/r for resume/rt for reset): ").strip().lower()
        time.sleep(0.5)  # small pause to avoid clashing with timer output

        # The following block needs to be indented to be part of the 'if' statement
        if command == 'p':
            timer.pause()
        elif command == 'r':
            timer.resume()
        elif command == 'rt':
            timer.reset()
            timer = CountdownTimer(60)  # Restart the timer
            timer.start()
