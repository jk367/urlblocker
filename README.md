# simple_blocker
This is a python script to block websites on a Mac. 

How it works: You vim into the blocked_websites file, then type the websites
that you wish to block, then you run the command: sudo python3 blocker.py 
You will be prompted to either block or unblock. 
If you block then the websites will be added to your etc/hosts file and then you will not be able to access them anymore. Unblocking will reverse this. 

You have to clear your browser cache and restart it, for this to take effect. 
