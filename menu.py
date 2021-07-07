import os
import getpass
while True:
    print("""
    #############################################
    press 1:  *Run python code inside (container)
    press 2:  *To configure webserver (container)
    Press 3:  *Integrate Lvm With Hadoop
    press 4:  *Hadoop options(*Client,NameNode,DataNode)
    press 5: AWS Options
    press 6: Docker options
    press 7:  Yum configure
    press 8: To setup lvm
    press 9: To resize the Lvm
    press 10: webserver(vm)
    press 11: exit
    #############################################
    """)
    ask=int(input("enter your choice"))
    
    if ask==1:
        os.system('systemctl start docker')
        os.system('docker pull centos:latest')
        os.system('docker create -it --name python_container centos')
        os.system('docker start python_container')
        os.system('docker exec -it python_container yum  install python3 -y')
        os.system('docker exec -it python_container yum install wget -y')
        path=input("Enter url of your code")
        os.system('docker exec -it python_container wget -O /py_code.py {}'.format(path))

    elif ask==2:	
        os.system('systemctl start docker')
        os.system('docker pull centos:latest')
        os.system('docker create -it --name webserver centos')
        os.system('docker start webserver')
        os.system('docker exec -it webserver install httpd -y')
        os.system('docker exec -it webserver yum install wget')
        os.system('docker exec -it webserver yum install net-tools')
        path=input("Enter url of your code")
        os.system('docker exec -it webserver wget -O /var/www/html/index.html {}'.format(path))
        os.system('docker exec -it webserver /usr/sbin/httpd')

    elif ask==3:
        ask2=int(input("How Many Nodes You Have :- "))
        hyt=[]	
        pyt=[]
        for k in range(0,ask2):
            if k==0:
                ask31=input("Enter the Ip of NameNode :- ")
                hyt.append(ask31)
                passs=getpass.getpass("enter your password")
                pyt.append(passs)
		
            elif k==1:
                ask31=input("Enter the Ip of Client :- ")
                hyt.append(ask31)
                passs=getpass.getpass("enter your password")
                pyt.append(passs)
            elif k>1:
                ask31=input("Enter the Ip of DataNode :- ")
                hyt.append(ask31)
                passs=getpass.getpass("enter your password")
                pyt.append(passs)
                   
        for i in range(0,ask2):		
            if i==0:
                ask31=hyt[i]
                passs=pyt[i]
                a = 'ssh {} yum install sshpass -y'.format(ask31)
                os.system(a)
                a = 'ssh {} pip3 install gdown'.format(ask31)
                os.system(a)
                a="""sshpass -p {} ssh {} wget -O /root/hadoop-1.2.1-1.x86_64.rpm https://drive.google.com/file/d/1_qobuHO8NjRlxQG3hHw1KHei3XdOeIY5/view?usp=sharing""".format(passs,ask31)
                os.system(a)
                a="""sshpass -p {} ssh {} wget -O /root/jdk-8u171-linux-x64.rpm https://drive.google.com/file/d/15hZtVD6BO3op_xZot2Xpf101IWXiQp0i/view?usp=sharing""".format(passs,ask31)
                os.system(a)
                a = 'sshpass -p {} ssh {} rpm -ivh /root/jdk-8u171-linux-x64.rpm'.format(passs,ask31)
                print(os.system(a))
                a='sshpass -p {} ssh {} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force'.format(passs,ask31)
                print(os.system(a))	
                a="""sshpass -p {} ssh {} wget -O /etc/hadoop/core-site.xml https://drive.google.com/file/d/18bO0JTz--msq77UAqlBL5adrMe5XYYF8/view?usp=sharing""".format(passs,ask31)
                os.system(a)
                a="""sshpass -p {} ssh {} wget -O /etc/hadoop/hdfs-site.xml https://drive.google.com/file/d/1NTLgxJpfUO6RlUv1EL-F-k3vev1mZ9gJ/view?usp=sharing""".format(passs,ask31)				
                os.system(a)
                a="""sshpass -p {} ssh {} systemctl stop firewalld""".format(passs,ask31)
                os.system(a)
                a='sshpass -p {} ssh {} systemctl disable firewalld'.format(passs,ask31)
                os.system(a)		
                a='sshpass -p {} ssh {} hadoop namenode -format'.format(passs,ask31)
                os.system(a)
                a='sshpass -p {} ssh {} hadoop-daemon.sh start namenode'.format(passs,ask31)
                os.system(a)
            elif i==1:
                ask3=hyt[i]
                passs=pyt[i]
                a="""sshpass -p {} ssh {} wget -O /root/hadoop-1.2.1-1.x86_64.rpm https://drive.google.com/file/d/1_qobuHO8NjRlxQG3hHw1KHei3XdOeIY5/view?usp=sharing""".format(passs,ask3)
                os.system(a)
                a="""sshpass -p {} ssh {} wget -O /root/jdk-8u171-linux-x64.rpm https://drive.google.com/file/d/15hZtVD6BO3op_xZot2Xpf101IWXiQp0i/view?usp=sharing""".format(passs,ask3)
                os.system(a)
                a = 'sshpass -p {} ssh {} rpm -ivh /root/jdk-8u171-linux-x64.rpm'.format(passs,ask3)
                print(os.system(a))
                a='sshpass -p {} ssh {} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force'.format(passs,ask3)
                print(os.system(a))	
                a="""wget -O /core-site.xml https://drive.google.com/file/d/18bO0JTz--msq77UAqlBL5adrMe5XYYF8/view?usp=sharing"""
                os.system(a)
                with open('/core-site.xml') as f:
                    newText=f.read().replace('0.0.0.0', ask31)
                with open('/core-site.xml', "w") as f:
                    f.write(newText)
                os.system('sshpass -p {} scp /core-site.xml {}:/etc/hadoop/core-site.xml'.format(passs,ask3))

            elif i>1:
                ask3=hyt[i]
                passs=pyt[i]
                a="""sshpass -p {} ssh {} wget -O /root/hadoop-1.2.1-1.x86_64.rpm https://drive.google.com/file/d/1_qobuHO8NjRlxQG3hHw1KHei3XdOeIY5/view?usp=sharing""".format(passs,ask3)
                os.system(a)
                a="""sshpass -p {} ssh {} wget -O /root/jdk-8u171-linux-x64.rpm https://drive.google.com/file/d/15hZtVD6BO3op_xZot2Xpf101IWXiQp0i/view?usp=sharing""".format(passs,ask3)
                os.system(a)			
                a = 'sshpass -p {} ssh {} rpm -ivh /root/jdk-8u171-linux-x64.rpm'.format(passs,ask3)
                print(os.system(a))
                a='sshpass -p {} ssh {} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force'.format(passs,ask3)
                print(os.system(a))	
                a="""wget -O /core-site.xml https://drive.google.com/file/d/18bO0JTz--msq77UAqlBL5adrMe5XYYF8/view?usp=sharing"""
                os.system(a)
                a="""sshpass -p {} ssh {} wget -O /etc/hadoop/hdfs-site.xml https://drive.google.com/file/d/1NTLgxJpfUO6RlUv1EL-F-k3vev1mZ9gJ/view?usp=sharing""".format(passs,ask3)				
                os.system(a)
                with open('/core-site.xml') as f:
                   newText=f.read().replace('0.0.0.0', ask31)
                with open('/core-site.xml', "w") as f:
                   f.write(newText)
                os.system('sshpass -p {} scp /core-site.xml {}:/etc/hadoop/core-site.xml'.format(passs,ask3))
                os.system('sshpass -p {} ssh {} systemctl stop firewalld'.format(passs,ask3))
                os.system('sshpass -p {} ssh {} systemctl disable firewalld'.format(passs,ask3))		
                os.system('sshpass -p {} ssh {} hadoop-daemon.sh start datanode'.format(passs,ask3))
    
    elif ask==4:
        
        print("""
		press 1.  (Client)to upload the file on cluster
		press 2.  (Client)to create empty file on cluster
		press 3.  (Client)to list the files and folders in cluster
		press 4.  (Client)to create folder on cluster
		press 5.  (Client)to read the data inside file
		press 6.  (Client)to remove the file from the cluster
		press 7.  (Client)to remove the folder from the cluster 	
		press 8. (NameNode)to start namenode service 
		press 9. (NameNode)to stop namenode service
		press 10. (NameNode)to format namenode 
		press 11. (Any)to check cluster report 
		press 12. (DataNode)to stop datanode service
		press 13. (DataNode)to start datanode service 
    """)

        ask = int(input("enter your choice :- "))	
        if ask==1:
            ask1=input("full path of source file :- ")
            ask2=input("full path of destination :- ")
            a='hadoop fs -put {} {}'.format(ask1,ask2)
            os.system(a)
        if ask==2:
            ask2=input("path where you want to create file :- ")
            a='hadoop fs -touchz {}'.format(ask2)
            os.system(a)
        if ask==3:
            ask2=input("in which location you want to list :- ")
            a='hadoop fs -ls {}'.format(ask2)
            os.system(a)
        if ask==4:
            ask2=input("path where you want to create folder :- ")
            a='hadoop fs -mkdir {}'.format(ask2)
            os.system(a)
        if ask==5:
            ask2=input("file path you want to read :- ")
            a='hadoop fs -cat {}'.format(ask2)
            os.system(a)
        if ask==6:
            ask1=input("File Path :- ")
            a='hadoop fs -rm {}'.format(ask1)
            os.system(a)
        if ask==7:
            ask1=input("Folder Path :- ")
            a='hadoop fs -rmr {}'.format(ask1)
            os.system(a)
        if ask==8:
            a='hadoop-daemon.sh stop namenode'
            os.system(a)
        if ask==9:
            a='hadoop-daemon.sh start namenode'
            os.system(a)
        if ask==10:
            a='hadoop namenode -format'
            os.system(a)
        if ask==11:
            os.system('hadoop dfsadmin -report')
        if ask==12:
            os.system('hadoop-daemon.sh stop datanode')	
        if ask==13:
           os.system('hadoop-daemon.sh start datanode')

    elif ask==5:
        print("""
    press 1. to Install AwsCli
    press 2. to Use EC2 Service
    press 3. to Create S3 Bucket
    press 4. to Create Cloud Front
    press 5. to Create security groups
    press 6. to Create key-pair
    press 7. to Create EBS
    press 8. to attach the EBS 
    """)
        ask1 = int(input("enter your option :- "))
        if ask1==1:
            os.system("""curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" """)
            os.system('unzip awscliv2.zip')
            os.system('sudo ./aws/install -i /usr/local/aws-cli -b /usr/local/bin')
			
        elif ask1==2:
            name1=input("enter the key name :- ")
            a='aws ec2 create-key-pair --key-name {} --query KeyMaterial > finalkey.pem --output text > {}.pem'.format(name1)
            os.system(a)
            key="{}.pem".format(name)
            name=input("enter the security group name :- ")
            a="""aws ec2 create-security-group --group-name {} --description "aws cli task security group" --output text > security.text""".format(name)
            os.system(a)
            a = """aws ec2 authorize-security-group-ingress  --group-name {} --cidr 0.0.0.0/0 --protocol all""".format(name)
            os.system(a)
            os.system('sleep 2s')
            file1 =open("security.text","r")
            variable1 = file1.read()
            a="""aws ec2 run-instances --image-id ami-03cfb5e1fb4fac428 --instance-type t2.micro --key-name {} --subnet-id subnet-8e2124e6 --security-group-ids {} --output text""".format(name1,variable1)
            os.system(a)
        elif ask1==5:
            name=input("enter the security group name :- ")
            a="""aws ec2 create-security-group --group-name {} --description "aws cli task security group" --output text > security.text""".format(name)
            os.system(a)
            a = """aws ec2 authorize-security-group-ingress  --group-name {} --cidr 0.0.0.0/0 --protocol all""".format(name)
            os.system(a)
        elif ask1==6:	
            name=input("enter the key name :- ")
            a='aws ec2 create-key-pair --key-name {} --query KeyMaterial > finalkey.pem --output text > {}.pem'.format(name)
            os.system(a)
        elif ask1==7:
            size=int(input("enter the size of the volume"))
            az=input("enter the AZ of the volume")
            a = """aws ec2 create-volume --availability-zone {} --size {} --query VolumeId --output text""".format(az,size)
        elif ask1==8:
            device=input("enter the device name :- ")
            instance = input("enter the instance id :-")
            volume = input("enter the volume id :- ")
            a = """aws ec2 attach-volume --device {} --instance-id {} --volume-id {}""".format(device,instance,volume)
            os.system(a)

    elif ask==6:
        print("""
	press 1.  to install docker
	press 2.  to list docker images
	press 3.  to start docker service
	press 4.  to stop docker service
	press 5.  to download docker images
	press 6.  to search for docker images in dockerhub
	press 7.  to launch docker container
	press 8.  to start the container
	press 9.  to stop the container
	press 10. to attach to the container
	press 11. to list running containers only
	press 12. to list all containers
	press 13. to remove the docker image
	press 14. to info of the docker
	press 15. to Low Level Information of docker objects
	press 16. to remove specific container
	press 17. to remove all the containers
	press 18. to check logs of container """)

        ask = int(input("enter your choice :- "))	
        if ask==1:
            a='yum install docker-ce --nobest'
            os.system(a)
        if ask==2:
            os.system('docker images')
        if ask==3:
            os.system('systemctl start docker')
        if ask==4:
            os.system('systemctl stop docker')
        if ask==5:
            ask1=input("enter the image name :- ")
            a='docker pull {}'.format(ask1)
            os.system(a)
        if ask==6:
            ask1=input("enter the image name :- ")
            a='docker search {}'.format(ask1)
            os.system(a)
        if ask==7:
            name = input("enter the name of container :- ")
            image = input("enter the image name which you want to use :- ")
            a='docker run -it --name {} {}'.format(name,image)
            os.system(a)
        if ask==8:
            name = input("enter the name of container :- ")
            a = 'docker start {}'.format(name)
            os.system(a)
        if ask==9:
            name = input("enter the name of container :- ")
            a = 'docker stop {}'.format(name)
            os.system(a)
        if ask==10:
            name = input("enter the name of container :- ")
            a = 'docker exec -it {} /bin/bash'.format(name)
            os.system(a)
        if ask==11:
            a='docker ps'
            os.system(a)
        if ask==12:
            a='docker ps -a'
            os.system(a)
        if ask==13:
            image = input("enter image name :- ")
            a='docker rmi {}'.format(image)
            os.system(a)
        if ask==14:
            os.system('docker info')	
        if ask==15:	
            name = input("enter the name of container :- ")
            a='docker inspect {}'.format(name)
            os.system()	
        if ask==16:
            name = input("enter the name of container :- ")
            a= 'docker rm {}'.format(name)
            os.system(a)
        if ask==17:
            a= "docker rm $(docker ps -a )"
            os.system(a)
        if ask==18:
            name = input("enter the name of container :- ")
            a= 'docker logs {}'.format(name)
            os.system(a)
    
    elif ask==7:
        print("""
	press 1. rhel8 disk
	Press 2. docker""")
        yum=int(input("enter your choice :- "))
        if yum==1:
            a="""[dvd1]
	baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS/
	gpgcheck=0
	[dvd2]
	baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream/
	gpgcheck=0
	"""
            ip = input("enter the ip :- ")
            file1 = open("/harsh.repo","w")
            file1.write(a)
            file1.close()
            os.system('scp /harsh.repo {}:/etc/yum.repos.d/'.format(ip))
        elif yum==2:
            ip = input("enter the ip :- ")
            a="""[docker]
	baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/
	gpgcheck=0
	"""
            file1 = open("/docker.repo","w")
            file1.write(a)
            file1.close()
            os.system('scp /docker.repo {}:/etc/yum.repos.d/'.format(ip))

    
    elif ask==8:
        count=int(input("how many devices you have for the vg :- "))
        xg=[]
        d = """"""
        for i in range(0,count):
            print(os.system('fdisk -l'))
            device=input("enter the device{} name :- ".format(i+1))
            xg.append(device)
            d=d+' '+xg[i]
            a = 'pvcreate {}'.format(device)
            print(os.system(a))

        name = input("enter you vg name :- ")
        c = 'vgcreate {} '+d
        c = c.format(name)
        print(os.system(c))
        partname=input("enter the partition name :- ")
        size1 = input("enter the size you want :- ")
        d = 'lvcreate {} --size {} --name {} -y'.format(name,size1,partname)
        print(os.system(d))
        e='mkfs.ext4 /dev/'+name+'/'+partname
        print(os.system(e))
        mo = input("enter the folderpath to which you want to mount :- ")
        tomy = 'mkdir '+mo
        os.system(tomy)
        gght='mount /dev/'+name+'/'+partname+' '+mo
        os.system(gght)
    
    elif ask==9:

        print("""
		press 1: to increase
		press 2: to decrease""")
        ask22=int(input("enter your choice :- "))	
        if ask22==1:
            ask23=input("enter the lvm name which you want to increase :- ")
            ask24=input("enter the size you want to increase :- ")
            a='lvextend --resizefs --size +{} {}'.format(ask24,ask23)			
            os.system(a)
        elif ask22==2:
            ask23=input("enter the lvm name which you want to decrease :- ")
            ask24=input("enter the final size of partition :- ")
            a='lvreduce --resizefs --size {} {} -y'.format(ask24,ask23)			
            os.system(a)

    elif ask==10:
        os.system("yum install httpd -y")
        os.system("wget -O /var/www/html/index.html https://drive.google.com/file/d/1R4UFlMnYbaatl9X0PTIM90PKGqNTzTW4/view?usp=sharing")
        os.system("systemctl start httpd")       

    elif ask==11:
        break


