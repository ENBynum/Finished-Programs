#!usr/bin/env python3

from customtkinter import *
import datetime
import threading
import time
import re


def task_time(start, end) -> list[str]:
    prev_time = re.match(r"(\d{2}):(\d{2}):(\d{2})", start)
    prev_hour = int(prev_time.group(1))
    prev_min = int(prev_time.group(2))
    prev_sec = int(prev_time.group(3))

    curr_time = re.match(r"(\d{2}):(\d{2}):(\d{2})", end)
    curr_hour = int(curr_time.group(1))
    curr_min = int(curr_time.group(2))
    curr_sec = int(curr_time.group(3))

    task_hour = curr_hour - prev_hour
    if curr_min < prev_min:
        task_min = (curr_min - prev_min) + 60
        task_hour -= 1
    else:
        task_min = curr_min - prev_min
    if curr_sec < prev_sec:
        task_sec = (curr_sec - prev_sec) + 60
        task_min -= 1
    else:
        task_sec = curr_sec - prev_sec

    total_time = "{:02d}:{:02d}:{:02d}".format(task_hour, task_min, task_sec)

    return total_time


class MainApp(CTk):
    def __init__(self):
        super().__init__()
        self.title("DataAnnotation Work Tracker")
        self.iconbitmap("./assets/DataAnnotation Image.ico")
        self.minsize(width=350, height=200)
        self.maxsize(width=350, height=450)

        self.working = False
        self.project = ""
        self.start_time = "00:00:00"
        self.end_time = "00:00:00"
        self.current_task = 0
        self.previous_task_time = "00:00:00"
        self.current_time = "00:00:00"
        self.task_display_message = ""

        self.setup_interface("start")

    def setup_interface(self, page):
        try:
            self.app_frame.destroy()
        except:
            pass

        self.geometry("350x200+1000+0")
        self.app_frame = CTkFrame(
            self, fg_color="black", corner_radius=0
        ).place(x=0, y=0, relwidth=1, relheight=1)

        self.project_entry = CTkTextbox(
            self.app_frame, width=300, height=50, fg_color="lightgray",
            text_color="black", font=("arial", 14), wrap="word"
        )
        self.project_entry.insert("0.0", self.project)
        self.project_entry.place(x=25, y=25)
        if self.project != "":
            self.project_entry.configure(state="disabled")
        self.timer_display = CTkLabel(
            self.app_frame, width=300, height=50, fg_color="black",
            font=("arial", 24, "bold"), text_color="gray", text=self.current_time
        )
        self.timer_display.place(x=25, y=75)
        if page == "start":
            self.start_session_button = CTkButton(
                self.app_frame, width=150, height=50,
                fg_color="gray", hover_color="lightgray",
                text="START SESSION", text_color="black", font=("arial", 18, "bold"),
                command=self.start_session
            )
            self.start_session_button.place(x=100, y=125)
        elif page == "working":
            self.geometry("350x450+1000+0")
            self.submit_task_button = CTkButton(
                self.app_frame, width=125, height=50, fg_color="gray",
                hover_color="lightgray", text="SUBMIT TASK", text_color="black",
                font=("arial", 18, "bold"), command=self.submit_task
            )
            self.submit_task_button.place(x=33, y=125)
            self.void_task_button = CTkButton(
                self.app_frame, width=125, height=50,
                fg_color="gray", hover_color="lightgray",
                text="VOID TASK", text_color="black", font=("arial", 18, "bold"),
                command=self.reset_timer
            )
            self.void_task_button.place(x=192, y=125)
            self.completed_task_display = CTkTextbox(
                self.app_frame, width=300, height=150, fg_color="lightgray", border_width=1,
                border_color="black", corner_radius=0, font=("arial", 12), text_color="black",
                state="disabled"
            )
            self.completed_task_display.place(x=25, y=200)
            self.update_task_display()
            self.end_session_button = CTkButton(
                self.app_frame, width=150, height=50, fg_color="gray", hover_color="lightgray",
                text="END SESSION", text_color="black", font=("arial", 18, "bold"),
                command=self.end_session
            )
            self.end_session_button.place(x=100, y=375)
        elif page == "session_summary":
            self.geometry("350x375+1000+0")
            self.new_session_button = CTkButton(
                self.app_frame, width=150, height=50, fg_color="gray",
                hover_color="lightgray", text="NEW SESSION", text_color="black",
                font=("arial", 18, "bold"), command=self.start_session
            )
            self.new_session_button.place(x=100, y=125)
            self.completed_task_display = CTkTextbox(
                self.app_frame, width=300, height=150, fg_color="lightgray", border_width=1,
                border_color="black", corner_radius=0, font=("arial", 12), text_color="black",
                state="disabled"
            )
            self.completed_task_display.insert("0.0", self.task_display_message)
            self.completed_task_display.place(x=25, y=200)
            self.update_task_display()

    def update_task_display(self):
        self.completed_task_display.configure(state="normal")
        self.completed_task_display.delete("0.0", END)
        self.completed_task_display.insert(END, self.task_display_message)
        self.completed_task_display.configure(state="disabled")

    def reset_state(self):
        self.working = False
        self.project = ""
        self.start_time = "00:00:00"
        self.end_time = "00:00:00"
        self.current_task = 0
        self.previous_task_time = "00:00:00"
        self.current_time = "00:00:00"
        self.task_display_message = ""

    def start_session(self):
        self.reset_state()
        self.working = True

        self.start_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.project = self.project_entry.get("0.0", END).strip()
        self.task_display_message = (f"Project - {self.project_entry.get("0.0", END).strip()}\n"
                                     f"Session Start Time: {self.start_time}\n\n")

        self.timer_process = threading.Thread(target=self.timer, daemon=True)
        self.timer_process.start()

        self.setup_interface("working")

    def submit_task(self):
        self.current_task += 1
        task_work_time = task_time(self.previous_task_time, self.current_time)
        self.previous_task_time = self.current_time

        self.task_display_message += f"TASK {self.current_task} - {task_work_time}   ({self.previous_task_time})\n"
        self.update_task_display()

    def reset_timer(self):
        self.current_time = self.previous_task_time

    def end_session(self):
        self.working = False
        self.project_end_time = datetime.datetime.now().strftime("%H:%M:%S")

        self.task_display_message += f"\nSession End Time: {self.project_end_time}"
        self.update_task_display()

        self.setup_interface("session_summary")

    def timer(self):
        while self.working:
            time.sleep(1)

            curr_time = re.match(r"(\d{2}):(\d{2}):(\d{2})", self.current_time)
            curr_hour = int(curr_time.group(1))
            curr_min = int(curr_time.group(2))
            curr_sec = int(curr_time.group(3))

            curr_sec += 1
            if curr_sec == 60:
                curr_sec = 0
                curr_min += 1
            if curr_min == 60:
                curr_min = 0
                curr_hour += 1
            self.current_time = "{:02d}:{:02d}:{:02d}".format(curr_hour, curr_min, curr_sec)

            if self.working:
                self.timer_display.configure(text=self.current_time)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
