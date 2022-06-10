"""
Cortical thickness distribution profiles for interior and exterior vertices, 
below and above the mid cortical surface with effect size per individual.
"""
def sulcal_depth(input_txt, subjects_name, output_folder, max_t, min_t):
    
    import matplotlib.pyplot as plt
    import numpy as np
    import seaborn as sns
    import os
    
    path = os.path.join(os.getcwd(),input_txt)
    with open(path) as f: lines = f.read().splitlines()
    
    t_sulc_S = []
    t_gyr_S = []
    s_all = []
    
    d_S = []

    s_mean_all = []
    
    for line in lines:

        s_all = []
        
        hemis = ['lh','rh']
        
        for hemi in hemis:
            
            s = '{h}.sulc.asc'.format(h=hemi)
            S = '{h}.sulc.shrink.offset.7mm.asc'.format(h=hemi)
            t = '{h}.thickness.asc'.format(h=hemi)
            
            subjects_dir = os.path.join(os.getcwd(),subjects_name)
            subject = '{l}'.format(l=line)
            
            s = os.path.join(subjects_dir, subject, 'surf', s)
            S = os.path.join(subjects_dir, subject, 'surf', S)
            t = os.path.join(subjects_dir, subject, 'surf', t)
            
            # read sulcal depth
            with open(s,'r') as s_file:
                s_lines = s_file.readlines()
                
            s = np.zeros(len(s_lines))
                
            for i in range(len(s_lines)):
                s_data = s_lines[i].split()
                s[i] = s_data[4]

            # read sulcal shrink depth
            with open(S,'r') as S_file:
                S_lines = S_file.readlines()
                
            S = np.zeros(len(S_lines))
                
            for i in range(len(S_lines)):
                S_data = S_lines[i].split()
                S[i] = S_data[4]
                
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
                    
            for i in range(len(t)):
                if t[i] == 0:
                    S[i] = 0
                    s[i] = 0
                    
            t = t[t != 0]
            S = S[S != 0]
            s = s[s != 0]
                    
            # Sulcal depth divided into t_sulc and t_gyral 
            S_gyr = np.zeros(len(S))
            S_sulc = np.zeros(len(S))
            
            t_gyr = np.zeros(len(t))
            t_sulc = np.zeros(len(t))
            
            for i in range(len(S)):
                if S[i] < 0:
                    S_gyr[i] = S[i]
                    t_gyr[i] = t[i]
                    
            for i in range(len(S)):
                if S[i] > 0:
                    S_sulc[i] = S[i]
                    t_sulc[i] = t[i]
                    
            t_gyr = t_gyr[t_gyr != 0]
            t_sulc = t_sulc[t_sulc != 0]
            
            S_gyr = S_gyr[S_gyr != 0]
            S_sulc = S_sulc[S_sulc != 0]
                    
            t_gyr_S = np.append(t_gyr_S, t_gyr)
            t_sulc_S = np.append(t_sulc_S, t_sulc)

            s_all = np.append(s_all, s)

        s_mean = np.mean(s_all)
        s_mean_all = np.append(s_mean_all, s_mean)
    
        # sample sizes
        n1 = len(t_gyr_S)
        n2 = len(t_sulc_S)
        
        #  variance of the samples
        s1 = np.var(t_gyr_S, ddof=1)
        s2 = np.var(t_sulc_S, ddof=1)
        
        # pooled standard deviation
        s = np.sqrt(((n1 - 1) * s1 + (n2 - 1) * s2) / (n1 + n2 - 2))
        
        # means of the samples
        u1 = np.mean(t_gyr_S)
        u2 = np.mean(t_sulc_S)
        
        # effect size
        d = (u1 - u2) / s
        d_S = np.append(d_S, d)

    s_mean_all_mean = np.mean(s_mean_all)
    s_mean_all = np.append(s_mean_all, s_mean_all_mean)
                           
    plt.figure()
    ax = sns.kdeplot(t_gyr_S, color='#FDE725', shade=True, label = 'S>0', bw_adjust=6)
    ax = sns.kdeplot(t_sulc_S, color='#31688E', shade=True, label = 'S<0', bw_adjust= 6)
    plt.legend(loc='best', prop={'size': 14})
    ax.set(xlim=(min_t, max_t))
    ax.set(xlim=(min_t, max_t))
    fname = os.path.join('/afs/crc.nd.edu/group/commandlab/Nagehan/curveball_scripts/plots', output_folder, 'sd_all_offset.png')
    plt.savefig(fname, dpi = 500)
    
    #Box plot
    plt.figure()
    ax = sns.stripplot(data=[d_S], linewidth=0.8, color='white', edgecolor='black', size=5, alpha=0.8)
    ax = sns.boxplot(data=[d_S], fliersize=0, linewidth=1.5, width = 0.3, color='lightgrey')
    ax.set(ylim=(0, 1.2))
    fname = os.path.join('/afs/crc.nd.edu/group/commandlab/Nagehan/curveball_scripts/plots', output_folder,'sd_effect_all_offset.png')
    plt.savefig(fname, dpi = 500)

    plt.figure()
    ax = sns.boxplot(data=[d_S], fliersize=0, linewidth=1, width = 0.3, boxprops={'facecolor':'None','edgecolor':'black'},
                     whiskerprops={'color':'black'},medianprops={'color':'black'},capprops={'color':'black'})
    ax = sns.stripplot(data=[d_S], color='black', size=3, alpha=0.2, zorder=0)
    ax.set(ylim=(0, 1.2))
    ax.tick_params(axis = "x", which = "both", bottom = False, top = False)
    fname = os.path.join('/afs/crc.nd.edu/group/commandlab/Nagehan/curveball_scripts/plots', output_folder, 's_curv_effect_all_offset.png')
    plt.savefig(fname, dpi = 500)
    
    names = [('mean_s', 'mean_gyr', 'mean_sulc', 'std_gyr', 'std_sulc', 'mean_d')]
    results = [(np.mean(s_all), np.mean(t_gyr_S), np.mean(t_sulc_S), np.std(t_gyr_S), np.std(t_sulc_S), np.mean(d_S))]
        
    S_name = os.path.join('/afs/crc.nd.edu/group/commandlab/Nagehan/curveball_scripts/plots', output_folder, 'sd_all_offset.asc')
        
    np.savetxt(S_name, names, fmt='%s', delimiter=' '' ') 
        
    with open(S_name,'ab') as f:
        np.savetxt(f, results, fmt='%6.2f', delimiter=' '' ')

    s_name = os.path.join('/afs/crc.nd.edu/group/commandlab/Nagehan/curveball_scripts/plots', output_folder, 's_mean_all.asc')
    np.savetxt(s_name, s_mean_all, fmt='%6.2f', delimiter=' '' ')
        

    return
    
    
