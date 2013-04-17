directory <- Sys.getenv("OPENSHIFT_REPO_DIR");
pkgs <- read.csv(file.path(directory,"required.R"), header=F)
for (p in pkgs) {
	ver <- NA
	try(ver<-packageVersion(p),silent=T)
	if ( is.na(ver) )
		try(install.packages(p, repos="http://cran.us.r-project.org"))
}
