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
        # Create the label.
        self.label = ttk.Label(self, text="PDF Merger", font=("Helvetica", 24))
        self.label.pack(pady=10)


# Check the file run directly or as a module.
if __name__ == "__main__":
    # Create the main window.
    App(title="PDF Merger", geometry="500x500", themename="darkly")
