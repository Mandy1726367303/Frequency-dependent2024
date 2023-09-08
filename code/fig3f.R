dat <- read.table('freq_d.tsv',header=TRUE, sep="\t", na.strings="NA", dec=".", strip.white=TRUE)
dat <- dat[which(dat$CCF > 0),]
library(tidyr)
library(stringr)
library(corrplot)

cumMut <- function(mut,f){
  ms = c()
  for(i in f){
    ms=c(ms,length(mut[which(mut>i)]))
  }
  return(ms)
}

samples <- as.vector(unique(dat$Sample))
min_vaf = 0.02
max_vaf = 0.3
num_neutral = 0
#####Clonal mutations were defined as having a cancer cell fraction ≥0.8,
####while other mutations were defined as subclonal;
#####we chose this definition as a simple conservative approach with high specificity.
#dat <- dat[which(dat$CCF > min_vaf*2 & dat$CCF < 2*max_vaf),]
dat <- dat[which(dat$CCF > min_vaf*2 ),]

library(tidyr)
library(stringr)
library(corrplot)

#pdf("neutral_test.pdf", width=9, height=9)
par(mfrow = c(3, 3))
cumMut <- function(mut,f){
  ms = c()
  for(i in f){
    ms=c(ms,length(mut[which(mut>i)]))
  }
  return(ms)
}

#####Clonal mutations were defined as having a cancer cell fraction ≥0.8,
####while other mutations were defined as subclonal;
#####we chose this definition as a simple conservative approach with high specificity.

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
    muts_vaf <- as.numeric(pdat$CCF)/2
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
fq_info <- info


dat <- read.table('pervasive.tsv',header=TRUE, sep="\t", na.strings="NA", dec=".", strip.white=TRUE)
dat <- dat[which(dat$CCF > 0),]

samples <- as.vector(unique(dat$Sample))
num_neutral = 0
#####Clonal mutations were defined as having a cancer cell fraction ≥0.8,
####while other mutations were defined as subclonal;
#####we chose this definition as a simple conservative approach with high specificity.
#dat <- dat[which(dat$CCF > min_vaf*2 & dat$CCF < 2*max_vaf),]
dat <- dat[which(dat$CCF > min_vaf*2 ),]

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
    muts_vaf <- as.numeric(pdat$CCF)/2
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
fq_info$Type <- 'Freq_d'
info$Type <- 'Pervasive'
merge_info <- rbind(fq_info, info)
library(ggpubr)
#dev.off()
library(jtools)
library(stringr)
pdf("fig3f.pdf", width=4.8, height=6)
p <- ggboxplot(merge_info, x = "Type", y = "r.squared",
                 #palette =c("#4681b4", "#cd5b5c"),
                 #palette =c("#00AFBB", "#E7B800"),
                 palette =c("#E7B800","#00AFBB"),
                add = "jitter", fill = "Type")+theme_apa(
  legend.pos = "right",
  legend.use.title = FALSE,
  legend.font.size = 15,
  x.font.size = 15,
  y.font.size = 15,
  facet.title.size = 15,
  remove.y.gridlines = TRUE,
  remove.x.gridlines = TRUE
)+font("xy.text", size = 15,color = "black")+ylab(expression(italic("R"^2*"")))
             # Add global p-value
my_comparisons <- list( c("Freq_d", "Pervasive") )
p <- p + stat_compare_means(comparisons = my_comparisons)+rremove("legend")+rremove("xlab")
print(p)
#write.table(merge_info,"neutral_test.txt",sep='\t',quote=F,row.names=F)
dev.off()




