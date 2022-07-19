"""
- Cortical thickness distribution profiles are extracted and plotted for all convex (gyr), concave (sulc), and saddle (neg) shaped points. 
- Gaussian curvature is used to determine saddle shaped points and principal curvatures are used to determine convex and concave shaped points.
- Effect sizes for each distribution combination are also available (d1_K, d2_K, d3_K) (but not published).
- Mean and standard deviation of cortical thickness as well as p and d values are saved in a text file (average of all subjects).
- Mean cortical thickness ratio for each subject is also saved into a text file.
"""

def g_curv(input_txt, subjects_name, output_folder, max_t, min_t):
    
    import matplotlib.pyplot as plt
    import numpy as np
    import seaborn as sns
    import os
    import scipy.stats as stats
    
    path = os.path.join(os.getcwd(),input_txt)
    with open(path) as f: lines = f.read().splitlines()
    
    t_gyr_K = []
    t_sulc_K = []
    t_neg_K = []

    t_gyr_all = []
    t_sulc_all = []
    t_neg_all = []
    
    d1_K = []
    d2_K = []
    d3_K = []
    
    for line in lines:

        t_gyr_K = []
        t_sulc_K = []
        t_neg_K = []
        
        hemis = ['lh', 'rh']
        
        for hemi in hemis:
        
            K = '{h}.pial.K.asc'.format(h=hemi)
            k1 = '{h}.pial.k1.asc'.format(h=hemi)
            k2 = '{h}.pial.k2.asc'.format(h=hemi)
            t = '{h}.thickness.asc'.format(h=hemi)
            
            subjects_dir = os.path.join(os.getcwd(),subjects_name)
            subject = '{l}'.format(l=line)
            
            K = os.path.join(subjects_dir, subject, 'surf', K)
            k1 = os.path.join(subjects_dir, subject, 'surf', k1)
            k2 = os.path.join(subjects_dir, subject, 'surf', k2)
            t = os.path.join(subjects_dir, subject, 'surf', t)
            
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
                
            # read cortical thickness
            with open(t,'r') as t_file:
                t_lines = t_file.readlines()
                
            t = np.zeros(len(t_lines))
                
            for i in range(len(t_lines)):
                t_data = t_lines[i].split()
                t[i] = t_data[4]
                
            for i in range(len(t)):
                if t[i] >= max_t:
                    t[i] = 0
                    
            for i in range(len(t)):
                if t[i] <= min_t:
                    t[i] = 0
                    
            # Positive Gaussian Curvature divided into sulci and gyral points by using principal curvatures
        
            K_gyr = np.zeros(len(K))
            K_sulc = np.zeros(len(K))
            
            k1_gyr = np.zeros(len(k1))
            k2_gyr = np.zeros(len(k2))
            
            k1_sulc = np.zeros(len(k1))
            k2_sulc = np.zeros(len(k2))
            
            t_gyr = np.zeros(len(t))
            t_sulc = np.zeros(len(t))
            
            for i in range(len(k1)):
                if k1[i] < 0 and k2[i] < 0:
                    K_gyr[i] = K[i]
                    k1_gyr[i] = k1[i]
                    k2_gyr[i] = k2[i]
                    t_gyr[i] = t[i]
                    
            for i in range(len(k1)):
                if k1[i] > 0 and k2[i] > 0:
                    K_sulc[i] = K[i]
                    k1_sulc[i] = k1[i]
                    k2_sulc[i] = k2[i]
                    t_sulc[i] = t[i]
                            
            # Negative Gaussian Curvature - Saddle Points
            K_neg = np.zeros(len(K))
            k1_neg = np.zeros(len(k1))
            k2_neg = np.zeros(len(k2))
            t_neg = np.zeros(len(t))
            
            
            for i in range(len(K)):
                if K[i] < 0:
                    K_neg[i] = K[i]
                    k1_neg[i] = k1[i]
                    k2_neg[i] = k2[i]
                    t_neg[i] = t[i]
                    
            K_gyr = K_gyr[K_gyr != 0]
            K_sulc = K_sulc[K_sulc != 0]
            K_neg = K_neg[K_neg != 0]
            
            t_gyr = t_gyr[t_gyr != 0]
            t_sulc = t_sulc[t_sulc != 0]
            t_neg = t_neg[t_neg != 0]
            
            #T-test
            p1 = stats.ttest_ind(a=t_gyr, b=t_neg, equal_var=False)
            p2 = stats.ttest_ind(a=t_neg, b=t_sulc, equal_var=False)
            
            p_val1 = p1[1]
            p_val2 = p2[1]
                    
            t_gyr_K = np.append(t_gyr_K, t_gyr)
            t_sulc_K = np.append(t_sulc_K, t_sulc)
            t_neg_K = np.append(t_neg_K, t_neg)

        t_gyr_K_mean = np.mean(t_gyr_K)
        t_sulc_K_mean = np.mean(t_sulc_K)
        t_neg_K_mean = np.mean(t_neg_K)

        t_gyr_all = np.append(t_gyr_all, t_gyr_K_mean)
        t_sulc_all = np.append(t_sulc_all, t_sulc_K_mean)
        t_neg_all = np.append(t_neg_all, t_neg_K_mean)

        t_cc_all = t_gyr_all/t_sulc_all

        # Calculate Cohen's d
        n1 = len(t_gyr_K)
        n2 = len(t_neg_K)
        n3 = len(t_sulc_K)
        
        # calculate the variance of the samples
        s1 = np.var(t_gyr, ddof=1)
        s2 = np.var(t_neg, ddof=1)
        s3 = np.var(t_sulc, ddof=1)
        
        # calculate the pooled standard deviation
        s_p1 = np.sqrt(((n1 - 1) * s1 + (n2 - 1) * s2) / (n1 + n2 - 2))
        s_p2 = np.sqrt(((n2 - 1) * s2 + (n3 - 1) * s3) / (n2 + n3 - 2))
        s_p3 = np.sqrt(((n1 - 1) * s1 + (n3 - 1) * s3) / (n1 + n3 - 2))
        
        # calculate the means of the samples
        u1 = np.mean(t_gyr_K)
        u2 = np.mean(t_neg_K)
        u3 = np.mean(t_sulc_K)
        
        # calculate the effect size
        d1 = (u1 - u2) / s_p1
        d2 = (u2 - u3) / s_p2
        d3 = (u1 - u3) / s_p3
                
        d1_K = np.append(d1_K, d1)
        d2_K = np.append(d2_K, d2)
        d3_K = np.append(d3_K, d3)
            
    # Plots 

    # Plot distribution profiles for all convex, concave, and saddle shaped points   
    plt.figure()
    ax = sns.kdeplot(t_sulc_K, color='#31688E', shade=True, label='Pos k1, k2',bw_adjust=2, cut=0)
    ax = sns.kdeplot(t_neg_K, color='#FDE725', shade=True, label='Neg K', bw_adjust=2, cut=0)
    ax = sns.kdeplot(t_gyr_K, color='#31688E', shade=True, label='Neg k1, k2', bw_adjust=2, cut=0)
    ax.set(xlim=(min_t, max_t))
    ax.set(xlim=(min_t, max_t))
    ax.set(xlim=(min_t, max_t))
    fname = os.path.join('/afs/crc.nd.edu/group/commandlab/Nagehan/curveball_scripts/plots', output_folder, 'g_curv_all.png')
    plt.savefig(fname, dpi = 500)
    
    # Plot effect size (1)
    plt.figure()
    ax = sns.stripplot(data=[d3_K, d2_K, d1_K], linewidth=0.8, color='white', edgecolor='black', size=5, alpha=0.8)
    ax = sns.boxplot(data=[d3_K, d2_K, d1_K], fliersize=0, linewidth=1.5, width = 0.4, color='lightgrey')
    #ax.set(ylim=(0, 1.2))
    ax.tick_params(axis = "x", which = "both", bottom = False, top = False)
    fname = os.path.join('/afs/crc.nd.edu/group/commandlab/Nagehan/curveball_scripts/plots', output_folder, 'g_curv_effect_all.png')
    plt.savefig(fname, dpi = 500)


    # Plot effect size (2)
    plt.figure()
    ax = sns.boxplot(data=[d3_K, d2_K, d1_K], fliersize=0, linewidth=1, width = 0.3, boxprops={'facecolor':'None','edgecolor':'black'},
                     whiskerprops={'color':'black'},medianprops={'color':'black'},capprops={'color':'black'})
    ax = sns.stripplot(data=[d3_K, d2_K, d1_K], color='black', size=3, alpha=0.2, zorder=0)
    #ax.set(ylim=(0, 1.2))
    ax.tick_params(axis = "x", which = "both", bottom = False, top = False)
    fname = os.path.join('/afs/crc.nd.edu/group/commandlab/Nagehan/curveball_scripts/plots', output_folder, 'g_curv_effect_all2.png')
    plt.savefig(fname, dpi = 500)

    # Plot cortical thickness ratio (convex to concave)
    plt.figure()
    ax = sns.boxplot(data=[t_cc_all], fliersize=0, linewidth=1, width = 0.4, boxprops={'facecolor':'None','edgecolor':'black'},
                     whiskerprops={'color':'black'},medianprops={'color':'black'},capprops={'color':'black'})
    ax = sns.stripplot(data=[t_cc_all], color='black', size=4, alpha=0.4, zorder=0)
    ax.set(ylim=(0.5, 1.5))
    ax.tick_params(axis = "x", which = "both", bottom = False, top = False)
    #ax.set_xlabel(int(sa_all_mean/100), fontsize=8)
    fname = os.path.join('/afs/crc.nd.edu/group/commandlab/Nagehan/curveball_scripts/plots', output_folder, 'cc_mean_all.png')
    plt.savefig(fname, dpi = 500)
    

    # Save data (cortical thickness) for all convex, concave, and saddle shaped points

    names = [('mean_gyr', 'mean_sulc', 'mean_saddle', 'len_gyr', 'len_sulc', 'len_saddle', 'std_gyr', 'std_sulc', 'std_saddle', 'p_val1', 'p_val2', 'd1_mean', 'd2_mean', 'd3_mean')]
    results = [(np.mean(t_gyr_all), np.mean(t_sulc_all), np.mean(t_neg_all), len(t_gyr_K), len(t_sulc_K), len(t_neg_K), np.std(t_gyr_all), np.std(t_sulc_all), np.std(t_neg_all), p_val1, p_val2,
                np.mean(d1_K), np.mean(d2_K), np.mean(d3_K))]
        
    K_name = os.path.join('/afs/crc.nd.edu/group/commandlab/Nagehan/curveball_scripts/plots', output_folder, 'g_curv_all.asc')
        
    np.savetxt(K_name, names, fmt='%s', delimiter=' '' ') 
        
    with open(K_name,'ab') as f:
        np.savetxt(f, results, fmt='%6.2f', delimiter=' '' ')

    # Save mean cortical thickness ratio for each subject
    cc_name = os.path.join('/afs/crc.nd.edu/group/commandlab/Nagehan/curveball_scripts/plots', output_folder, 'cc_mean_all.asc')
    np.savetxt(cc_name, t_cc_all, fmt='%6.2f', delimiter=' '' ') 

    
    return
