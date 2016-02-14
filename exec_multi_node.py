import paramiko
import os

hosts = './hosts'

# To run the commands on all the nodesby doing ssh
def run_on_all_nodes():
        # Edit with your command
        command1 = 'pkill iperf'
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        for line in open(hosts).readlines():
                hostname = line.strip('\n')
                try:
                        #ssh.connect(hostname, username='root', password='cisco123', timeout=5)
                        ssh.connect(hostname, timeout=5)
                        stdin, stdout, stderr = ssh.exec_command(command1)
                        print "Done for : " + hostname
                except Exception as e:
                        print "Login Failed: %s : %s" (hostname, str(e))


# To run commands(like ssh-copy-id   scp etc) for all the nodes
def run_for_all_nodes():
        for line in open(hosts).readlines():
                command2 = 'scp /etc/hosts %s:/etc/hosts' % (line.strip('\n'))
                print "Executing for : %s" % (line.strip('\n'))
                os.system(command2)
