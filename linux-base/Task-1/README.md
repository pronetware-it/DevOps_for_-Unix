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
  it is enough  execute the **who --all** command, the key will be given all the information, 
  you can see the time of the last system load, the current level of execution,  
  the name of the host or the IP address, from which the user has logged into system.
![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-base/1-1-3.gif)

4) Change personal information about yourself.

+ To change personal information, we use the **chfn** username command.
+ For check we use  **finger -lmsp** command.
![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-base/1-1-4.gif)

8) List the contents of the home directory using the ls command, define its files
and directories. Hint: Use the help system to familiarize yourself with the ls
command.
![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-base/1-1-8.gif)

## Task 1 Part 2 ##

1) Examine the **tree** command. Master the technique of applying a template, for
example, display all files that contain a character c, or files that contain a
specific sequence of characters. List subdirectories of the root directory up to
and including the second nesting level.

- tree -P RE* /home/serhii_rozhko/

- tree -L 2 /

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-base/1-2-1.gif)

2) What command can be used to determine the type of file (for example, text or
binary)? Give an example.

- To determine the type of file, we use the **file** utility
- Commanr file *
+ OUTPUT: 
  serhii_rozhko@ita-kh-077:~/DevOps_for_Unix/linux-base$ file -b 1-1-1.gif
  GIF image data, version 89a, 1035 x 250

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-base/1-2-2.gif)


3) Master the skills of navigating the file system using relative and absolute paths.
How can you go back to your home directory from anywhere in the filesystem?

- cd ~

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-base/1-2-3.gif)

4) Become familiar with the various options for the ls command. Give examples
of listing directories using different keys. Explain the information displayed on
the terminal using the -l and -a switches.

- key -l conclusion in a long format: Before file names, access mode is issued, 
  the number of links to the file, the names of the owner and group, 
  the size in bytes and the time of the last modification.

- key -a display a list of all files (without this option, hidden files are not displayed, the names of which begin at a point).

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-base/1-2-4.gif)

5) Perform the following sequence of operations:
   - create a subdirectory in the home directory;
   - in this subdirectory create a file containing information about directories
     located in the root directory (using I/O redirection operations);
   - view the created file;
   - copy the created file to your home directory using relative and absolute
     addressing.
   - delete the previously created subdirectory with the file requesting removal;
   - delete the file copied to the home directory.

   ```cd /home/
   mkdir -p dir
   cd ./dir
   sudo ls -la /root/ > root-dir.txt
   cat root-dir.txt
   cp root-dir.txt ~
   cp root-dir.txt /home/serhii_rozhko/
   rm -i -v root-dir.txt
   rm -i -v ~ root-dir.txt
   ```

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-base/1-2-5.gif)

6) Perform the following sequence of operations:
   - create a subdirectory test in the home directory;
   - copy the .bash_history file to this directory while changing its name to
     labwork2;
   - create a hard and soft link to the labwork2 file in the test subdirectory;
   - how to define soft and hard link, what do these
     concepts;
   - change the data by opening a symbolic link. What changes will happen and
     why
   - rename the hard link file to hard_lnk_labwork2;
   - rename the soft link file to symb_lnk_labwork2 file;
   - then delete the labwork2. What changes have occurred and why?

   ```cd ~
      mkdir -p link
      cp .bash_history ./link/LabWork2
      ln -s LabWork2 sym_lnk_lw2
      ln LabWork2 har_lnk_lw2
   ```

      To make sure that LabWork2 and har_lnk_lw2 are, in fact, the same file system object, 
      compare their index numbers by running the ls command along with the options 
      -l (display extended information), -i (display inode) and -h (use letters to indicate size):

    ```ls -lih
    ```

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-base/sc-2.png)

     The letter l in the group of file permissions signals to us that this file
     is a symbolic link to another file, which is also reflected in
     the file name - sym_lnk_lw2 -> LabWork2

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-base/sc-3.png)

     It can be seen that the index number of sym_lnk_lw2 differs from other numbers, 
     since for the file system these are already two independent objects. Also noticeable is the difference in the set of rights

     you can change the name, attributes of the link itself or redirect it to refer to another file,
     and the original file will not be affected
 
     You cannot rename a symbolic link or a hard link, you must use unlink to remove the links, 
     and create new links with the desired names.
    
    ```unlink har_lnk_lw2
       unlink sym_lnk_lw2

       ln -s LabWork2 symb_lnk_labwork2
       ln LabWork2 hard_lnk_labwork2

       rm -r ~/link
    ``` 
     The original file was left untouched


7) Using the locate utility, find all files that contain the squid and traceroute
   sequence.
   
  + sudo find / -name traceroute*
  + sudo find / -name squid*
 
![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-base/1-2-7.gif)

8) Determine which partitions are mounted in the system, as well as the types of
   these partitions.

9) Count the number of lines containing a given sequence of characters in a given
   file.

10) Using the find command, find all files in the /etc directory containing the
    host character sequence.
11) List all objects in /etc that contain the ss character sequence. How can I
    duplicate a similar command using a bunch of grep?

12) Organize a screen-by-screen print of the contents of the /etc directory. Hint:
    You must use stream redirection operations.
13) What are the types of devices and how to determine the type of device? Give
    examples.
14) How to determine the type of file in the system, what types of files are there?
15) * List the first 5 directory files that were recently accessed in the /etc
    directory.
