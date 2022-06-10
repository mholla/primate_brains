"""
- Sulcal depth (not shrunken sulcal depth) distribution profiles for convex, concave, and saddle shaped points
for all subjects. Convex and concave shaped points are identified by negative and positive principal curvatures respectively
and saddle shaped points are identified by negative Gaussian curvature
"""


def sd_curv(input_txt, subjects_name, output_folder, max_t, min_t):
    
    import matplotlib.pyplot as plt
    import numpy as np
    import seaborn as sns
    import os
    import scipy.stats as stats
    
    path = os.path.join(os.getcwd(),input_txt)
    with open(path) as f: lines = f.read().splitlines()

    sd_gyr_hemis = []
    sd_sulc_hemis = []
    sd_neg_hemis = []

    sd_gyr_all = []
    sd_sulc_all = []
    sd_neg_all = []

    sd_all_all = []
    
    for line in lines:

        sd_gyr_hemis = []
        sd_sulc_hemis = []
        sd_neg_hemis = []
        
        hemis = ['lh', 'rh']
        
        for hemi in hemis:
        
            K = '{h}.pial.K.asc'.format(h=hemi)
            k1 = '{h}.pial.k1.asc'.format(h=hemi)
            k2 = '{h}.pial.k2.asc'.format(h=hemi)
            sd = '{h}.sulc.asc'.format(h=hemi)
            
            subjects_dir = os.path.join(os.getcwd(),subjects_name)
            subject = '{l}'.format(l=line)
            
            K = os.path.join(subjects_dir, subject, 'surf', K)
            k1 = os.path.join(subjects_dir, subject, 'surf', k1)
            k2 = os.path.join(subjects_dir, subject, 'surf', k2)
            sd = os.path.join(subjects_dir, subject, 'surf', sd)
            
            # read Gaussian curvature
            with open(K,'r') as K_file:
                K_lines = K_file.readlines()
                
            K = np.zeros(len(K_lines))
                
            for i in range(len(K_lines)):
                K_data = K_lines[i].split()
                K[i] = K_data[4]
                
            # read principal curvatures
            with open(k1,'r') as k1_file:
                k1_lines = k1_file.readlines()
                
            k1 = np.zeros(len(k1_lines))
                
            for i in range(len(k1_lines)):
                k1_data = k1_lines[i].split()
                k1[i] = k1_data[4]
                
            with open(k2,'r') as k2_file:
                k2_lines = k2_file.readlines()
                
            k2 = np.zeros(len(k2_lines))
                
            for i in range(len(k2_lines)):
                k2_data = k2_lines[i].split()
                k2[i] = k2_data[4]
                
            # read sulcal depth
            with open(sd,'r') as sd_file:
                sd_lines = sd_file.readlines()
                
            sd = np.zeros(len(sd_lines))
                
            for i in range(len(sd_lines)):
                sd_data = sd_lines[i].split()
                sd[i] = sd_data[4]

            # Positive Gaussian Curvature divided into sulci and gyral points by using principal curvatures
            
            sd_gyr = np.zeros(len(sd))
            sd_sulc = np.zeros(len(sd))
            
            for i in range(len(k1)):
                if k1[i] < 0 and k2[i] < 0:
                    sd_gyr[i] = sd[i]
                    
            for i in range(len(k1)):
                if k1[i] > 0 and k2[i] > 0:
                    sd_sulc[i] = sd[i]
                            
            # Negative Gaussian Curvature - Saddle Points
            sd_neg = np.zeros(len(sd))
            
            for i in range(len(K)):
                if K[i] < 0:
                    sd_neg[i] = sd[i]
                    
            sd_gyr = sd_gyr[sd_gyr != 0]
            sd_sulc = sd_sulc[sd_sulc != 0]
            sd_neg = sd_neg[sd_neg != 0]

            sd_gyr_hemis = np.append(sd_gyr_hemis, sd_gyr)
            sd_sulc_hemis = np.append(sd_sulc_hemis, sd_sulc)
            sd_neg_hemis = np.append(sd_neg_hemis, sd_neg)

            #T-test
            p1 = stats.ttest_ind(a=sd_gyr_hemis, b=sd_neg_hemis, equal_var=False)
            p2 = stats.ttest_ind(a=sd_neg_hemis, b=sd_sulc_hemis, equal_var=False)
            
            p_val1 = p1[1]
            p_val2 = p2[1]

        sd_gyr_mean = np.mean(sd_gyr_hemis)
        sd_sulc_mean = np.mean(sd_sulc_hemis)
        sd_neg_mean = np.mean(sd_neg_hemis)

        sd_gyr_all = np.append(sd_gyr_all, sd_gyr_mean)
        sd_sulc_all = np.append(sd_sulc_all, sd_sulc_mean)
        sd_neg_all = np.append(sd_neg_all, sd_neg_mean)

    sd_all_all = np.append(sd_all_all, sd_gyr_all)
    sd_all_all = np.append(sd_all_all, sd_sulc_all)
    sd_all_all = np.append(sd_all_all, sd_neg_all)

    # # Plot    
    # plt.figure()
    # ax = sns.kdeplot(sd_sulc_K, color='#31688E', shade=True, label='Pos k1, k2',bw_adjust=2, cut=0)
    # ax = sns.kdeplot(sd_neg_K, color='#FDE725', shade=True, label='Neg K', bw_adjust=2, cut=0)
    # ax = sns.kdeplot(sd_gyr_K, color='#31688E', shade=True, label='Neg k1, k2', bw_adjust=2, cut=0)
    # fname = os.path.join('/afs/crc.nd.edu/group/commandlab/Nagehan/curveball_scripts/plots', output_folder, 'sd_curv_all.png')
    # plt.savefig(fname, dpi = 500)
    
    names = [('mean_gyr', 'len_gyr', 'mean_sulc', 'len_sulc', 'mean_saddle', 'len_saddle','std_gyr', 'std_sulc', 'std_saddle', 'p_val1', 'p_val2')]
    results = [(np.mean(sd_gyr_all), len(sd_gyr_hemis), np.mean(sd_sulc_all), len(sd_sulc_hemis), np.mean(sd_neg_all), len(sd_neg_hemis), np.std(sd_gyr_all), np.std(sd_sulc_all), 
        np.std(sd_neg_all), p_val1, p_val2)]
        
    K_name = os.path.join('/afs/crc.nd.edu/group/commandlab/Nagehan/curveball_scripts/plots', output_folder, 'sd_curv_all_mean.asc')
        
    np.savetxt(K_name, names, fmt='%s', delimiter=' '' ') 
        
    with open(K_name,'ab') as f:
        np.savetxt(f, results, fmt='%6.2f', delimiter=' '' ')

    sd_name = os.path.join('/afs/crc.nd.edu/group/commandlab/Nagehan/curveball_scripts/plots', output_folder, 'sd_curv_all.asc')
    np.savetxt(sd_name, sd_all_all, fmt='%6.2f', delimiter=' '' ') 
    
    return
                