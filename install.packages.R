getwd()
pkgs <- read.csv("${OPENSHIFT_REPO_DIR}required.R")
for ( p in packages ) {
	install.packages(p, repos="http://cran.us.r-project.org")
}
