library(tidyr)
library(stringr)
dat <- read.table('all_maf',header=TRUE,sep='\t')
#dat <- maf
library(corrplot)
cumMut <- function(mut,f){
  ms = c()
  for(i in f){
    ms=c(ms,length(mut[which(mut>i)]))
  }
  return(ms)
}
response <- read.table("fig4h_b.txt",header=TRUE, sep="\t", na.strings="NA", dec=".", strip.white=TRUE)
dat$ID <- paste(dat$Patient_ID, ":", dat$Tumor_Sample_Barcode,sep="")
dat$tumor <- paste(dat$Patient_ID,dat$Tumor_Sample_Barcode, sep="")

samples <- as.vector(unique(dat$ID))
min_vaf = 0.1
num_neutral = 0
dat <- dat[which(dat$CCFa_upper < 1 & dat$CCF > min_vaf*2),]

pdf("neutral_prediction_CCFa_upper.pdf", width=9, height=9)
par(mfrow = c(3, 3))

num = 0
r.squared.p <- c()
cancer.type <- c()
num.subclonal <- c()
primary.sample <- c()

info <- list()
for (pt in samples){
    real_patient <- str_split(pt,":",simplify = TRUE)[1]
    print(real_patient)
  pdat <- dat[which(dat$ID==pt),]
  if(nrow(pdat)>20) { #select samples which variants num >20
    #hist(pdat$CCF/2, breaks=round(nrow(pdat)/10+10), main=paste(pt,"_Primary_CCF", sep=""), xlab="VAF", ylab="Frequency", xlim=c(0,0.5), col="#9ecae1", cex.main=0.8)
    muts_vaf <- as.numeric(pdat$CCF)/2
	max_vaf <- max(muts_vaf)
	x=seq(min_vaf,max_vaf,0.005)
    res <- response[which(response$Patient==real_patient),]$Response[1]
    y=cumMut(muts_vaf,x)

    xx=1/x
    fit = lm(y~xx)

    para = summary(fit)
    r.squared.p <- c(r.squared.p, para$adj.r.squared)
    num.subclonal <- c(num.subclonal, nrow(pdat))
  #  cancer.type <- c(cancer.type, as.character(pdat$CancerType[1]))
    primary.sample <- c(primary.sample, pt)

    plot(1/x,y, axes = FALSE, xlab="1/alpha",ylab="Cumulative # of muts", main=paste(res,";", pt,"\nR^2:",para$adj.r.squared,sep=""),
         cex.lab=1.2, cex.main=1.2, xlim=c(1/max_vaf,1/min_vaf), ylim=c(0,length(muts_vaf)+20), cex.axis=1.1, col = "blue", cex=2)

    axis(1, at=c(1/max_vaf,1/0.15,1/min_vaf), labels=c("1/0.3","1/0.15","1/0.1"),cex.axis=1.1)
    axis(2, at=seq(0,length(muts_vaf)+20,20),labels=seq(0,length(muts_vaf)+20,20),cex.axis=1.1)
    box()
    abline(fit,lty=1,col="red",lwd=2)

    if(para$adj.r.squared>0.98){
      print("###############")
      print(pt)
      print(para$adj.r.squared)
      num_neutral = num_neutral +1

    }

    num = num +1
    info[[num]]<-data.frame(Patient_ID=pdat$Patient_ID,Tumor_Sample_Barcode=pdat$Tumor_Sample_Barcode,r.squared=para$adj.r.squared)

  }
}


info <-unique(do.call("rbind", lapply(info, as.data.frame))[,1:3])
info$Prediction <- ifelse(info$r.squared >0.98, "neutral", "non-neutral")
info$note <- NA
info[1,5]<-paste("num_neutral",":",num_neutral)
info <- merge(info,response,by.x='Patient_ID',by.y='Patient')
purity <- read.table("TitanCNA_purity_ploity_depth_choice.txt",header = T)

info$a<-paste(info$Patient_ID,info$Tumor_Sample_Barcode,sep="")
purity <- subset(purity, sample %in% info$Tumor_Sample_Barcode)
hist(info$r.squared, plot = T,main = paste("Histogram of R squared"),xlab="R squared", col="salmon")
mat<-data.frame(r.squared=info$r.squared, purity=purity$purity,ploidy=purity$ploidy,mean_depth=purity$depth)
x<-cor(mat)
corrplot(x, type="upper", order="hclust",tl.cex=2,tl.col = "black")

x<-cor(purity[,2:4])
corrplot(x, type="upper",order="hclust",tl.cex=2,tl.col = "black")
pairs(~purity$ploidy+purity$purity+purity$depth,col="blue",upper.panel=NULL,labels=c("ploidy","purity","depth"))

library(ggpubr)
library(jtools)
library(stringr)
#info$res <- 'CR/PR'
#info$res[info$Response == 'PD' | info$Response == 'SD'] <- 'SD/PD'
#info <- info[which(info$Sample),]
info$Res <- 'NA'
info$Res[info$Response == 'PD' | info$Response == 'SD'] <- 'SD_PD'
info$Res[info$Response == 'CR' | info$Response == 'PR'] <- 'CR_PR'
info <- info[which(info$Res != 'NA'),]
pdf("Amato_2020_Cancers_neutral_prediction.pdf", width=4.8, height=6)

# Perform a one-sided t-test
comparison <- wilcox.test(info$r.squared[info$Res == "SD_PD"],info$r.squared[info$Res == "CR_PR"], 
                     alternative = "greater") # alternative can be "less" for a lower tailed test
print(comparison)
p <- ggboxplot(info, x = "Res", y = "r.squared",
                 palette =c("#D0C295", "#718374"),
                add = "jitter", fill = "Res")+theme_apa(
  legend.pos = "right",
  legend.use.title = FALSE,
  legend.font.size = 15,
  x.font.size = 15,
  y.font.size = 15,
  facet.title.size = 15,
  remove.y.gridlines = TRUE,
  remove.x.gridlines = TRUE
)+font("xy.text", size = 15,color = "black")+ylab(expression(italic("R"^2*"")))+scale_x_discrete(limits = c("SD_PD","CR_PR"))
             # Add global p-value
my_comparisons <- list( c("CR_PR", "SD_PD") )
p + stat_compare_means(comparisons = my_comparisons)+ # Add pairwise comparisons p-value
  rremove("legend")+rremove("xlab")
dev.off()
