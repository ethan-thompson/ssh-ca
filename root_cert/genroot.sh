#!/bin/bash

#create public/private keys
ssh-keygen -t rsa -b 4096 -m PEM -f root_key -q -N ""

#create self-signed cert with keys
openssl req -new -x509 -key root_key -out myroot.pem -days 365 -config config

#convert to crt
openssl x509 -in myroot.pem -inform PEM -out myroot.crt