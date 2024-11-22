from classes import *

def optionbox(clr_frame, lab_frame, sr_frame, dp_frame, cr_frame,
              cq_frame, mr_frame, or_frame, sl_frame, nl_frame):

    option_box = OptionBox()

    angle_options = ["Spot", "Flood", "Wide", "Narrow"]
    option_box.create_option_box(sl_frame, angle_options, 4, 0, 5, 5)

    color_options = ["Red", "Blue"]
    option_box.create_option_box(clr_frame, color_options, 4, 0, 5, 5)

    color_options = ["Ambient", "Red", "UV", "Task lights"]
    option_box.create_option_box(lab_frame, color_options, 4, 0, 5, 5)

    color_options = ["Neutral White", "Cool White", "Dim Red", "Blue"]
    option_box.create_option_box(sr_frame, color_options, 4, 0, 5, 5)

    color_options = ["White", "Warm White", "Red"]
    option_box.create_option_box(dp_frame, color_options, 4, 0, 5, 5)

    color_options = ["Neutral White", "Cool White", "Dim Red", "Blue"]
    option_box.create_option_box(cr_frame, color_options, 4, 0, 5, 5)

    color_options = ["Neutral White", "Cool White", "Dim Red", "Blue"]
    option_box.create_option_box(cq_frame, color_options, 4, 0, 5, 5)

    color_options = ["Neutral White", "Cool White", "Dim Red", "Blue"]
    option_box.create_option_box(mr_frame, color_options, 4, 0, 5, 5)

    color_options = ["Neutral White", "Cool White", "Dim Red", "Blue"]
    option_box.create_option_box(or_frame, color_options, 4, 0, 5, 5)

    color_options = ["Neutral White", "Cool White", "Dim Red", "Blue"]
    option_box.create_option_box(nl_frame, color_options, 4, 0, 5, 5)



