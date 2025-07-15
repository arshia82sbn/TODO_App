import customtkinter as ctk
import json
import os

# ===============================
# Setup main window
# ===============================
root = ctk.CTk()
root.geometry("800x700")
root.title("📝 Daily Task Manager")
ctk.set_appearance_mode("dark")

# ===============================
# Constants
# ===============================
TASKS_FILE = "tasks.json"
tasks = []

# ===============================
# Load tasks from JSON safely
# ===============================
def load_tasks():
    global tasks
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as f:
                tasks.extend(json.load(f))
        except json.JSONDecodeError:
            tasks.clear()  # Clear if error found
            with open(TASKS_FILE, "w") as f:
                json.dump([], f)

# ===============================
# Save tasks to JSON
# ===============================
def save_tasks():
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

# ===============================
# Add new task
# ===============================
def add_task(event=None):
    task_text = entry.get().strip()
    if task_text:
        task_id = len(tasks)
        tasks.append({"text": task_text, "completed": False})
        add_task_ui(task_id, task_text)
        entry.delete(0, ctk.END)
        save_tasks()

# ===============================
# Add task to the UI
# ===============================
def add_task_ui(task_id, task_text):
    frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")
    frame.pack(fill="x", pady=5)

    checkbox = ctk.CTkCheckBox(frame, text="", width=30, command=lambda: toggle_task(task_id))
    checkbox.pack(side="left", padx=5)

    label = ctk.CTkLabel(frame, text=task_text, anchor="w", font=ctk.CTkFont(size=14))
    label.pack(side="left", fill="x", expand=True)

    delete_btn = ctk.CTkButton(
        frame, text="✕", width=30, height=20, corner_radius=10,
        fg_color="transparent", hover_color="#d11a2a",
        command=lambda: delete_task(task_id)
    )
    delete_btn.pack(side="right", padx=5)

    task_frames.append(frame)

# ===============================
# Toggle task state
# ===============================
def toggle_task(task_id):
    tasks[task_id]["completed"] = not tasks[task_id]["completed"]
    update_task_styles()
    save_tasks()

# ===============================
# Delete task
# ===============================
def delete_task(task_id):
    tasks.pop(task_id)
    for frame in task_frames:
        frame.destroy()
    task_frames.clear()
    refresh_task_list()
    save_tasks()

# ===============================
# Rebuild UI after deletion
# ===============================
def refresh_task_list():
    for i, task in enumerate(tasks):
        add_task_ui(i, task["text"])
    update_task_styles()

# ===============================
# Update visual style of tasks
# ===============================
def update_task_styles():
    for i, frame in enumerate(task_frames):
        label = frame.winfo_children()[1]
        if tasks[i]["completed"]:
            label.configure(text_color="#888888", font=ctk.CTkFont(overstrike=True))
        else:
            label.configure(text_color="#ffffff", font=ctk.CTkFont(overstrike=False))

# ===============================
# UI Layout
# ===============================
ctk.CTkLabel(root, text="📅 Daily Task Manager", font=ctk.CTkFont(size=28, weight="bold")).pack(pady=20)

scroll_frame = ctk.CTkScrollableFrame(root, width=600, height=400, corner_radius=15)
scroll_frame.pack(pady=10)

input_frame = ctk.CTkFrame(root, fg_color="transparent")
input_frame.pack(pady=15)

entry = ctk.CTkEntry(
    input_frame, width=450, height=40, font=ctk.CTkFont(size=14),
    placeholder_text="Write a new task here..."
)
entry.pack(side="left", padx=10)
entry.bind("<Return>", add_task)

ctk.CTkButton(input_frame, text="➕ Add Task", width=120, command=add_task).pack(side="right", padx=10)

# ===============================
# Load previous tasks
# ===============================
task_frames = []
load_tasks()
refresh_task_list()

root.mainloop()