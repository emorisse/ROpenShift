directory <- Sys.getenv("OPENSHIFT_REPO_DIR");
pkgs <- read.csv(file.path(directory,"required.R"), header=F)
f <- NA
for ( p in pkgs ) {
	rm(f)
	try(f <- library(p))
	if ( ! exists("f") ) 
		try(install.packages(p, repos="http://cran.us.r-project.org"))
	else
		print("package", p, "already loaded")
}
