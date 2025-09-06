import tkinter as tk
import time

class DigitalStopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Stopwatch")
        self.running = False
        self.start_time = None
        self.elapsed_time = 0.0

        self.time_label = tk.Label(root, text="00:00:00:00", font=("Courier", 50), fg="yellow", bg="black")
        self.time_label.pack(padx=20, pady=20)

        button_frame = tk.Frame(root, bg="black")
        button_frame.pack(pady=10)

        self.start_button = tk.Button(button_frame, text="Start", font=("Arial", 16), command=self.start, width=8)
        self.start_button.grid(row=0, column=0, padx=5)

        self.pause_button = tk.Button(button_frame, text="Pause", font=("Arial", 16), command=self.pause_resume, width=8)
        self.pause_button.grid(row=0, column=1, padx=5)

        self.stop_button = tk.Button(button_frame, text="Stop", font=("Arial", 16), command=self.stop, width=8)
        self.stop_button.grid(row=0, column=2, padx=5)

        self.reset_button = tk.Button(button_frame, text="Reset", font=("Arial", 16), command=self.reset, width=8)
        self.reset_button.grid(row=0, column=3, padx=5)

    def update_time(self):
        if self.running:
            current_time = time.time()
            self.elapsed_time = current_time - self.start_time

        hours = int(self.elapsed_time // 3600)
        minutes = int((self.elapsed_time % 3600) // 60)
        seconds = int(self.elapsed_time % 60)
        milliseconds = int((self.elapsed_time * 100) % 100)  

        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}:{milliseconds:02d}"
        self.time_label.config(text=time_str)

        self.root.after(10, self.update_time)  

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True

    def pause_resume(self):
        if self.running:
            self.running = False
            self.pause_button.config(text="Resume")
        else:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self.pause_button.config(text="Pause")

    def stop(self):
        """Stops counting but keeps the current time displayed"""
        self.running = False
        self.pause_button.config(text="Pause")

    def reset(self):
        """Resets stopwatch to 00:00:00:00"""
        self.running = False
        self.elapsed_time = 0.0
        self.time_label.config(text="00:00:00:00")
        self.pause_button.config(text="Pause")


if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg='black')
    app = DigitalStopwatch(root)
    app.update_time()
    root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg='black')
    app = DigitalStopwatch(root)
    app.update_time()
    root.mainloop()
