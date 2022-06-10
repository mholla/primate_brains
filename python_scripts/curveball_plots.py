"""
Main plotting script of the pipeline. Plots curvature and thickness distributions of each subset of the ABIDE (or any) dataset.
    
"""

def curveball_plots():
    
    import os
    import g_curv
    import shape_index
    import sulcal_depth
    import CT
    import t_sd_box
    import FI_C_GI
    import sd_curv

    #input_txt = 'subjects_ABIDE_TD_quality.txt'
    #subjects_name = 'subjects_ABIDE_TD/subjects_ABIDE_TD'
    #output_folder = 'results_qual67'

    #input_txt = 'subjects_macaques.txt'
    #subjects_name = 'subjects_macaques'
    #output_folder = 'results_macaques'

    input_txt = 'subjects_primates_single.txt'
    subjects_name = 'subjects_primates'
    output_folder = 'results_primates'

    max_t = 5.0
    min_t = 0.5
        
    g_curv.g_curv(input_txt, subjects_name, output_folder, max_t, min_t)
    sd_curv.sd_curv(input_txt, subjects_name, output_folder, max_t, min_t)
    shape_index.shape_index(input_txt, subjects_name, output_folder, max_t, min_t)
    sulcal_depth.sulcal_depth(input_txt, subjects_name, output_folder, max_t, min_t)
    FI_C_GI.FI_C_GI(input_txt, subjects_name, output_folder, max_t, min_t)
    CT.CT(input_txt, subjects_name, output_folder, max_t, min_t)
    t_sd_box.t_sd_box(input_txt, subjects_name, output_folder, max_t, min_t)
        
    return
    
curveball_plots()









