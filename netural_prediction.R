args = commandArgs(trailingOnly = TRUE)
library(tidyr)
library(stringr)
library(corrplot)
freq_fn <- args[1]
all_data <- read.table(freq_fn,header=TRUE, sep="\t", na.strings="NA", dec=".", strip.white=TRUE)
purity_ls <- seq(0.2,0.8,by=0.2)
depth_ls <- seq(100,500,by=100)
for (j in 1:length(purity_ls)){
	for(k in 1:length(depth_ls)){
		purity <- purity_ls[j]
		depth <- depth_ls[k]
		dat <- all_data[which(all_data$purity == str_c(purity) & all_data$depth == depth),]
		max_vaf = 0.3

		samples <- as.vector(unique(dat$Sample))
		min_vaf = 0.015
		num_neutral = 0
		#####Clonal mutations were defined as having a cancer cell fraction ≥0.8,
		####while other mutations were defined as subclonal;
		#####we chose this definition as a simple conservative approach with high specificity.
		dat <- dat[which(dat$VAF > min_vaf & dat$VAF < max_vaf),]

		file_name <- paste("neutral_test_noise_depth_",depth,"_purity_",purity,".pdf",sep='')
		pdf(file_name, width=9, height=9)
		par(mfrow = c(3, 3))
		cumMut <- function(mut,f){
		  ms = c()
		  for(i in f){
			ms=c(ms,length(mut[which(mut>i)]))
		  }
		  return(ms)
		}

		samples <- as.vector(unique(dat$Sample))

		num = 0
		r.squared.p <- c()
		cancer.type <- c()
		num.subclonal <- c()
		primary.sample <- c()

		info <- list()

		for (pt in samples){
			real_patient <- pt
		  pdat <- dat[which(dat$Sample==pt),]
		  if(nrow(pdat)>5) { #select samples which variants num >20
			#hist(pdat$CCF/2, breaks=round(nrow(pdat)/10+10), main=paste(pt,"_Primary_CCF", sep=""), xlab="VAF", ylab="Frequency", xlim=c(0,0.5), col="#9ecae1", cex.main=0.8)
			muts_vaf <- as.numeric(pdat$VAF)
			max_vaf <- max(muts_vaf)
			x=seq(min_vaf,max_vaf,0.005)
			y=cumMut(muts_vaf,x)

			xx=1/x
			fit = lm(y~xx)

			para = summary(fit)
			r.squared.p <- c(r.squared.p, para$adj.r.squared)
			num.subclonal <- c(num.subclonal, nrow(pdat))
			cancer.type <- c(cancer.type, as.character(pdat$CancerType[1]))
			primary.sample <- c(primary.sample, pt)

			plot(1/x,y, axes = FALSE, xlab="1/alpha",ylab="Cumulative # of muts", main=paste( pt,"\nR^2:",para$adj.r.squared,sep=""),
				 cex.lab=1.2, cex.main=1.2, xlim=c(1/max_vaf,1/min_vaf), ylim=c(0,length(muts_vaf)+20), cex.axis=1.1, col = "blue", cex=2)

			axis(1, at=c(1/max_vaf,1/0.15,1/min_vaf), labels=c("1/0.3","1/0.15","1/0.1"),cex.axis=1.1)
			axis(2, at=seq(0,length(muts_vaf)+20,20),labels=seq(0,length(muts_vaf)+20,20),cex.axis=1.1)
			box()
			abline(fit,lty=1,col="red",lwd=2)

			if(para$adj.r.squared>0.98){
			  print("###############")
			  num_neutral = num_neutral +1

			}

			num = num +1

			info[[num]]<-data.frame(Patient_ID=pdat$Sample,r.squared=para$adj.r.squared)

		  }
		}

		info <-unique(do.call("rbind", lapply(info, as.data.frame)))
		info$Prediction <- ifelse(info$r.squared >0.98, "neutral", "non-neutral")
		info$purity <- purity
		info$depth <- depth
		#info$Type <- 'Freq_d'
		info$Type <- 'Pervasive'
		#file_name <- paste0("Freq_d_neutral_test_noise_depth_",depth,"_purity_",purity,".txt")
		file_name <- paste0("Pervasive_neutral_test_noise_depth_",depth,"_purity_",purity,".txt")
		write.table(info, file_name,sep='\t',quote=F,row.names=F)
		dev.off()
		
			}

}

#write.table(empty_df, 'freq_d.tsv',sep='\t',quote=F,row.names=F)
