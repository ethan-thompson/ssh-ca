"""
Utilities for handling keys and certificates
"""

import subprocess

"""
Get existing ssh keys if they exist, otherwise generate keys. If successful, this will return the filename of a loaded key
"""
def get_ssh_keys():
    # Check if any keys are currently loaded in ssh
    # Throw this in a try in case no matching keys exist for this host
    try:
        key_list = subprocess.check_output('ssh-add -l | grep -e "$(whoami)@$(hostname)"', shell=True, universal_newlines=True).split('\n')

        # Remove the extra empty entry in the list (from when we split with newline)
        key_list = key_list[0:len(key_list) - 1]

        # Get a list of available keys in the .ssh folder

        # Iterate through the list and see which keys are associated with which files in the users .ssh file

        # Pick a key, and return the filename

    except Exception as e:
        # Check if the exception was raised because there were no keys
        if ("returned non-zero exit status 1." in e):
            # No keys exist, so let's generate some
            return gen_ssh_keys()
        
        # A different error occured
        print("Error: ", e)
    
    # ssh-keygen -l -f ~/.ssh/id_ecdsa.pub
    subprocess.check_output('ssh-keygen -l -f ~/.ssh/id_ecdsa.pub', shell=True, universal_newlines=True).split('\n')


    return 0

"""
Generate ssh keys for the user.
"""
def gen_ssh_keys():
    return 0

"""
Check for an existing certificate for the destination host.
"""
def get_ssh_cert(dest_host_id):
    return 0

"""
Verify the existing certificate for the destination host is valid. Will need to be verified by the CA server.
"""
def verify_cert(cert, dest_host_id):
    return 0

"""
Requests an ssh certificate from the CA server. Returns a signed ssh certificate on success.
"""
def req_ssh_cert(pub_key, dest_host_id):
    return 0

"""
Configure ssh to use a certificate for the specified destination host
"""
def configure_ssh(cert, dest_host_id):
    return 0