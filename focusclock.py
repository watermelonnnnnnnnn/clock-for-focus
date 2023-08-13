# clock-for-focus
import tkinter as tk
import time
import winsound

window = tk.Tk()
window.title("专注时钟")
window.geometry("300x200")

label_time = tk.Label(window, text="00:00", font=("Arial", 40))
label_time.pack(pady=20)
label_info = tk.Label(window, text="点击开始按钮开始计时", font=("Arial", 16))
label_info.pack()

button_start = tk.Button(window, text="开始", command=lambda: start_timer(25, "green", "专注"))
button_start.pack(side=tk.LEFT, padx=20, pady=10)
button_stop = tk.Button(window, text="停止", command=lambda: window.after_cancel(timer_id))
button_stop.pack(side=tk.RIGHT, padx=20, pady=10)

timer_id = None
focus_count = 0

def timer(seconds, color, info):
    global timer_id, focus_count
    label_time.config(text=time.strftime("%M:%S", time.gmtime(seconds)), bg=color)
    label_info.config(text=info)
    if seconds > 0:
        timer_id = window.after(1000, timer, seconds-1, color, info)
    else:
        winsound.PlaySound("alarm.wav", winsound.SND_ASYNC)
        if info == "专注":
            focus_count += 1
            start_timer(15 if focus_count == 4 else 5, "red" if focus_count == 4 else "yellow", "长休息" if focus_count == 4 else "休息")
        else:
            focus_count = 0 if info == "长休息" else focus_count
            start_timer(25, "green", "专注")

def start_timer(seconds, color, info):
    global timer_id
    if timer_id:
        window.after_cancel(timer_id)
    timer(seconds, color, info)

window.mainloop()
