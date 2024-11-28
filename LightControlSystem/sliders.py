from .classes import *

def sliders(main_frame, ilcs_frame, elcs_frame,
            clr_frame, lab_frame, sr_frame, dp_frame, cr_frame,
            cq_frame, mr_frame, or_frame, sl_frame, nl_frame):

    slider = Sliders()
    slider.create_slider(sl_frame, 2, 0, 5, 5)  # Slider to change light intensity in spotlight frame
    slider.create_slider(clr_frame, 2, 0, 5, 5)  # Slider to change brightness of light in control room
    slider.create_slider(lab_frame, 2, 0, 5, 5)  # Slider to change brightness of light in laboratory
    slider.create_slider(sr_frame, 2, 0, 5, 5)  # Slider to change brightness of light in storage room
    slider.create_slider(dp_frame, 2, 0, 5, 5)  # Slider to change brightness of light in Data Processing Room
    slider.create_slider(cr_frame, 2, 0, 5, 5)  # Slider to change brightness of light in Communication Room
    slider.create_slider(cq_frame, 2, 0, 5, 5)  # Slider to change brightness of light in Crew Quarters
    slider.create_slider(mr_frame, 2, 0, 5, 5)  # Slider to change brightness of light in Medical Room
    slider.create_slider(or_frame, 2, 0, 5, 5)  # Slider to change brightness of light in Observation Room
    slider.create_slider(nl_frame, 2, 0, 5, 5)  # Slider to change brightness of  navigation lights

