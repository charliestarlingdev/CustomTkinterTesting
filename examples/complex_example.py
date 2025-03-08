import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("themes/red.json")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Rapid Fire :: Asset Tracker")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create left sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Asset Tracker", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # Right Sidebar
        self.right_sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.right_sidebar_frame.grid(row=0, column=2, rowspan=6, sticky="nsew")
        self.right_sidebar_frame.grid_rowconfigure(4, weight=1)
        self.right_logo_label = customtkinter.CTkLabel(self.right_sidebar_frame, text="Filters", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.right_logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        switch = customtkinter.CTkSwitch(master=self.right_sidebar_frame, text=f"CO2     ")
        switch.grid(row=1, column=0, padx=(5,10), pady=(20, 0))
        
        switch = customtkinter.CTkSwitch(master=self.right_sidebar_frame, text=f"H20     ")
        switch.grid(row=2, column=0, padx=(5, 10), pady=(20, 0))
        switch = customtkinter.CTkSwitch(master=self.right_sidebar_frame, text=f"Wet Chem")
        switch.grid(row=3, column=0, padx=20, pady=(20, 0))
        switch = customtkinter.CTkSwitch(master=self.right_sidebar_frame, text=f"Show all")
        switch.grid(row=4, column=0, padx=20, pady=(30, 0))

        # set default values
        self.sidebar_button_3.configure(state="disabled", text="Disabled CTkButton")
 
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
  

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")


if __name__ == "__main__":
    app = App()
    app.mainloop()
