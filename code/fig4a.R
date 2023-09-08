library(ggpubr)
library(stringr)
library(jtools)
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
pdf(paste("fig4a.pdf",sep=""),width = 5, height = 5)
sub_neoantigen <- read.table('fig4a.txt',header=TRUE, sep="\t", na.strings="NA", dec=".", strip.white=TRUE)
sub_neoantigen$Patient<- str_replace(sub_neoantigen$Sample, "T[0-9]+$", "")


p1 <- scatter(sub_neoantigen, "meanCCF", "NTMB", 'Reuben_2017_npjGenomicMedcine')
print(p1)
dev.off()
