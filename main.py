import psutil
import tkinter as tk
from tkinter import ttk, messagebox
from collections import deque
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

psutil.cpu_percent(interval=None)

root = tk.Tk()
root.title("Thermal Monitor Pro")
root.geometry("850x650")

# Labels
cpu_label = tk.Label(root, text="CPU Usage: ", font=("Arial", 18, "bold"))
cpu_label.pack(pady=5)

status_label = tk.Label(root, text="", font=("Arial", 14))
status_label.pack()

alert_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
alert_label.pack()

suggestion_label = tk.Label(root, text="", font=("Arial", 12))
suggestion_label.pack(pady=5)

# Graph
cpu_data = deque([0]*20, maxlen=20)

fig, ax = plt.subplots(figsize=(5, 2))
line, = ax.plot(cpu_data)
ax.set_ylim(0, 100)
ax.set_title("CPU Usage Over Time")

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Table
columns = ("Process", "CPU %", "Usage Bar")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)

tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

def update_data():
    cpu = psutil.cpu_percent(interval=None)

    # Status
    if cpu < 30:
        status = "COOL 🟢"
        color = "green"
    elif cpu < 70:
        status = "WARM 🟡"
        color = "orange"
    else:
        status = "HOT 🔴"
        color = "red"

    cpu_label.config(text=f"CPU Usage: {cpu}%")
    status_label.config(text=f"Status: {status}", fg=color)

    # Popup alert
    if cpu > 85:
        messagebox.showwarning("Warning", "High CPU Usage!")

    # Suggestion system
    if cpu > 70:
        suggestion_label.config(text="Suggestion: Close Chrome or heavy apps", fg="red")
    else:
        suggestion_label.config(text="")

    # Graph update
    cpu_data.append(cpu)
    line.set_ydata(cpu_data)
    line.set_xdata(range(len(cpu_data)))
    ax.relim()
    ax.autoscale_view()
    canvas.draw()

    # Clear table
    for row in tree.get_children():
        tree.delete(row)

    processes = []
    for p in psutil.process_iter(['name','cpu_percent']):
        try:
            processes.append((p.info['name'], p.info['cpu_percent']))
        except:
            pass

    processes = sorted(processes, key=lambda x: x[1], reverse=True)

    # Insert processes with visual bars
    for proc in processes[:5]:
        name = proc[0] if proc[0] else "Unknown"
        cpu_usage = proc[1]

        bar = "█" * int(cpu_usage / 5)

        tree.insert("", tk.END, values=(name, f"{cpu_usage}%", bar))

    root.after(2000, update_data)

update_data()
root.mainloop()