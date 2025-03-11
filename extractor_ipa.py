import paramiko
import getpass
import os

# Get app name from user
app_name = input("Enter the app name: ")
ip_address = input("Enter the iPhone IP address: ")
password = getpass.getpass("Enter root password (default: alpine): ")

def ssh_command(ssh, command):
    stdin, stdout, stderr = ssh.exec_command(command)
    return stdout.read().decode(), stderr.read().decode()

def main():
    try:
        # SSH into iPhone
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip_address, port=22, username='root', password=password)
        print("Connected to iPhone.")

        # Navigate to Application Directory
        ssh_command(ssh, "cd /var/containers/Bundle/Application")
        
        # Identify the Application Container
        stdout, stderr = ssh_command(ssh, f"ls * | grep -B 2 -I '{app_name}'")
        if stderr:
            print("Error finding app container:", stderr)
            return
        
        container_id = stdout.strip().split('\n')[-1]  # Get last line as container ID
        print("Found container ID:", container_id)

        # Navigate to container
        ssh_command(ssh, f"cd /var/containers/Bundle/Application/{container_id}")
        ssh_command(ssh, "mkdir Payload")
        ssh_command(ssh, f"cp -r {app_name}.app/ Payload/")
        ssh_command(ssh, f"zip -r /tmp/{app_name}.ipa Payload/")
        ssh_command(ssh, f"zip -u /tmp/{app_name}.ipa iTunesMetadata.plist")
        print("IPA file created at /tmp/{app_name}.ipa")

    	# Copy IPA file to local machine
        local_path = os.path.join(os.getcwd(), f"{app_name}.ipa")
        sftp = ssh.open_sftp()
        sftp.get(f"/tmp/{app_name}.ipa", local_path)
        print(f"IPA file copied to {local_path}")

    	# Close connection
        sftp.close()
        ssh.close()
        print("Done")

    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()
