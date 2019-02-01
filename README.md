#Logs_Project.py

The file logs_project.py contains python code to query the news database and return lists of the three most popular articles, authors sorted by popularity, and dates on which more than 1% of requests resulted in errors. The code is written in Python 3.

The news database runs on a virtual machine. To the install the virtual machine, complete the following steps:
1. Install VirtualBox from virtualbox.org. Install the platform package for your operating system. 
2. Install Vagrant from vagrantup.com. Install the version for your operating system. 
3. Download the VM confirguration by forking and cloning the Github repository at  [https://github.com/udacity/fullstack-nanodegree-vm].
4. Using a terminal program such as GitBash, change directories to the directory containing the VM files. Inside you will find another directory called vagrant. Change directories to the vagrant directory.
5. From inside the vagrant subdirectory, run the command `vagrant up`
When this command is finished running, run `vagrant ssh` to log into the virtual machine.

Download the file newsdata.sql from this link: [https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip]

Put this file into the vagrant directory and run the command:
```psql -d news -f newsdata.sql```
This command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data. After running this command, you can connect to your database using the command:
```psql -d news```

The third query uses two views, errorcounts and datecounts. To create these views, after connecting to the news database run the following commands:

```create view datecounts as
select time::date, count(time::date) as count from log
group by time::date;
```

```create view errorcounts as
select time::date, count(time::date) as count from log
where status = '404 NOT FOUND'
group by time::date;```

After creating these views, use the command `\q`
to exit psql (but stay logged in to the virtual machine). Now you are ready to run the reporting tool! Do so using the following command:
```python logs_project.py```


