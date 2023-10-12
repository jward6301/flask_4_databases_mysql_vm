# flask_4_databases_mysql_vm
HHA 504 Week 4B assignment

## Azure VM Setup
1. Log into the Azure portal.
2. Search for Virtual Machines.
3. Once that page is loaded, click on create and select the first option Azure Virtual Machine.
4. Subscription should be selected to Azure for students. You can create a new resource group or choose an existing one, I created a new one for this assignment
5. Under Instance details, only a few changes need to be made. First create a name for your VM, then change security type to standard, under size the Standard_B1ms should be selected. 
6. Move onto the Administrator account section. Under this section select password and follow the steps to create a username and password. This information must be written down or remembered as it will be needed during future steps.  
7. Under inbound port rules, select allow selected ports and SSH, HTTP and HTTPs should be seleected.
8. Under networking, delete NIC when VM is deleted should be selected.
9. Under Managements, please select to enable auto-shutdown and select a time that will work for you.
10. Review all selections and click create. 

## Google Cloud VM Setup
1. Log inot the Google portal.
2. Click on the select a porject button and then select new project button.
3. Name the project to your desire.
4. The location should be to what you need, for me it was AHI -GCP
5. Click the icon on the left side and click on VM Instances under compute engine.
6. Click on create instance.
7. Please name your VM. The following options should be selected: Under region and zone, us-cnetral1 Iowa, machine configuration should be E2 and e2small (2 VCPU), under Idendity and API access select compute engine deault service, under firewall allow HTTP and HTTPs.
8. Review the selections and click create. 

## Connecting MYSQL and Azure VM
* Before connecting the Azure VM to MYSQL Workbench, a few steps have to be completed through google shell and Azure.
1. Using Google Cloud shell, enter the command ssh username@IP address, for example my command was jward@74.235.194.68. Your IP address can be found under the overview section of your Azure VM.
2. You will then receieve a message asking if you want to continue, please type in yes. You will then have to retype the SSH message, but you can jsut copy and paste it
3. Your next message will ask for your login info, which you created during the creation of your VM.
4. Before doing any further steps to connect it, you will have to run the following three commands seperately, sudo apt-get update, sudo apt install mysql-client my sql-server and sudo mysql
5. Next you will create a user using the following command create user 'username'@'%' IDENTIFIED BY 'password';
6. Once the user is created, use the follwoing command to allow all access to this user, grant all priveleges on  *.* to 'username'@'%' with grant option;
7. Next return to the Azure VM page and select networking under settings. Here you will create an inbound port rule. Select add inbound port rule.
8. The only change that needs to be made is under the service drop down, please select MySQL and click add.
9. Please return to google shell where you will now type in the command sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf and scroll down to the bind-addres. This should be changed to 0.0.0.0.
10. Click ctrl+0 to save and type in the command /etc/init.d/mysql restart to restart it and log in to save the changes.
11. Now that those changes are complete, open MySQL Workbench and click on add connection. Under hosname, that is your IP address from Azure. Username and password are the ones created during the process of setting up your Azure VM. click test conenction to ensure your information was added correctly.
12. To create the database, please see the MYSQL folder or click the following link: https://github.com/jward6301/flask_4_databases_mysql_vm/blob/main/MYSQL/code.sql.


## Flask Integration
1. I utilzied code provided by professor Williams and code from a previous HW assignment to set up the flask templates.
2. I followed the instructions in the code provded from Professor Williams to create gitignore and env files to protect my informtion and all changes to the code that were needed were made.
3. You can view my code in the app.py file and under the tempaltes folder.
4. You can view what my flask app looked like under the screenshots folder. 


## Errors
* I ran into two errors while completing this homework assignment. 
* Since I created the Azure VM during class last week, I forgot the username I created for my VM and when conencting it using the ssh command, I ran into a few issues. Luckily I remembered my informaiton before having to delete the current VM and creating a new one.
* My other issue is on my flask app, on the data page my footer is in the middle of my third table. I am unsure how to fix this. A photo of this is in the screenshots folder, (https://github.com/jward6301/flask_4_databases_mysql_vm/blob/main/Screenshots/Screenshot%202023-10-11%20at%2010.59.32%20PM.png). 
* No issues were ran into creating both VMs as they were completed in class with Professor Williams.


