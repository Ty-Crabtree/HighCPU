import paramiko
import argparse
from simple_colors import *
import animation


class Connect:


    def __init__(self):
        self.commands = {"High-CPU" : "sudo modprobe -r acpi_pad"}
        parser = argparse.ArgumentParser()
        parser.add_argument('--host', type=str,  default="nd-4ec4.solr.pdx.smarshinc.com")
        parser.add_argument('--username', type=str)
        parser.add_argument('--password', type=str)
        parser.add_argument('--command', type=str,  default="pwd")
        parser.add_argument('--port', type=str,  default="22")

        # Parse the argument
        self.arg = parser.parse_args()
        self.host = self.arg.host
        if not self.arg.username:
            self.username = input(yellow("Please enter your username: "))
        else:
            self.username = self.arg.username
        if not self.arg.username:
            self.password = input(yellow("Please enter your password: "))
        else:
            self.password = self.arg.password
        self.command = self.arg.command
        self.port = self.arg.port

    @animation.simple_wait
    def ssh_connection(self):
        print()
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(self.host, self.port, self.username, self.password)
            print(green("SSH connection established."))
        except Exception as e:
            print(red(e))
            exit()


    def execute_remote_command(self):
        try:
            print(green(f"Running {self.command}"))
            stdin, stdout, stderr = self.ssh.exec_command(self.command)
            lines = stdout.readlines()
            print(green(f"Command Output: {lines})"))
        except Exception as e:
            print(red(e))



    def main(self):
        self.ssh_connection()
        self.execute_remote_command()


if __name__ == '__main__':
    connect = Connect()
    connect.main()
