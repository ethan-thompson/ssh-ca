"""
Utilities for handling keys and certificates
"""

"""
Get existing ssh keys if they exist, otherwise return 0
"""
def get_ssh_keys():
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