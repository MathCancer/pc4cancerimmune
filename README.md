# pc4cancerimmune
PhysiCell model of immune cells attacking a heterogeneous tumor. This app can be run in a Jupyter notebook GUI at https://nanohub.org/tools/pc4cancerimmune.

This app demonstrates key stochastic attachment dynamics during a cancer immune response. It is based on a published PhysiCell example in Ghaffarizadeh et al. (2018) [1], which was further explored in [2-3]. In this model, cancer cells rapidly divide while consuming oxygen, which drives the emergence of hypoxic gradients. Greater availability of oxygen drives faster proliferation, while low oxygen can trigger necrotic death, creating a necrotic core (brown cells) in the center of the tumor. Each cell expresses a mutant "oncoprotein" *p*, which determines how well the cells can respond to oxygen availability to enter the cell cycle. Cells with greater *p* expression divide more rapidly. In the demonstration, cells are shaded from blue (lowest *p* and least proliferative) to yellow (greatest *p* and most proliferative). See further description of the untreated heterogeneous tumor at https://nanohub.org/tools/pc4heterogen.

As a simple model of cancer-immune contact interactions, we introduce immune cells (green) later in the simulation. These immune cells peform a biased random migration towards a tumor-released immunostimulatory compound (e.g., CXCL9), test for physical contact, and form a focal adhesion. While adhered, they sample the cell's immunogenicity and attempt to induce apoptosis. (Red cells are apoptotic.) If they succeed, they detach and resume their search for more targets. If they fail, they remain attached and continue attempting to induce apoptosis until reaching a maximum attachment time.

More details about the model can be found at https://nanohub.org/resources/pc4cancerimmune/about.

[1] Ghaffarizadeh A, Heiland R, Friedman SH, Mumenthaler SM, Macklin P (2018) PhysiCell: An open source physics-based cell simulator for 3-D multicellular systems. PLoS Comput Biol 14(2): e1005991. https://doi.org/10.1371/journal.pcbi.1005991

[2] Ozik J, Collier N, Wozniak J, Macal C, Cockrell C, Friedman S, Ghaffarizadeh A, Heiland R, An G, Macklin P (2018). High-throughput cancer hypothesis testing with an integrated PhysiCell-EMEWS workflow. BMC Bioinformatics 19:483. https://dx.doi.org/10.1186/s12859-018-2510-x. 

[3] Ozik J et al. (2019, in preparation) Learning-accelerated discovery of immune-tumor interactions. 
