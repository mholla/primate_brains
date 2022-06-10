"""
Mean folding index and intrinsic curvature index for all subjects
"""
def FI_C_GI(input_txt, subjects_name, output_folder, max_t, min_t):
    
    import matplotlib.pyplot as plt
    import numpy as np
    import seaborn as sns
    import os
    from scipy.stats import skew
    import pyvista as pv
    
    path = os.path.join(os.getcwd(),input_txt)
    with open(path) as f: lines = f.read().splitlines()
    
    fi_sum_all = []
    c_sum_all = []
    gi_all =[]
    alpha_all_area = []
    
    for line in lines:

        fi_all = []
        c_all = []
        alpha_all = [] # area of alpha surface for both hemispheres
        pial_all = [] # area of the pial surface for both hemispheres

        hemis = ['lh','rh']
        
        for hemi in hemis:
            
            alpha = '{h}.alpha.ply'.format(h=hemi)
            a = '{h}.pial.area.asc'.format(h=hemi)
            K = '{h}.pial.K.asc'.format(h=hemi)
            k1 = '{h}.pial.k1.asc'.format(h=hemi)
            k2 = '{h}.pial.k2.asc'.format(h=hemi)
            
            subjects_dir = os.path.join(os.getcwd(),subjects_name)
            subject = '{l}'.format(l=line)
            
            alpha = os.path.join(subjects_dir, subject, 'surf', alpha)
            a = os.path.join(subjects_dir, subject, 'surf', a)
            K = os.path.join(subjects_dir, subject, 'surf', K)
            k1 = os.path.join(subjects_dir, subject, 'surf', k1)
            k2 = os.path.join(subjects_dir, subject, 'surf', k2)
            
            # reading alpha surface mesh by pyvista
            mesh_alpha = pv.read(alpha)

            # reading Gaussian curvature
            with open(K,'r') as K_file:
                K_lines = K_file.readlines()
                
            K = np.zeros(len(K_lines))
                
            for i in range(len(K_lines)):
                K_data = K_lines[i].split()
                K[i] = K_data[4]
                
            # reading k1-principal curvature
            with open(k1,'r') as k1_file:
                k1_lines = k1_file.readlines()
                
            k1 = np.zeros(len(k1_lines))
                
            for i in range(len(k1_lines)):
                k1_data = k1_lines[i].split()
                k1[i] = k1_data[4]
                
            # reading k2-principal curvature
            with open(k2,'r') as k2_file:
                k2_lines = k2_file.readlines()
                
            k2 = np.zeros(len(k2_lines))
                
            for i in range(len(k2_lines)):
                k2_data = k2_lines[i].split()
                k2[i] = k2_data[4]
                
            # reading area file
            with open(a,'r') as a_file:
                a_lines = a_file.readlines()
                
            a = np.zeros(len(a_lines))
                
            for i in range(len(a_lines)):
                a_data = a_lines[i].split()
                a[i] = a_data[4]

            # removing 
            for i in range(len(K)):
                if K[i] > 1:
                    K[i] = 0
                    a[i] = 0
                    k1[i] = 0
                    k2[i] = 0

            for i in range(len(K)):
                if K[i] < -1:
                    K[i] = 0
                    a[i] = 0
                    k1[i] = 0
                    k2[i] = 0

            for i in range(len(k1)):
                if k1[i] == 0:
                    a[i] = 0
                    k2[i] = 0

            for i in range(len(k2)):
                if k2[i] == 0:
                    a[i] = 0
                    k1[i] = 0

            for i in range(len(a)):
                if a[i] == 0:
                    k2[i] = 0
                    k1[i] = 0

            a = a[a != 0]
            k2 = k2[k2 != 0]
            k1 = k1[k1 != 0]

            alpha_area = mesh_alpha.area
            pial_area = np.sum(a)/3

            fi = np.sum(abs(k1) * abs(k1 - k2) * a/3)/4/np.pi #folding index
            c = np.sqrt((k1**2 + k2**2)/2) # vertex-wise curvedness
            c = np.mean(c) # average curvedness
        
            fi_all = np.append(fi_all, fi)
            c_all = np.append(c_all, c)
            
            alpha_all = np.append(alpha_all, alpha_area)
            pial_all = np.append(pial_all, pial_area)


        fi_sum = np.sum(fi_all)
        fi_sum_all = np.append(fi_sum_all, fi_sum)

        gi = np.sum(pial_all)/np.sum(alpha_all)
        gi_all = np.append(gi_all, gi)

        c_sum = np.sum(c_all)
        c_sum_all = np.append(c_sum_all, c_sum)
    
    #Statistic
    var_fi = np.var(fi_sum_all)
    mean_fi = np.mean(fi_sum_all)
    skew_fi = skew(fi_sum_all)
    std_fi = np.std(fi_sum_all)

    var_c = np.var(c_sum_all)
    mean_c = np.mean(c_sum_all)
    skew_c = skew(c_sum_all)
    std_c = np.std(c_sum_all)

    var_gi = np.var(gi_all)
    mean_gi = np.mean(gi_all)
    skew_gi = skew(gi_all)
    std_gi = np.std(gi_all)
    
    names = [('fi_mean', 'fi_std', 'fi_var', 'fi_skew', 'c_mean', 'c_std', 'c_var', 'gi_skew', 'gi_mean', 'gi_std', 'gi_var', 'gi_skew')]
    results = [(mean_fi, std_fi, var_fi, skew_fi, mean_c, std_c, var_c, skew_c, mean_gi, std_gi, var_gi, skew_gi)]
        
    fi_name = os.path.join('/afs/crc.nd.edu/group/commandlab/Nagehan/curveball_scripts/plots', output_folder, 'fi_c_gi_all.asc')
        
    np.savetxt(fi_name, names, fmt='%s', delimiter=' '' ') 
        
    with open(fi_name,'ab') as f:
        np.savetxt(f, results, fmt='%6.2f', delimiter=' '' ')

    fi_name = os.path.join('/afs/crc.nd.edu/group/commandlab/Nagehan/curveball_scripts/plots', output_folder, 'fi_sum_all.asc')
    np.savetxt(fi_name, fi_sum_all, fmt='%6.2f', delimiter=' '' ')

    c_name = os.path.join('/afs/crc.nd.edu/group/commandlab/Nagehan/curveball_scripts/plots', output_folder, 'c_sum_all.asc')
    np.savetxt(c_name, c_sum_all, fmt='%6.2f', delimiter=' '' ')

    gi_name = os.path.join('/afs/crc.nd.edu/group/commandlab/Nagehan/curveball_scripts/plots', output_folder, 'gi_all.asc')
    np.savetxt(gi_name, gi_all, fmt='%6.2f', delimiter=' '' ')

    plt.figure()
    ax = sns.boxplot(data=[gi_all], fliersize=0, linewidth=1, width = 0.4, boxprops={'facecolor':'None','edgecolor':'black'},
                     whiskerprops={'color':'black'},medianprops={'color':'black'},capprops={'color':'black'})
    ax = sns.stripplot(data=[gi_all], color='black', size=4, alpha=0.4, zorder=0)
    ax.set(ylim=(1.5, 3.0))
    ax.tick_params(axis = "x", which = "both", bottom = False, top = False)
    #ax.set_xlabel(int(sa_all_mean/100), fontsize=8)
    fname = os.path.join('/afs/crc.nd.edu/group/commandlab/Nagehan/curveball_scripts/plots', output_folder, 'gi_mean_all.png')
    plt.savefig(fname, dpi = 500)
        
    return

