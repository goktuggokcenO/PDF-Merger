import customtkinter
from file_selected import Selected_File


class Files(customtkinter.CTkScrollableFrame):
    def __init__(self, master) -> None:
        super().__init__(master=master)
        self.pack(side="top", fill="both", expand=True, padx=10, pady=10)
        self.selected_files = []
        self.create_widgets()

    def create_widgets(self) -> None:
        # Create the label if there is noe files.
        if len(self.selected_files) == 0:
            self.label = customtkinter.CTkLabel(
                master=self,
                text="No file selected.",
            )
            self.label.pack(side="top", fill="x", padx=5, pady=5)

    def add_file(self, file_path: str) -> None:
        selected_file = Selected_File(self, file_path)
        self.selected_files.append(selected_file)

        # Destroy the label.
        if len(self.selected_files) >= 1:
            self.label.destroy()
