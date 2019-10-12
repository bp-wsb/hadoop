# Mapreduce with MRJob

1. Login to the cluster:
```console
    $ ssh sshuser@hdfs_name.azurehdinsight.net
```
where:<br/>
    sshuser - is default name created by the Azure<br/>
    hdfs_name - is the name provided in configuration step of cluster

2. Install mrjob:
```console
    $ sudo pip install mrjob
```
3. From local computer copy example_2 to local master fs tmp:
```console
    $ scp -r .\example_2\* sshuser@hdfs_name.azurehdinsight.net:/home/user/
```
where:<br/>
    sshuser - is default name created by the Azure<br/>
    hdfs_name - is the name provided in configuration step of cluster<br/>

4. Run script only local:
```console
    $ python hotel.py data.txt
```

Additional steps:
5. From cluster shell copy data.txt to hdfs:
```console
    $ hdfs dfs -copyFromLocal /tmp/example_2/data.txt /user/data.txt
```
6. Run script on cluster:
```console
    $ python hotel.py wasb:///data.txt -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar
```

