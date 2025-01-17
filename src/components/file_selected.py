import customtkinter
import PyPDF2


class Selected_File(customtkinter.CTkFrame):
    def __init__(self, master, file_path: str) -> None:
        super().__init__(master=master)
        self.pack(side="top", fill="x", padx=5, pady=5)
        self.file_path = file_path
        self.is_page_selected = False
        self.selected_pages = []
        self.pdf_reader = PyPDF2.PdfReader(file_path)
        self.create_widgets()

    def create_widgets(self) -> None:
        # Create the remove button.
        self.remove_button = customtkinter.CTkButton(
            master=self,
            text="Remove",
            width=60,
            command=self.remove_file,
            fg_color="#e74c3c",
            hover_color="#c0392b",
        )
        self.remove_button.pack(side="right", padx=5, pady=5)

        # Select the page number.
        self.select_page_number_button = customtkinter.CTkButton(
            master=self, text="Edit", command=self.select_page_number, width=60
        )
        self.select_page_number_button.pack(side="right", padx=5, pady=5)

        # Create the file path label.
        self.label = customtkinter.CTkLabel(master=self, text=self.file_path)
        self.label.pack(side="left", fill="x", padx=5, pady=5)

    def remove_file(self):
        self.destroy()
        self.master.selected_files.remove(self)

        # Create the label if no file is left.
        if len(self.master.selected_files) == 0:
            self.master.label = customtkinter.CTkLabel(
                master=self.master, text="No file selected."
            )
            self.master.label.pack(side="top", fill="x", padx=5, pady=5)

    def select_page_number(self) -> None:
        self.select_page_window = customtkinter.CTkToplevel(self.master.master)
        self.select_page_window.title("Select Page Number")
        self.select_page_window.geometry("300x300")

        # Create the select page number button.
        select_button = customtkinter.CTkButton(
            self.select_page_window,
            text="Selects",
            command=lambda: self.get_selected_pages(checkboxes),
        )
        select_button.pack(side="bottom", fill="x", padx=5, pady=5)

        # Create the scrollable frame.
        pages = customtkinter.CTkScrollableFrame(self.select_page_window)
        pages.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        # Iterate over the pages.
        checkboxes = []
        for page in range(len(self.pdf_reader.pages)):
            # Create the checkbox.
            checkbox = customtkinter.CTkCheckBox(
                master=pages, text="Page {}".format(page + 1)
            )
            checkbox.pack(side="top", fill="x", padx=5, pady=5)
            checkboxes.append(checkbox)

    def get_selected_pages(self, checkboxes: list) -> None:
        if len(checkboxes) == 0:
            self.select_page_window.destroy()
            return

        self.selected_pages = []
        for checkbox in checkboxes:
            if checkbox.get():
                self.selected_pages.append(int(checkbox._text.split()[1]) - 1)
                self.is_page_selected = True
        self.select_page_window.destroy()
