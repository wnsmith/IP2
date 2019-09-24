install.packages("factoextra")
install.packages("cluster")

library(factoextra)
library(cluster)

dataset = read.csv(header = FALSE, sep = ",", file = "transposedData.txt")
head(dataset, nrows = 3)
x = as.matrix(sapply(dataset, as.numeric)) 


fviz_nbclust(dataset, FUNcluster = clara, method = "silhouette", diss = NULL, k.max = 10, nboot = 100, verbose = interactive(), barfill = "steelblue", barcolor = "steelblue", linecolor = "steelblue", print.summary = TRUE)

clara.results = clara(x, 4, samples = 50, pamLike = TRUE)
print(clara.results)

fviz_cluster(clara.results, data = NULL, choose.vars = NULL, stand = TRUE,
             axes = c(1, 2), geom = c("point", "text"), repel = FALSE,
             show.clust.cent = TRUE, ellipse = TRUE, ellipse.type = "convex",
             ellipse.level = 0.95, ellipse.alpha = 0.2, shape = NULL,
             pointsize = 1.5, labelsize = 12, main = "Cluster plot", xlab = NULL,
             ylab = NULL, outlier.color = "black", outlier.shape = 19,
             ggtheme = theme_grey())

