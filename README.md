# FreqDependSimulation

Neoantigens accumulated in cancers can elicit immune response but may not necessarily be eliminated by the immune system when present at low frequencies. The scripts in this repository implement a stochastic branching process-based simulation of tumour growth, taking into account the chance acqusition of antigenic mutations and negative frequency-dependent selection (NFDS). 

## Simulation details

We made use of the Gillespie algorithm [1] to conduct simulation of populations of cells. Each time a cell divided, it acquired m new unique mutations following the Poisson distribution (Poission(m)) [2]. The newly gained mutations were assigned as neoantigens at rate p , or as passengers (evolutionary neutral) at rate 1-p. Each antigenic mutation was assigned an antigenicity value (denoted ak for the k-th antigen in a given cell) sampled from an exponential distribution with mean equals 0.2 (Exp(0.2)) [2]. The death rate of each cell was determined by the complement of the survival rate, which was reduced by the immunogenicity of the tumor cell. Then we have dC = 1-(1+s*∑{k}ak)b0.

To incorporate negative frequency-dependent selection, we set condition(1): ∑{k}ak > c1, and condition(2): the fraction of cell satisfying (1) > c2. The parameter s is negative only when these two conditions are satisfied. Tumor growth was simulated until a predetermined population size of 100,000 cells was reached. 

### Simulations with subconal immune escape

We modeled immune escape by stochastically setting s = 0 for immune escaped cells regardless of its antigenicity. We allowed cancer cells to acquire immune escape with a probability of pe. pe is independent of antigenic mutation accumulation.
We chose parameters to represent different tumor-immune environments and studied literatures to estimate the parameter values in our model. 
The following parameters were used in all simulations:  b=0.5 [3,4], b0=0.4, m=5, p=0.1 , pe=10^-4 [5,6] (probability of immune escape, where applicable) [3, 35]. For the analyses where cells and tumors were classified as immunogenic or not, the cell and tumor immunogenicity thresholds c1=0.5 and c2=0.5 were used [2], unless stated otherwise. For simulation of purifying selection (PS), we set c1=c2=0.  

### Simulations with ICB therapy

Simulation of ICB consists of two parts: tumor growth simulation and ICB therapy initiation. Tumor grow until simulation time equals t1 (or any self-defined therapy time) when simulated tumors reach a population size of about 10,000 cells. Initiate ICB therapy by restoring the death rate of immune escaped cells from 1-b0 to 1-(1+s*∑{k}ak)b0 and eliminationg any newly acquired immune escape mutations (s<0). Quit simulation at time t2 to evaluate the effect of ICB therapy. 


### The base simulation of the model can be found in FrequencyDependent.py. All other files are based on the same code but contain small modifications, as explained in the header of each file.



#References

[1] Gillespie, D.T.: A general method for numerically simulating the stochastic time evolution of coupled chemical reactions. Journal of Computational Physics 22(4), 403–434 (1976)

[2] Lakatos, E., et al.: Evolutionary dynamics of neoantigens in growing tumors. Nature genetics 52(10), 1057–1066 (2020)

[3] Diefenbach, Andreas, et al.: Rae1 and H60 ligands of the NKG2D receptor stimulate tumour immunity." Nature 413.6852 (2001): 165-171.

[4] Dudley, Mark E., et al.: Cancer regression and autoimmunity in patients after clonal repopulation with antitumor lymphocytes." Science 298.5594 (2002): 850-854.

[5] Kayhanian, H., et al.: Mutation rate evolution drives immune escape in mismatch repair-deficient cancer. bioRxiv (2022)

[6] Aguad´e-Gorgori´o, G., Sol´e, R.: Tumour neoantigen heterogeneity thresholds provide a time window for combination therapy. JOURNAL OF THE ROYAL SOCIETY INTERFACE (2020)
