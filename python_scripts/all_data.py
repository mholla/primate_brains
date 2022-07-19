"""
Main script of the pipeline. Extracts data for each species from the text files shared at Zenodo website (10.5281/zenodo.6638529).

Change the name of your subjects directory, input text file, and results directory accordingly. 

There are multiple subjects for humans, macaques, and chimpanzees.
For the rest of the species, N=1.

Limit the cortical thickness by min and max values. 
For humans and chimpanzees max_t = 5.0
For macaques max_t = 4.0
For smaller species max_t = 3.5

Go to each individual script to learn about what/how it does. 
"""

def all_data():
    
    import os
    import g_curv
    import shape_index
    import sulcal_depth
    import CT
    import t_sd_box
    import FI_C_GI
    import sd_curv

    #input_txt = 'subjects_humans.txt'
    #subjects_name = 'subjects_humans'
    #output_folder = 'results_humans'

    #input_txt = 'subjects_macaques.txt'
    #subjects_name = 'subjects_macaques'
    #output_folder = 'results_macaques'

    #input_txt = 'subjects_chimps.txt'
    #subjects_name = 'subjects_chimps'
    #output_folder = 'results_chimps'

    input_txt = 'subjects_primates.txt'
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
    
all_data()









