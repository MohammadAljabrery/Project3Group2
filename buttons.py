from classes import *
def buttons(main_frame, frame_manager, ilcs_frame, elcs_frame,
            clr_frame, lab_frame, sr_frame, dp_frame, cr_frame,
            cq_frame, mr_frame, or_frame, sl_frame, nl_frame):
    button = Buttons(main_frame, frame_manager)

    button.create_buttons(main_frame, "Internal Lights", "red", 100, 1,
                          0, 20, 20, main_frame, ilcs_frame)
    button.create_buttons(main_frame, "external Lights", "red", 100, 2,
                          0, 20, 20, main_frame, elcs_frame)
    # Button to go from ilcs to control room LCS
    button.create_buttons(ilcs_frame, "CR", "red", 100, 1,
                          0, 20, 20, ilcs_frame, clr_frame)
    # Button to go from ilcs to Laboratory LCS
    button.create_buttons(ilcs_frame, "LAB", "red", 100, 2,
                          0, 20, 20, ilcs_frame, lab_frame)
    # Button to go from ilcs to Storage room LCS
    button.create_buttons(ilcs_frame, "SR", "red", 100, 3,
                          0, 20, 20, ilcs_frame, sr_frame)
    # Button to go from ilcs to Data Processing room LCS
    button.create_buttons(ilcs_frame, "DP", "red", 100, 4,
                          0, 20, 20, ilcs_frame, dp_frame)
    # Button to go from ilcs to Communications room LCS
    button.create_buttons(ilcs_frame, "CR", "red", 100, 5,
                          0, 20, 20, ilcs_frame, dp_frame)
    # Button to go from ilcs to Crew Quarters LCS
    button.create_buttons(ilcs_frame, "CQ", "red", 100, 6,
                          0, 20, 20, ilcs_frame, cq_frame)
    # Button to go from ilcs to Medical room LCS
    button.create_buttons(ilcs_frame, "MR", "red", 100, 7,
                          0, 20, 20, ilcs_frame, mr_frame)
    # Button to go from ilcs to Observation room LCS
    button.create_buttons(ilcs_frame, "OR", "red", 100, 8,
                          0, 20, 20, ilcs_frame, or_frame)
    # Button to go from elcs to spotlight LCS
    button.create_buttons(elcs_frame, "SL", "red", 100, 1,
                          0, 20, 20, elcs_frame, sl_frame)
    # Button to go from elcs to navigational lights
    button.create_buttons(elcs_frame, "NL", "red", 100, 2,
                          0, 20, 20, elcs_frame, nl_frame)

# BACK BUTTONS

    #  Go back from lcs
    button.back_button(main_frame, main_frame, main_frame)
    # Button to go back to lcs from ilcs
    button.back_button(ilcs_frame, ilcs_frame, main_frame)
    # Button to go back to elcs from ilcs
    button.back_button(elcs_frame, elcs_frame, main_frame)
    # Button to go back to ilcs from control room LCS
    button.back_button(clr_frame, clr_frame, ilcs_frame)
    # Button to go back to ilcs from Laboratory LCS
    button.back_button(lab_frame, lab_frame, ilcs_frame)
    # Button to go back to ilcs from Storage room LCS
    button.back_button(sr_frame, sr_frame, ilcs_frame)
    # Button to go back to ilcs from Data Processing room LCS
    button.back_button(dp_frame, dp_frame, ilcs_frame)
    # Button to go back to ilcs from Communications room LCS
    button.back_button(cr_frame, cr_frame, ilcs_frame)
    # Button to go back to ilcs from Crew Quarters LCS
    button.back_button(cq_frame, cq_frame, ilcs_frame)
    # Button to go back to ilcs from Medical room LCS
    button.back_button(mr_frame, mr_frame, ilcs_frame)
    # Button to go back to ilcs from Observation room LCS
    button.back_button(or_frame, or_frame, ilcs_frame)
    # Button to go back to elcs from Spotlight LCS
    button.back_button(sl_frame, sl_frame, elcs_frame)
    # Button to go back to slcs from Navigational Light Frame
    button.back_button(nl_frame, nl_frame, elcs_frame)

    main_frame.pack(expand=1, fill="both")
