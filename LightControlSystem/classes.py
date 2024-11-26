import customtkinter


class Frames:
    def __init__(self, frame):
        self.frame = frame
        self.frame.title("Light Control System")
        self.frame.attributes('-fullscreen', True)
        self.frame.geometry("1920x1080")

    def switch_frames(self, frame1, frame2):
        frame1.forget()
        frame2.pack(expand=1, fill="both")

    def rcconfigure(self, frame):

        for i in range(30):
            # Making rows
            frame.grid_rowconfigure(i, weight=1)

            # Making Columns
            frame.grid_columnconfigure(i, weight=1)
class Buttons:

    def __init__(self, frame, frame_manager):
        self.frame = frame
        self.frame_manager = frame_manager

    # Method for back button
    def back_button(self, frame, frame1, frame2):
        back_button_top_left = customtkinter.CTkButton(frame, text="<-", fg_color="red", width=50)
        back_button_top_left.bind("<ButtonRelease>", lambda event: self.frame_manager.switch_frames(frame1, frame2))
        back_button_top_left.grid(row=0, column=0, padx=20, pady=20, sticky="nw")

    # Method to create other buttons
    def create_buttons(self, frame, text, fg_color, width, row, column, pady, padx, frame1, frame2):
        frame_buttons = customtkinter.CTkButton(frame, text=text, fg_color=fg_color, width=width)
        frame_buttons.bind("<Double-Button-1>", lambda event: self.frame_manager.switch_frames(frame1, frame2))
        frame_buttons.grid(row=row, column=column, pady=pady, padx=padx)


class Sliders:
    def create_slider(self, frame, row, column, pady, padx):
        label = customtkinter.CTkLabel(frame, text="0%")
        label.grid(row=2, column=1, pady=5, padx=5)
        slider = customtkinter.CTkSlider(frame, from_=0, to=100, command=lambda value: self.update_label(label, value))
        slider.grid(row=row, column=column, pady=pady, padx=padx)

    def update_label(self, label, value):
        label.configure(text=f"{int(float(value))}%")

class Labels:
    def create_label(self, frame, text, row, column, padx, pady, sticky):
        label_fonts = customtkinter.CTkFont(family="Courier New", size=18, weight="normal", underline=True)
        label = customtkinter.CTkLabel(frame, text=text, font=label_fonts)
        label.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)

class OptionBox:

    def create_option_box(self, frame, values, row, column, padx, pady):
        box = customtkinter.CTkOptionMenu(frame, values=values)
        box.grid(row=row, column=column, padx=padx, pady=pady)
        return box




class Switch:
    def switcher(self, switch_label, switch_var):
        switch_label.configure(text=switch_var.get())

    def create_switch(self, frame, row, column, pady, padx):
        switch_var = customtkinter.StringVar(value="on")
        switch = customtkinter.CTkSwitch(frame, fg_color="green", command=lambda: self.switcher(switch_label, switch_var),
                                         variable=switch_var, onvalue="on", offvalue="off", text="")
        switch.grid(row=row, column=column, pady=pady, padx=padx, sticky="ne")

        switch_label = customtkinter.CTkLabel(frame, text="")
        switch_label.grid(row=0, column=30, pady=0, padx=0, sticky="ne")




# If I didn't use lambda the function will execute directly without even clicking the button
