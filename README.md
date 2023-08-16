Purpose: To help developers keep track the amount of bugs that is encountered in the development phase. This will include:
- Creating a new Json file with a key ID number and writing details entered by the developer.
- Change the status of a bug

**Main Function**
This function will assign an id to a bug that's registered. There will be 3 options that the user will be able to do including:
- Create a new bug
- Change the status of a bug
- Exit Program
![[Pasted image 20230815192913.png]]
**Create a New Bug**
This part will ask for a name from the developer, and create a new Json file with an id number to it.
- Each file will begin as 0, and will increase by 1.  For example, lets say William encountered his  2nd bug and adds it to the lists of things needed to do, he will run the program fill out the prompts and the file name will be "bug-1.json"
![[Pasted image 20230815193039.png]]
Once this part is established, then information will be taken from the developer to keep easier track of the bug. This includes:
1. Developer's Name
2. Type of bug
3. Priority of the Bug
4. Bug Description
5. Status of the Bug
6. Time of Bug in Pacific and Military Time (this is done manually by the packages pytz and datetime)
![[Pasted image 20230815193134.png]]
Once the information is filled out, the Json file will look like this:
![[Pasted image 20230815193219.png]]

**Change Status of a Bug**
This function will take info about the bug and change the status of it as well. It will also display an update time of the bug as well so other developers know when the last time someone updated the bug status. It will look this this menu wise:
![[Pasted image 20230815193426.png]]

**Improving this in the Future**
In the future with more time for research and learning, I would rather use SQL or any other DB language to store bug information instead of Json files. I would also use more advanced features such as a react website with these services that numerous developers can pull bug reports from without having each developer install this code, email the reports or screenshot, etc.