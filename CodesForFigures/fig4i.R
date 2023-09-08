# Load survival package
library(survival)
library("survminer")



survival <- read.table('survival.tsv',sep='\t',header=TRUE)

fit <- survfit(Surv(OS, dead) ~ Neutral, data = survival)

# Summary of survival curves
summary(fit)
# Access to the sort summary table
summary(fit)$table

# Change color, linetype by strata, risk.table color by strata

surv_plot <- ggsurvplot(fit,
          pval = TRUE, conf.int = TRUE,
          risk.table = TRUE, # Add risk table
           legend.labs = c("High R square", "Low R square"),
           legend.title = "",
          risk.table.col = "strata", # Change risk table color by groups
          linetype = "strata", # Change line type by groups
          surv.median.line = "hv", # Specify median survival
          palette = c("#E7B800", "#2E9FDF"),
          font.main = c(22, "bold", "black"), 
  font.submain = c(20, "bold", "black"), 
  font.caption = c(14, "plain", "black"), 
  font.x = c(16, "bold", "black"),
  font.y = c(16, "bold", "black"),
  font.tickslab = c(12, "plain", "black"))
pdf('fig4i.pdf',width = 6,height = 8)

print(surv_plot)
dev.off()
