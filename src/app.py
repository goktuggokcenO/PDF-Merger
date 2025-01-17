import customtkinter
import PyPDF2
from tkinter import filedialog
from tkinter import messagebox
from components.file_list import Files


class App(customtkinter.CTk):
    def __init__(self, title: str, geometry: str) -> None:
        super().__init__()
        customtkinter.set_appearance_mode("dark")
        self.title(title)
        self.minsize(300, 150)
        self.geometry(geometry)
        self.create_widgets()
        self.mainloop()

    def create_widgets(self) -> None:
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

    def add_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("PDF Files", "*.pdf")], title="Select a file."
        )
        if file_path:
            self.file_element.add_file(file_path)

    def merge_files(self):
        # Check if there are at least two files selected.
        if len(self.file_element.selected_files) == 0:
            messagebox.showerror(
                "Error", "Select at least one files to merge.", parent=self
            )

        # Merge the files.
        else:
            # Create a PDF writer object.
            pdf_writer = PyPDF2.PdfWriter()

            # Iterate over the selected files.
            for selected_file in self.file_element.selected_files:
                # Open each file and add its pages to the writer object.
                with open(selected_file.file_path, "rb") as file:
                    if selected_file.is_page_selected:
                        for page_num in selected_file.selected_pages:
                            page = selected_file.pdf_reader.pages[page_num]
                            pdf_writer.add_page(page)
                    else:
                        for page_num in range(len(selected_file.pdf_reader.pages)):
                            page = selected_file.pdf_reader.pages[page_num]
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
