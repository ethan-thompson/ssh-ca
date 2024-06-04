#!/bin/bash

#This script will create and sign client ssh keys

#create keys
ssh-keygen -q -t rsa -b 4096 -N '' -f user_key -m PEM

#sign public key
# The key will be signed and valid from 5 mins prev (for clock drift) until 30 mins from the time it was signed.
ssh-keygen -s ../root_cert/root_key -I "$(whoami)@$(hostname) user key" -n "$(whoami)" -V -5m:+30m user_key.pub