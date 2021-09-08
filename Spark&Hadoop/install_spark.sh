# Install scala
sudo apt install default-jdk scala git -y
java -version; javac -version; scala -version; git --version

# Install package
wget https://downloads.apache.org/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz

tar xvf spark-*
sudo mv spark-3.1.2-bin-hadoop3.2 /opt/spark

sudo nano .bashrc 

"
export SPARK_HOME=/opt/spark

export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

export PYSPARK_PYTHON=/usr/bin/python3

"
source ~/.bashrc 

sudo nano .profile 

"
export SPARK_HOME=/opt/spark

export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

export PYSPARK_PYTHON=/usr/bin/python3

"
source ~/.profile 

start-master.sh

# http://127.0.0.1:8080/
