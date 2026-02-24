from typing import Any, List, Optional

import customtkinter as ctk

from task_manager.core.task_service import TaskService


class TaskRow(ctk.CTkFrame):  # type: ignore
    """A custom frame representing a single task row in the UI."""

    def __init__(
        self,
        master: Any,
        index: int,
        task_text: str,
        completed: bool,
        on_toggle: Any,
        on_delete: Any,
    ):
        super().__init__(master, fg_color="transparent")
        self.index = index

        self.checkbox = ctk.CTkCheckBox(
            self, text="", width=30, command=lambda: on_toggle(self.index)
        )
        if completed:
            self.checkbox.select()
        self.checkbox.pack(side="left", padx=5)

        self.label = ctk.CTkLabel(self, text=task_text, anchor="w", font=ctk.CTkFont(size=14))
        self.label.pack(side="left", fill="x", expand=True)

        self.delete_btn = ctk.CTkButton(
            self,
            text="✕",
            width=30,
            height=20,
            corner_radius=10,
            fg_color="transparent",
            hover_color="#d11a2a",
            command=lambda: on_delete(self.index),
        )
        self.delete_btn.pack(side="right", padx=5)

        self.update_style(completed)

    def update_style(self, completed: bool) -> None:
        """Updates the style of the label based on completion status."""
        if completed:
            self.label.configure(text_color="#888888", font=ctk.CTkFont(overstrike=True))
        else:
            self.label.configure(text_color="#ffffff", font=ctk.CTkFont(overstrike=False))


class TaskApp(ctk.CTk):  # type: ignore
    """Main application window for the Daily Task Manager.

    This class handles the UI layout and user interactions, delegating
    business logic to the TaskService.
    """

    def __init__(self, service: Optional[TaskService] = None):
        """Initializes the application.

        Args:
            service (Optional[TaskService]): The task service to use.
        """
        super().__init__()

        self.service = service or TaskService()
        self.task_rows: List[TaskRow] = []

        self.setup_ui()
        self.refresh_task_list()

    def setup_ui(self) -> None:
        """Sets up the UI layout and widgets."""
        self.geometry("800x700")
        self.title("📝 Daily Task Manager")
        ctk.set_appearance_mode("dark")

        ctk.CTkLabel(
            self, text="📅 Daily Task Manager", font=ctk.CTkFont(size=28, weight="bold")
        ).pack(pady=20)

        self.scroll_frame = ctk.CTkScrollableFrame(self, width=600, height=400, corner_radius=15)
        self.scroll_frame.pack(pady=10)

        input_frame = ctk.CTkFrame(self, fg_color="transparent")
        input_frame.pack(pady=15)

        self.entry = ctk.CTkEntry(
            input_frame,
            width=450,
            height=40,
            font=ctk.CTkFont(size=14),
            placeholder_text="Write a new task here...",
        )
        self.entry.pack(side="left", padx=10)
        self.entry.bind("<Return>", self.add_task_event)

        ctk.CTkButton(input_frame, text="➕ Add Task", width=120, command=self.add_task_event).pack(
            side="right", padx=10
        )

    def add_task_event(self, event: Optional[Any] = None) -> None:
        """Handles the add task event.

        Args:
            event: The event object (optional).
        """
        task_text = self.entry.get().strip()
        if task_text:
            self.service.add_task(task_text)
            self.entry.delete(0, ctk.END)
            self.refresh_task_list()

    def toggle_task(self, index: int) -> None:
        """Toggles a task's completion status.

        Args:
            index (int): The index of the task.
        """
        self.service.toggle_task(index)
        self.update_task_styles()

    def delete_task(self, index: int) -> None:
        """Deletes a task.

        Args:
            index (int): The index of the task.
        """
        self.service.delete_task(index)
        self.refresh_task_list()

    def refresh_task_list(self) -> None:
        """Rebuilds the entire task list in the UI."""
        for row in self.task_rows:
            row.destroy()
        self.task_rows.clear()

        tasks = self.service.get_tasks()
        for i, task in enumerate(tasks):
            row = TaskRow(
                self.scroll_frame, i, task.text, task.completed, self.toggle_task, self.delete_task
            )
            row.pack(fill="x", pady=5)
            self.task_rows.append(row)

        self.update_task_styles()

    def update_task_styles(self) -> None:
        """Updates the visual appearance of tasks based on their completion status."""
        tasks = self.service.get_tasks()
        for i, row in enumerate(self.task_rows):
            if i < len(tasks):
                row.update_style(tasks[i].completed)

    def run(self) -> None:
        """Starts the application main loop."""
        self.mainloop()
