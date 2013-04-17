directory <- Sys.getenv("OPENSHIFT_REPO_DIR");
pkgs <- read.csv(file.path(directory,"required.R"), header=F)
for ( p in pkgs ) {
	install.packages(p, repos="http://cran.us.r-project.org")
}
