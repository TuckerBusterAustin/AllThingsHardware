import os
import paramiko
import concurrent.futures

# log in data
remote_hosts = []
file_path = 'INSERT FILE PATH
with open(file_path, 'r') as file:
        for line in file:
            remote_hosts.append(line.strip())
print(remote_hosts)

remote_user = "username"
remote_pass = "passwor"


#log file paths
log_file_path1 = "INSERT LOG PATH"
os.makedirs(log_file_path1, exist_ok=True)
log_file_names = [f"{remote_host}_system_info.log" for remote_host in remote_hosts]

# path + file names
log_files = [os.path.join(log_file_path1, log_file_name) for log_file_name in log_file_names]

# collecting system information
def collect_system_info(remote_host):
    try:
        # create ssh client(object)
        ssh_client = paramiko.SSHClient()

        # auto add remote hosts ssh key
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # password based connection
        ssh_client.connect(hostname=remote_host, username=remote_user, password=remote_pass)

        # Collect system info/configs(can add more)
        stdin, stdout, stderr = ssh_client.exec_command("lshw && lspci && lscpu && dmidecode")

        # check if execution went correctly
        if stderr.read():
            print(f"ERROR: Could not collect system information from remote system {remote_host}")
        else:
            # Log the system info to log file(may need to expand)
            with open(log_files[remote_hosts.index(remote_host)], "a") as f:
                f.write(stdout.read().decode())
            print(f"System information collected and logged to {log_files[remote_hosts.index(remote_host)]} for {remote_host}")

        # ssh connection close
        ssh_client.close()

    except paramiko.AuthenticationException:
        print(f"ERROR: Authentication failed for remote system {remote_host}")
    except paramiko.SSHException as e:
        print(f"ERROR: SSH connection failed for remote system {remote_host}: {str(e)}")
    except Exception as e:
        print(f"ERROR: An error occurred while collecting system information from remote system {remote_host}: {str(e)}")

# Create a thread pool to run the collection function for each remote host
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(collect_system_info, remote_host) for remote_host in remote_hosts]

#step 1: collect host names
#step 2: collect bmc names
#step 3:activate git environment
#step 4:run command 
#step 5:
#step 6:
#step 7: