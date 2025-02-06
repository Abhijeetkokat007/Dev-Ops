# Linux Commands Cheat Sheet

## 1. File and Directory Management
```sh
ls          # List files in a directory
cd          # Change directory
pwd         # Print current working directory
mkdir       # Create a new directory
rmdir       # Remove empty directory
rm -r       # Remove directory and its contents
cp          # Copy files and directories
mv          # Move or rename files
find        # Search for files and directories
locate      # Find files quickly using a database
tree        # Display directory structure in tree format
```

## 2. File Operations
```sh
cat         # Display contents of a file
less        # View file contents one page at a time
head        # View first 10 lines of a file
tail        # View last 10 lines of a file
touch       # Create an empty file
nano        # Open nano text editor
vim         # Open vim text editor
grep        # Search for patterns in a file
diff        # Compare two files
sort        # Sort file contents
cut         # Extract specific columns from a file
```

## 3. File Permissions and Ownership
```sh
ls -l       # List files with permissions
chmod       # Change file permissions
chown       # Change file owner
chgrp       # Change file group
```

## 4. Process Management
```sh
ps          # Show running processes
top         # Show real-time system usage
htop        # Interactive process viewer
kill        # Kill a process by PID
pkill       # Kill a process by name
bg          # Resume a suspended process in the background
fg          # Resume a suspended process in the foreground
nohup       # Run a process immune to hangups
jobs        # Show background jobs
```

## 5. User Management
```sh
whoami      # Show the current user
who         # Show logged-in users
id          # Display user ID (UID) and group ID (GID)
adduser     # Create a new user
deluser     # Delete a user
passwd      # Change user password
usermod     # Modify user account
groupadd    # Create a new group
groups      # Show user groups
```

## 6. Disk and Storage Management
```sh
df -h       # Show disk usage
du -sh      # Show directory size
mount       # Mount a filesystem
umount      # Unmount a filesystem
lsblk       # List all block devices
fdisk       # Partition a disk
mkfs        # Create a filesystem
```

## 7. Networking
```sh
ifconfig    # Show network interfaces (deprecated, use 'ip')
ip a        # Show IP addresses
ping        # Check connectivity to a host
netstat -tulnp  # Show active network connections
ss -tulnp   # Alternative to 'netstat'
curl        # Fetch data from URLs
wget        # Download files from the internet
scp         # Securely copy files between hosts
rsync       # Synchronize files between machines
hostname    # Show or set the system's hostname
nslookup    # Query DNS records
```

## 8. Package Management
### Debian-based Systems (`apt`)
```sh
apt update     # Update package list
apt upgrade    # Upgrade installed packages
apt install    # Install a package
apt remove     # Remove a package
```
### RedHat-based Systems (`yum` / `dnf`)
```sh
yum install    # Install a package
yum remove     # Remove a package
dnf install    # Install a package (modern version of yum)
```
### Arch-based Systems (`pacman`)
```sh
pacman -S      # Install a package
pacman -R      # Remove a package
```

## 9. System Monitoring
```sh
uptime      # Show system uptime
free -h     # Show memory usage
vmstat      # Show system performance stats
iostat      # Show CPU and disk usage
sar         # Collect and report system activity
```

## 10. Logs and System Information
```sh
dmesg       # Show boot logs
journalctl  # View systemd logs
uname -a    # Show system information
cat /etc/os-release  # Show OS version
lscpu       # Show CPU information
lsblk       # List block devices
lspci       # Show PCI devices
lsusb       # Show USB devices
```

## 11. Compression and Archiving
```sh
tar -cvf archive.tar file     # Create a tar archive
tar -xvf archive.tar         # Extract a tar archive
tar -czvf archive.tar.gz file  # Create a compressed tar archive
tar -xzvf archive.tar.gz      # Extract a compressed tar archive
zip archive.zip file         # Create a zip file
unzip archive.zip            # Extract a zip file
```

## 12. Scheduling Tasks
```sh
cron         # Background job scheduler
crontab -e   # Edit user’s cron jobs
at           # Schedule a one-time job
systemctl enable <service>  # Enable a service at boot
systemctl disable <service> # Disable a service at boot
```

## 13. Power Management
```sh
shutdown -h now  # Shutdown system immediately
reboot           # Reboot system
poweroff         # Power off system
