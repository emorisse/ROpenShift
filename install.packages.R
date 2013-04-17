directory <- Sys.getenv("OPENSHIFT_REPO_DIR");
pkgs <- read.csv(file.path(directory,"required.R"), header=F)
f <- NA
for ( p in pkgs ) {
	rm(f)
	try(f <- require(p))
	if ( f == FALSE )  {
		try(install.packages(p, repos="http://cran.us.r-project.org"))
	}
	else
		print("package", p, "already loaded")
}
