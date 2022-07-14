## Task 1 Part 1 ##
1) Log in to the system as root.

+ To enter the system under the root of the user, we use the **sudo su** command.
![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-base/1-1-1.gif)

2) Use the passwd command to change the password. Examine the basic parameters of the command. 
   What system file does it change *?

+ Under the user account, the passwd team can only change the password of this account.
  The team executed from root can change the password of any account.
+ The passwd team makes changes to the **/etc/shadow** file
![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-base/1-1-2.gif)

3) Determine the users registered in the system, as well as what commands they
execute. What additional information can be gleaned from the command
execution?

+ To get information about registered users in the system, 
  it is enough  execute the who --all command, the key will be given all the information, 
  you can see the time of the last system load, the current level of execution,  
  the name of the host or the IP address, from which the user has logged into system.
![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-base/1-1-3.gif)
