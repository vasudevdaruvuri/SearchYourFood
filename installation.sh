#!/bin/bash
yum install wget 
wget  http://mirrors.cat.pdx.edu/epel/7/x86_64/e/epel-release-7-5.noarch.rpm
yum install epel-release-7-5.noarch.rpm
yum -y install python-pip
pip install beautifulsoup4
pip install html5lib
