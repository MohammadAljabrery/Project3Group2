from .buttons import *
from .sliders import *
from .label import *
from .optionboxes import *
from .switches import *
from .classes import *


main_window = customtkinter.CTk()

main_frame = customtkinter.CTkFrame(main_window)  # Main Frame
ilcs_frame = customtkinter.CTkFrame(main_window)  # Internal Light Control System Frame
elcs_frame = customtkinter.CTkFrame(main_window)  # External Light Control System Frame
clr_frame = customtkinter.CTkFrame(main_window)   # Control Room Frame
lab_frame = customtkinter.CTkFrame(main_window)   # Laboratory Frame
sr_frame = customtkinter.CTkFrame(main_window)    # Storage Room Frame
dp_frame = customtkinter.CTkFrame(main_window)    # Data Processing Room Frame
cr_frame = customtkinter.CTkFrame(main_window)    # Communication Room Frame
cq_frame = customtkinter.CTkFrame(main_window)    # Crew Quarters Frame
mr_frame = customtkinter.CTkFrame(main_window)    # Medical Room Frame
or_frame = customtkinter.CTkFrame(main_window)    # Observation Room Frame
sl_frame = customtkinter.CTkFrame(main_window)    # Spotlight Frame
nl_frame = customtkinter.CTkFrame(main_window)    # Navigational Lights Frame

frame_manager = Frames(main_window)

frame_manager.rcconfigure(main_frame)
frame_manager.rcconfigure(ilcs_frame)
frame_manager.rcconfigure(elcs_frame)
frame_manager.rcconfigure(clr_frame)
frame_manager.rcconfigure(lab_frame)
frame_manager.rcconfigure(sr_frame)
frame_manager.rcconfigure(dp_frame)
frame_manager.rcconfigure(cr_frame)
frame_manager.rcconfigure(cq_frame)
frame_manager.rcconfigure(mr_frame)
frame_manager.rcconfigure(or_frame)
frame_manager.rcconfigure(or_frame)
frame_manager.rcconfigure(sl_frame)
frame_manager.rcconfigure(nl_frame)


buttons(main_frame, frame_manager, ilcs_frame, elcs_frame,
        clr_frame, lab_frame, sr_frame, dp_frame, cr_frame,
        cq_frame, mr_frame, or_frame, sl_frame, nl_frame)

sliders(main_frame, ilcs_frame, elcs_frame,
        clr_frame, lab_frame, sr_frame, dp_frame, cr_frame,
        cq_frame, mr_frame, or_frame, sl_frame, nl_frame)

labels(main_frame, ilcs_frame, elcs_frame,
       clr_frame, lab_frame, sr_frame, dp_frame, cr_frame,
       cq_frame, mr_frame, or_frame, sl_frame, nl_frame)

optionbox(clr_frame, lab_frame, sr_frame, dp_frame, cr_frame,
          cq_frame, mr_frame, or_frame, sl_frame, nl_frame)

switches(main_frame, ilcs_frame, elcs_frame,
         clr_frame, lab_frame, sr_frame, dp_frame, cr_frame,
         cq_frame, mr_frame, or_frame, sl_frame, nl_frame)


main_frame.mainloop()
