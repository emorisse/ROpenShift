ROpenShift - Running R and ryp2 on OpenShift.com
==========

Running R on OpenShift is easy, but not simple.  You must install R as a user and tell python (rpy2) where to find it.

This repo includes R v2.15 compiled to run on RHEL 6.2 (base OS for OpenShift.com), as well as the OpenShift.com specific necessities. 

WARNING: If you just close this repo and upload to OpenShift.com it will not work.  There are a few more manual steps, see: README.Rinstall for tips.
