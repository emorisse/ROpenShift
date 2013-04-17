pkgs <- read.csv("required.R")
for ( p in packages ) {
	install.packages(p, repos="http://cran.us.r-project.org")
}

