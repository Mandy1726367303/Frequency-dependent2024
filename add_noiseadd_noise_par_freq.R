source("/data/xieduo/Immun_genomics/shaoqing_simulation/CCF/add_noise/Fit_fun.R")
args = commandArgs(trailingOnly = TRUE)
CCF_freq_d <- read.table("/data/xieduo/Immun_genomics/shaoqing_simulation/CCF/freq_d/CCF.sum.tsv",header=TRUE)
prob_cn <- data.frame(CN=c(1:8),prob_cn=c(0,1,0,0,0,0,0,0)) ## no copy number variations
sample <- args[1]
#purity <- as.numeric(args[2])
purity=seq(0.2,0.8,by=0.2)  ## Given the purity
depth=seq(100,500,by=100)  ## Given the purity
#depth <- as.numeric(args[3])  ## Given the purity
fn <- paste0("/data/xieduo/Immun_genomics/shaoqing_simulation/CCF/add_noise/results/freq_d_",sample,"_purity_",purity,"_depth_",depth,".pdf")
pdf(fn,height = 9,width = 12)
opar<-par(no.readonly=T)
par(mfrow=c(3,3))
sfs <- vector("list", 4)
for (j in 1:4) {
  sfs[[j]] <- vector("list", 5)
}
#for(i in unique(CCF_freq_d$Sample)){
	CCF <- CCF_freq_d[which(CCF_freq_d$Sample == sample),]$CCF
	CCF <- CCF[CCF>0]
	vaf <- CCF/2
	for (j in 1:length(purity)){
		for(k in 1:length(depth)){
		sfs[[j]][[k]]=corrected.SFS.plot(sampName = sample,simAF = vaf,sampAF = NULL,prob_cn = prob_cn,
                                        sampCN=NULL, purity=purity[j], ploidy=2,
                                        NB_size=1.5, NB_mu=depth[k],
                                        maxdepth=1000, minAF=0.02, binw=0.01,
                                        plotAF=TRUE, pdf=FALSE, widthadj=0, AD = 4,
                                        heightadj=0, colors=c("#de2d26","#3288bd"))	
	}
}
#}

par(opar)
dev.off()
fn <- paste0("/data/xieduo/Immun_genomics/shaoqing_simulation/CCF/add_noise/results/freq_d_",sample,".RData")
print(fn)
save(sfs, file = fn)
