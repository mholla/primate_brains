"""
- For plotting figure 6. Box plot of surface area, sulcal depth, and cortical thickness
"""

def t_sd_box(input_txt, subjects_name, output_folder, max_t, min_t):
    
    import matplotlib.pyplot as plt
    import numpy as np
    import seaborn as sns
    import os
    import scipy.stats as stats
    
    path = os.path.join(os.getcwd(),input_txt)
    with open(path) as f: lines = f.read().splitlines()
    
    t_mean_all = []
    sd_mean_all = [] # average of total sulcal depth for all subjects
    sa_all_all = [] # average of total surface area for all subjects
    #vol_all_all = [] # average of total volume of the cortex for all subjects
    
    for line in lines:

        t_all = []
        sd_all = [] # total sulcal depth including both hemispheres
        sa_all = [] # total surface area including both hemispheres
        vol_all = [] # total volume of the cortex including both hemispheres
        
        hemis = ['lh','rh']
        
        for hemi in hemis:
        
            t = '{h}.thickness.asc'.format(h=hemi)
            sa = '{h}.pial.area.asc'.format(h=hemi)
            sd = '{h}.sulc.asc'.format(h=hemi)
            
            subjects_dir = os.path.join(os.getcwd(),subjects_name)
            subject = '{l}'.format(l=line)
            
            t = os.path.join(subjects_dir, subject, 'surf', t)
            sa = os.path.join(subjects_dir, subject, 'surf', sa)
            sd = os.path.join(subjects_dir, subject, 'surf', sd)
                
            # read sulcal depth
            with open(sd,'r') as sd_file:
                sd_lines = sd_file.readlines()
                
            sd = np.zeros(len(sd_lines))
                
            for i in range(len(sd_lines)):
                sd_data = sd_lines[i].split()
                sd[i] = sd_data[4]

            # read cortical thickness
            with open(t,'r') as t_file:
                t_lines = t_file.readlines()
                
            t = np.zeros(len(t_lines))
                
            for i in range(len(t_lines)):
                t_data = t_lines[i].split()
                t[i] = t_data[4]

            # read surface area
            with open(sa,'r') as sa_file:
                sa_lines = sa_file.readlines()
                
            sa = np.zeros(len(sa_lines))
                
            for i in range(len(sa_lines)):
                sa_data = sa_lines[i].split()
                sa[i] = sa_data[4]
                
            for i in range(len(t)):
                if t[i] >= max_t:
                    t[i] = 0
                    sa[i] = 0
                    sd[i] = 0
                    
            for i in range(len(t)):
                if t[i] <= min_t:
                    t[i] = 0
                    sa[i] = 0
                    sd[i] = 0

            t = t[t != 0]
            sa = sa[sa != 0]
            sd = sd[sd != 0]
                    
            t_all = np.append(t_all, t)
            sa_all = np.append(sa_all, sa)
            sd_all = np.append(sd_all, sd)
            
        #vol_all = t_all*sa_all/3

        t_mean = np.mean(t_all)
        sd_mean = np.mean(sd_all)
        sa_sum = np.sum(sa_all)/3
        vol_sum = np.sum(vol_all)

        t_mean_all = np.append(t_mean_all, t_mean)
        sd_mean_all = np.append(sd_mean_all, sd_mean)
        sa_all_all = np.append(sa_all_all, sa_sum)
        #vol_all_all = np.append(vol_all_all, vol_sum)

    sa_all_mean = np.mean(sa_all_all)
    #vol_all_mean = np.mean(vol_all_all)

    sa_all_all_ave = np.append(sa_all_all, sa_all_mean)
    #vol_all_all_ave = np.append(vol_all_all, vol_all_mean)

    sd_mean_all_ave = np.append(sd_mean_all, np.mean(sd_mean_all))
    sd_mean_all_ave = np.append(sd_mean_all_ave, np.std(sd_mean_all))

    t_mean_all_ave = np.append(t_mean_all, np.mean(t_mean_all))
    t_mean_all_ave = np.append(t_mean_all_ave, np.std(t_mean_all))

    # box plot of cortical thickness
    plt.figure()
    ax = sns.stripplot(data=[t_mean_all], linewidth=0.6, color='white', edgecolor='black', size=4, alpha=0.8)
    ax = sns.boxplot(data=[t_mean_all], fliersize=0, linewidth=1.5, width = 0.3, color='lightgrey')
    ax.set(ylim=(1.5, 3.4))
    ax.tick_params(axis = "x", which = "both", bottom = True, top = False, labelbottom=True)
    ax.set_xlabel(int(sa_all_mean/100), fontsize=8)
    fname = os.path.join('/afs/crc.nd.edu/group/commandlab/Nagehan/curveball_scripts/plots', output_folder, 't_mean_all.png')
    plt.savefig(fname, dpi = 500)

    # box plot of cortical thickness (2) - change box properties
    plt.figure()
    ax = sns.boxplot(data=[t_mean_all], fliersize=0, linewidth=1, width = 0.4, boxprops={'facecolor':'None','edgecolor':'black'},
                     whiskerprops={'color':'black'},medianprops={'color':'black'},capprops={'color':'black'})
    ax = sns.stripplot(data=[t_mean_all], color='black', size=4, alpha=0.4, zorder=0)
    ax.set(ylim=(1.5, 3.4))
    ax.tick_params(axis = "x", which = "both", bottom = False, top = False)
    ax.set_xlabel(int(sa_all_mean/100), fontsize=8)
    fname = os.path.join('/afs/crc.nd.edu/group/commandlab/Nagehan/curveball_scripts/plots', output_folder, 't_mean2_all.png')
    plt.savefig(fname, dpi = 500)

    # box plot of surface area
    plt.figure()
    ax = sns.boxplot(data=[sa_all_all], fliersize=0, linewidth=1, width = 0.4, boxprops={'facecolor':'None','edgecolor':'black'},
                     whiskerprops={'color':'black'},medianprops={'color':'black'},capprops={'color':'black'})
    ax = sns.stripplot(data=[sa_all_all], color='black', size=4, alpha=0.4, zorder=0)
    ax.set(ylim=(0, 280000))
    ax.tick_params(axis = "x", which = "both", bottom = False, top = False)
    #ax.set_xlabel(int(sa_all_mean/100), fontsize=8)
    fname = os.path.join('/afs/crc.nd.edu/group/commandlab/Nagehan/curveball_scripts/plots', output_folder, 'sa_all_all.png')
    plt.savefig(fname, dpi = 500)

    # box plot of sulcal depth
    plt.figure()
    ax = sns.stripplot(data=[sd_mean_all], linewidth=0.6, color='white', edgecolor='black', size=4, alpha=0.8)
    ax = sns.boxplot(data=[sd_mean_all], fliersize=0, linewidth=1.5, width = 0.3, color='lightgrey')
    ax.set(ylim=(1.5, 8))
    ax.tick_params(axis = "x", which = "both", bottom = True, top = False, labelbottom=True)
    ax.set_xlabel(int(sa_all_mean/100), fontsize=8)
    fname = os.path.join('/afs/crc.nd.edu/group/commandlab/Nagehan/curveball_scripts/plots', output_folder, 'sd_mean_all.png')
    plt.savefig(fname, dpi = 500)

    # box plot of sulcal depth (2) - change box properties
    plt.figure()
    ax = sns.boxplot(data=[sd_mean_all], fliersize=0, linewidth=1, width = 0.4, boxprops={'facecolor':'None','edgecolor':'black'},
                     whiskerprops={'color':'black'},medianprops={'color':'black'},capprops={'color':'black'})
    ax = sns.stripplot(data=[sd_mean_all], color='black', size=4, alpha=0.4, zorder=0)
    ax.set(ylim=(1.5, 8))
    ax.tick_params(axis = "x", which = "both", bottom = False, top = False)
    ax.set_xlabel(int(sa_all_mean/100), fontsize=8)
    fname = os.path.join('/afs/crc.nd.edu/group/commandlab/Nagehan/curveball_scripts/plots', output_folder, 'sd_mean2_all.png')
    plt.savefig(fname, dpi = 500)

    #Save data, total surface area, volume, sulcal depth, cortical thickness for each subject
    sa_name = os.path.join('/afs/crc.nd.edu/group/commandlab/Nagehan/curveball_scripts/plots', output_folder, 'sa_all.asc')
    np.savetxt(sa_name, sa_all_all_ave, fmt='%6.2f', delimiter=' '' ') 

    #vol_name = os.path.join('/afs/crc.nd.edu/group/commandlab/Nagehan/curveball_scripts/plots', output_folder, 'vol_all.asc')
    #np.savetxt(vol_name, vol_all_all_ave, fmt='%6.2f', delimiter=' '' ') 

    sd_name = os.path.join('/afs/crc.nd.edu/group/commandlab/Nagehan/curveball_scripts/plots', output_folder, 'sd_mean_all.asc')
    np.savetxt(sd_name, sd_mean_all_ave, fmt='%6.2f', delimiter=' '' ') 

    t_name = os.path.join('/afs/crc.nd.edu/group/commandlab/Nagehan/curveball_scripts/plots', output_folder, 't_mean_all2.asc')
    np.savetxt(t_name, t_mean_all_ave, fmt='%6.2f', delimiter=' '' ') 
    
    return
