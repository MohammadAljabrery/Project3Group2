from classes import *

def labels(main_frame, ilcs_frame, elcs_frame,
           clr_frame, lab_frame, sr_frame, dp_frame, cr_frame,
           cq_frame, mr_frame, or_frame, sl_frame, nl_frame):

    label = Labels()
    label.create_label(sl_frame, "Spotlight Intensity", 1, 0, 1, 1, "nw")
    label.create_label(sl_frame, "Spotlight Coverage", 3, 0, 1, 1, "nw")
    label.create_label(clr_frame, "Brightness", 1, 0, 1, 1, "nw")
    label.create_label(clr_frame, "colour", 3, 0, 1, 1, "nw")
    label.create_label(lab_frame, "Brightness", 1, 0, 1, 1, "nw")
    label.create_label(lab_frame, "colour", 3, 0, 1, 1, "nw")
    label.create_label(sr_frame, "Brightness", 1, 0, 1, 1, "nw")
    label.create_label(sl_frame, "colour", 3, 0, 1, 1, "nw")
    label.create_label(dp_frame, "Brightness", 1, 0, 1, 1, "nw")
    label.create_label(dp_frame, "colour", 3, 0, 1, 1, "nw")
    label.create_label(cr_frame, "Brightness", 1, 0, 1, 1, "nw")
    label.create_label(cr_frame, "colour", 3, 0, 1, 1, "nw")
    label.create_label(cq_frame, "Brightness", 1, 0, 1, 1, "nw")
    label.create_label(cq_frame, "colour", 3, 0, 1, 1, "nw")
    label.create_label(mr_frame, "Brightness", 1, 0, 1, 1, "nw")
    label.create_label(mr_frame, "colour", 3, 0, 1, 1, "nw")
    label.create_label(or_frame, "Brightness", 1, 0, 1, 1, "nw")
    label.create_label(or_frame, "colour", 3, 0, 1, 1, "nw")
    label.create_label(sl_frame, "colour", 3, 0, 1, 1, "nw")
    label.create_label(nl_frame, "Brightness", 1, 0, 1, 1, "nw")
    label.create_label(nl_frame, "colour", 3, 0, 1, 1, "nw")
