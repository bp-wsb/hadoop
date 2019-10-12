# Mapreduce

1. From local shell copy example_1 to cluster:
```console
    $ scp -r .\example_1\* sshuser@hdfs_name.azurehdinsight.net:/home/user/
```
where:<br/>
    sshuser - is default name created by the Azure<br/>
    hdfs_name - is the name provided in configuration step of cluster

2. Login to the cluster:
```console
    $ ssh sshuser@hdfs_name.azurehdinsight.net
```
where:<br/>
    sshuser - is default name created by the Azure<br/>
    hdfs_name - is the name provided in configuration step of cluster<br/>

3. From cluster shell copy data.txt to hdfs:
```console
    $ hdfs dfs -copyFromLocal /home/user_name/data.txt /user_name/data.txt
```
where:<br/>
    user_name - is the name provided in configuration step of cluster

4. Run script:
```console
    $ hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -files MRatingCount.py,RRatingCount.py -mapper MRatingCount.py -reducer RRatingCount.py -input /data.txt -output /count
```
