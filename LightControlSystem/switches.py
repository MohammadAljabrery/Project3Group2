from classes import *

def switches(main_frame, ilcs_frame, elcs_frame,
             clr_frame, lab_frame, sr_frame, dp_frame, cr_frame,
             cq_frame, mr_frame, or_frame, sl_frame, nl_frame):
    toggle_switch = Switch()
    toggle_switch.create_switch(clr_frame, 0, 29, 1, 1)
    toggle_switch.create_switch(lab_frame, 0, 29, 1, 0)
    toggle_switch.create_switch(sr_frame, 0, 29, 1, 0)
    toggle_switch.create_switch(dp_frame, 0, 29, 1, 0)
    toggle_switch.create_switch(cr_frame, 0, 29, 1, 0)
    toggle_switch.create_switch(cq_frame, 0, 29, 1, 0)
    toggle_switch.create_switch(mr_frame, 0, 29, 1, 0)
    toggle_switch.create_switch(or_frame, 0,29, 1, 0)
    toggle_switch.create_switch(sl_frame, 0, 29, 1, 0)
    toggle_switch.create_switch(nl_frame, 0, 29, 1, 0)
