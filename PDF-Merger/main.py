# Libraraies.
import customtkinter
import PyPDF2
from tkinter import filedialog
from tkinter import messagebox


# Create the main window.
class App(customtkinter.CTk):
    # Constructor.
    def __init__(self, title: str, geometry: str):
        super().__init__()
        customtkinter.set_appearance_mode("dark")
        self.title(title)
        self.geometry(geometry)
        self.create_widgets()
        self.mainloop()

    # Create the widgets.
    def create_widgets(self):
        # Create the buttons frame.
        self.buttons_frame = customtkinter.CTkFrame(self)
        self.buttons_frame.pack(side="top", fill="x", padx=10, pady=10)

        # Create the add button.
        self.add_button = customtkinter.CTkButton(
            master=self.buttons_frame,
            text="Add",
            width=80,
            command=self.add_file,
        )
        self.add_button.pack(side="left", padx=5, pady=5)

        # Create the merge button.
        self.merge_button = customtkinter.CTkButton(
            master=self.buttons_frame,
            text="Merge",
            width=80,
            command=self.merge_files,
        )
        self.merge_button.pack(side="right", padx=5, pady=5)

        # Create the title label.
        self.title_label = customtkinter.CTkLabel(self.buttons_frame, text="PDF Merger")
        self.title_label.pack(side="top", fill="x", padx=5, pady=5)

        # Create the file element.
        self.file_element = Files(self)

    # Add a file.
    def add_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("PDF Files", "*.pdf")], title="Select a file."
        )
        if file_path:
            self.file_element.add_file(file_path)

    # Merge the files.
    def merge_files(self):
        # Check if there are at least two files selected.
        if len(self.file_element.selected_files) < 2:
            messagebox.showerror(
                "Error", "Select at least two files to merge.", parent=self
            )

        # Merge the files.
        else:
            # Create a PDF writer object.
            pdf_writer = PyPDF2.PdfWriter()

            # Iterate over the selected files.
            for selected_file in self.file_element.selected_files:
                # Open each file and add its pages to the writer object.
                with open(selected_file.file_path, "rb") as file:
                    pdf_reader = PyPDF2.PdfReader(file)
                    for page_num in range(len(pdf_reader.pages)):
                        page = pdf_reader.pages[page_num]
                        pdf_writer.add_page(page)

            # Save the merged PDF to a file.
            output_file_path = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF Files", "*.pdf")],
                title="Save merged PDF",
            )
            if output_file_path:
                with open(output_file_path, "wb") as output_file:
                    pdf_writer.write(output_file)


# Create the file element.
class Files(customtkinter.CTkFrame):
    # Constructor.
    def __init__(self, master):
        super().__init__(master=master)
        self.pack(side="top", fill="both", expand=True, padx=10, pady=10)
        self.selected_files = []
        self.create_widgets()

    # Create the widgets.
    def create_widgets(self):
        # Create the label.
        if len(self.selected_files) == 0:
            self.label = customtkinter.CTkLabel(
                master=self,
                text="No file selected.",
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
class Selected_File(customtkinter.CTkFrame):
    # Constructor.
    def __init__(self, master, file_path: str):
        super().__init__(master=master)
        self.pack(side="top", fill="x", padx=5, pady=5)
        self.file_path = file_path
        self.create_widgets()

    # Create the widgets.
    def create_widgets(self):
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

        # Create the label.
        self.label = customtkinter.CTkLabel(master=self, text=self.file_path)
        self.label.pack(side="left", fill="x", padx=5, pady=5)

    # Remove the file.
    def remove_file(self):
        self.destroy()
        self.master.selected_files.remove(self)

        # Create the label.
        if len(self.master.selected_files) == 0:
            self.master.label = customtkinter.CTkLabel(
                master=self.master, text="No file selected."
            )
            self.master.label.pack(side="top", fill="x", padx=5, pady=5)


# Check the file run directly or as a module.
if __name__ == "__main__":
    # Create the main window.
    App(title="PDF Merger", geometry="500x500")
