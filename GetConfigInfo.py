import paramiko
from jproperties import Properties
def getSShConnection(host, user, password, port):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(host, port, user, password)
    return client


def readRemoteFile(client, filepath):
    sftp_client = client.open_sftp()
    remote_file = sftp_client.open(filepath)
    file = []
    try:
        for line in remote_file:
            file.append(line)
        return file
    finally:
        remote_file.close()

def printJavaProperies():

    client = getSShConnection('169.254.10.67', 'intertrust', '39CgjVfkHtf<ea', 3322)
    file_prop = readRemoteFile(client,'/home/intertrust/server.properties')

    for x in file_prop:
       if ((str(x).startswith('#'))==False):
           print(x)

printJavaProperies()