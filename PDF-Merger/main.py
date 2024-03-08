# Libraraies.
import ttkbootstrap as ttk


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
        # Create the buttons and the frame that contains them.
        self.buttons_frame = ttk.Frame(self)
        self.buttons_frame.pack(side="top", fill="x", padx=10, pady=10)

        self.add_button = ttk.Button(
            self.buttons_frame, text="Add", style="primary", width=15
        )
        self.add_button.pack(side="left")

        self.merge_button = ttk.Button(
            self.buttons_frame, text="Merge", style="success", width=15
        )
        self.merge_button.pack(side="right")

        # Create the file element.
        self.file_element = Files(self)


# Create the file element.
class Files(ttk.Frame):
    # Constructor.
    def __init__(self, master):
        super().__init__(master=master)
        self.pack(side="top", fill="both", expand=True, padx=10, pady=10)
        self.create_widgets()

    # Create the widgets.
    def create_widgets(self):
        self.configure(bootstyle="warning")


# Check the file run directly or as a module.
if __name__ == "__main__":
    # Create the main window.
    App(title="PDF Merger", geometry="500x500", themename="darkly")
