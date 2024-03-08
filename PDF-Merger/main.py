# Libraraies.
import ttkbootstrap as ttk
from tkinter import filedialog


# Create the main window.
class App(ttk.Window):
    # Constructor.
    def __init__(self, title: str, geometry: str, themename: str):
        super().__init__(themename=themename)
        self.title(title)
        self.geometry(geometry)
        self.create_widgets()
        self.mainloop()

    # Create the widgets.
    def create_widgets(self):
        # Create the buttons frame.
        self.buttons_frame = ttk.Frame(self)
        self.buttons_frame.pack(side="top", fill="x", padx=10, pady=10)

        # Create the add button.
        self.add_button = ttk.Button(
            self.buttons_frame,
            text="Add",
            style="primary",
            width=15,
            command=self.add_file,
        )
        self.add_button.pack(side="left")

        # Create the merge button.
        self.merge_button = ttk.Button(
            self.buttons_frame, text="Merge", style="success", width=15
        )
        self.merge_button.pack(side="right")

        # Create the file element.
        self.file_element = Files(self, background="secondary")

    # Add a file.
    def add_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("PDF Files", "*.pdf")], title="Select a file."
        )
        if file_path:
            self.file_element.add_file(file_path)


# Create the file element.
class Files(ttk.Frame):
    # Constructor.
    def __init__(self, master, background):
        super().__init__(master=master, bootstyle=background)
        self.pack(side="top", fill="both", expand=True)
        self.selected_files = []
        self.create_widgets()

    # Create the widgets.
    def create_widgets(self):
        if len(self.selected_files) == 0:
            self.label = ttk.Label(
                self,
                text="No file selected.",
                font="helvetica 12",
                background="#444444",
                anchor="center",
            )
            self.label.pack(side="top", fill="x", padx=5, pady=5)

    # Add a file.
    def add_file(self, file_path: str):
        selected_file = Selected_File(self, file_path)
        self.selected_files.append(selected_file)

        # Destroy the label.
        if len(self.selected_files) >= 1:
            self.label.destroy()


# Create the selected file.
class Selected_File(ttk.Frame):
    # Constructor.
    def __init__(self, master, file_path: str):
        super().__init__(master=master)
        self.pack(side="top", fill="x", padx=5, pady=5)
        self.file_path = file_path
        self.create_widgets()

    # Create the widgets.
    def create_widgets(self):
        # Create the label.
        self.label = ttk.Label(self, text=self.file_path)
        self.label.pack(side="left", fill="x", padx=5, pady=5)

        # Create the remove button.
        self.remove_button = ttk.Button(
            self, text="Remove", style="danger", width=8, command=self.remove_file
        )
        self.remove_button.pack(side="right", padx=5, pady=5)

    # Remove the file.
    def remove_file(self):
        self.destroy()
        self.master.selected_files.remove(self)

        # Create the label.
        if len(self.master.selected_files) == 0:
            self.master.label = ttk.Label(
                self.master,
                text="No file selected.",
                font="helvetica 12",
                background="#444444",
                anchor="center",
            )
            self.master.label.pack(side="top", fill="x", padx=5, pady=5)


# Check the file run directly or as a module.
if __name__ == "__main__":
    # Create the main window.
    App(title="PDF Merger", geometry="500x500", themename="darkly")
