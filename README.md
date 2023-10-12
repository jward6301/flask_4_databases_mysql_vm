# flask_4_databases_mysql_vm
HHA 504 Week 4B assignment

## Azure VM Setup
1. Log into the Azure portal using the following link:
2. Search for Virtual Machines.
3. Once that page is loaded, click on create and select the first option Azure Virtual Machine.
4. Subscription should be selected to Azure for students. You can create a new resource group or choose an existing one, I created a new one for this assignment
5. Under Instance details, only a few changes need to be made. First create a name for your VM, then change security type to standard, under size the Standard_B1ms should be selected. 
6. Move onto the Administrator account section. Under this section select password and follow the steps to create a username and password. This information must be written down or remembered as it will be needed during future steps.  
7. Under inbound port rules 

## Google Cloud VM Setup
1. Log inot the Google portal using the following link: 

## Connecting MYSQL and Azure VM
* Before connecting the Azure VM to MYSQL Workbench, a few steps have to be completed through google shell and Azure.
1. Using Google Cloud shell, enter the command ssh username@IP address, for example my command was jward@74.235.194.68. Your IP address can be found under the overview section of your Azure VM.
2. You will then receieve a message asking if you want to continue, please type in yes. You will then have to retype the SSH message, but you can jsut copy and paste it
3. Your next message will ask for your login info, which you created during the creation of your VM.
4. Before doing any further steps to connect it, you will have to run the following three commands seperately, sudo apt-get update, sudo apt install mysql-client my sql-server and sudo mysql
5. Next you will create a user using the following command create user 'username'@'%' IDENTIFIED BY 'password';
6. Once the user is created, use the follwoing command to allow all access to this user, grant all priveleges on  *.* to 'username'@'%' with grant option;
7. Next return to the Azure VM page and select networking under settings. Here you will create an inbound port rule. Select add inbound port rule.
8. 

Open MySQL Workbench and click on add connection. 





## Integrating the database with Flask
1. 



## Errors
* I ran into two errors while completing this homework assignment. 
* Since I created the Azure VM during class last week, I forgot the username I created for my VM and when conencting it using the ssh command, I ran into a few issues. Luckily I remembered my informaiton before having to delete the current VM and creating a new one.
* My other issue is on my flask app, on the data page my footer is in the middle of my third table. I am unsure how to fix this. A photo of this is in the screenshots folder, named 
* No issues were ran into creating both VMs as they were completed in class with Professor Williams.


