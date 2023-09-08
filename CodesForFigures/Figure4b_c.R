#args = commandArgs(trailingOnly = TRUE)
#pat = args[1]
library(jtools)
library(ggpubr)
pre_scatter <- function(data, x, y, title){
    res2 <- cor.test(data[,x], data[,y],  method = "spearman")
    p_value <- res2$p.value
   estimate <- res2$estimate
    r_label <- paste("italic(rho)==",estimate,"~~italic(p)==",p_value, sep="")
    print(r_label)
    p <- ggscatter(data, x = x, y = y,
   add = "reg.line",  # Add regressin line
   add.params = list(color = "black", fill = "#fcf9cd",linetype="dashed"), # Customize reg. line
    fill = "#2b9fc9",color = "#2b9fc9",ellipse.alpha = 0.3,
   conf.int = TRUE,size = 4,
                title = title,
                xlab ="Subclonal antigenic mean CCF", ylab = "Number of subclonal antigenic mutations"# Add confidence interval
   )+annotate('text', label=r_label,
              hjust = -.2,vjust=2,
              x=-Inf, y=Inf, size = 7,
              parse=TRUE)+yscale("log10")+
	theme_apa(
  legend.pos = "right",
  legend.use.title = FALSE,
  legend.font.size = 15,
  x.font.size = 15,
  y.font.size = 15,
  facet.title.size = 15,
  remove.y.gridlines = TRUE,
  remove.x.gridlines = TRUE
)+font("xy.text", size = 15,color = "black")

	return(p)
}

on_scatter <- function(data, x, y, title){
    res2 <- cor.test(data[,x], data[,y],  method = "spearman")
    p_value <- res2$p.value
   estimate <- res2$estimate
    r_label <- paste("italic(rho)==",estimate,"~~italic(p)==",p_value, sep="")
    print(r_label)
    p <- ggscatter(data, x = x, y = y,
   add = "reg.line",  # Add regressin line
   add.params = list(color = "black", fill = "#fcf9cd",linetype="dashed"), # Customize reg. line
    fill = "#D7000F",color = "#D7000F",ellipse.alpha = 0.3,
   conf.int = TRUE,size = 4,
                title = title,
                xlab ="Subclonal antigenic mean CCF", ylab = "Number of subclonal antigenic mutations"# Add confidence interval
   )+annotate('text', label=r_label,
              hjust = -.2,vjust=2,
              x=-Inf, y=Inf, size = 7,
              parse=TRUE)+yscale("log10")+
	theme_apa(
  legend.pos = "right",
  legend.use.title = FALSE,
  legend.font.size = 15,
  x.font.size = 15,
  y.font.size = 15,
  facet.title.size = 15,
  remove.y.gridlines = TRUE,
  remove.x.gridlines = TRUE
)+font("xy.text", size = 15,color = "black")

	return(p)
	}
scatter <- function(data, x, y, title){
    res2 <- cor.test(data[,x], data[,y],  method = "spearman")
    p_value <- res2$p.value
   estimate <- res2$estimate
    r_label <- paste("italic(rho)==",estimate,"~~italic(p)==",p_value, sep="")
    print(r_label)
    p <- ggscatter(data, x = x, y = y,
   add = "reg.line",  # Add regressin line
   add.params = list(color = "black", fill = "#fcf9cd",linetype="dashed"), # Customize reg. line
    fill = "#f6b57b",color = "#f6b57b",ellipse.alpha = 0.3,
   conf.int = TRUE,size = 4,
                title = title,
                xlab ="Subclonal antigenic mean CCF", ylab = "Number of subclonal antigenic mutations"# Add confidence interval
   )+annotate('text', label=r_label,
              hjust = -.2,vjust=2,
              x=-Inf, y=Inf, size = 7,
              parse=TRUE)+yscale("log10")+
	theme_apa(
  legend.pos = "right",
  legend.use.title = FALSE,
  legend.font.size = 15,
  x.font.size = 15,
  y.font.size = 15,
  facet.title.size = 15,
  remove.y.gridlines = TRUE,
  remove.x.gridlines = TRUE
)+font("xy.text", size = 15,color = "black")

	return(p)
	}

#subclone <- list.files(path = "/data/public/Riaz_2017_Cell/results/6.neoantigen/seperate/results", pattern = pat,full.names = TRUE, recursive = TRUE)
#print(subclone)
sub_neoantigen <- read.table('fig4b_c.txt',header=TRUE, sep="\t", na.strings="NA", dec=".", strip.white=TRUE)
#for(i in 2:length(subclone)){
#    forsub <- read.table(subclone[i],header=TRUE, sep="\t", na.strings="NA", dec=".", strip.white=TRUE)
#    sub_neoantigen <- rbind(sub_neoantigen,forsub)
#}


pdf(paste("fig4b_c.pdf",sep=""),width =12, height = 6)

sub_neoantigen_TP <- sub_neoantigen[ with(sub_neoantigen,  grep("TO", Sample,invert=TRUE)) , ]
sub_neoantigen_TO <- sub_neoantigen[ with(sub_neoantigen,  grep("TO", Sample)) , ]
p2 <- pre_scatter(sub_neoantigen_TP, "meanCCF", "NTMB", 'Amato_2020_Cancers-Pre-therapy')
library(stringr)
sub_neoantigen$Patient<- str_replace(sub_neoantigen$Sample, "[TPO]+$", "")
response <- read.table("fig4b_c_b.txt",header=TRUE, sep="\t", na.strings="NA", dec=".", strip.white=TRUE)
merge_res <- merge(response,sub_neoantigen,by="Patient")
#merge_res <- merge_res[which(merge_res$NTMB > 50),]
CRPR <- merge_res[which((merge_res$Response == "CR"| merge_res$Response == "PR")),]
CDPD <- merge_res[which(merge_res$Response == "SD"| merge_res$Response == "PD"),]
CRPR <- CRPR[ with(CRPR,  grepl("TO", Sample)) , ]
CDPD <- CDPD[ with(CDPD,  grepl("TO", Sample)) , ]
p5 <- on_scatter(CDPD, "meanCCF", "NTMB", 'Amato_2020_Cancers-CD/PD')
combined_plot <- ggarrange(p2, p5, ncol = 2, nrow = 1)
print(combined_plot)
# Add correlation coefficient
dev.off()
