# Mapreduce

1. From Azure portal copy cluster ssh address.
    Grupy zasobów  -> "name of the group" (ex bigdata) -> enter to the "HDInsight cluster" -> Properties -> Copy Secure Shell (SSH).

2. From local shell copy example_1 to cluster:
```console
    $ scp -r ./example_1/ ssh_address:/home/sshuser/
```
**where:**<br/>
* sshuser - is default name created by the Azure<br/>
* ssh_address - address from the first step.

3. Login to the cluster:
```console
    $ ssh ssh_address
```
**where:**<br/>
* ssh_address - address from the first step.

4. From cluster shell copy data.txt to hdfs:
```console
    $ hdfs dfs -copyFromLocal /home/sshuser/example_1/data.txt /user/data.txt
```
**where:**<br/>
* sshuser - is default name created by the Azure<br/>

5. Run script:
```console
    $ hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -files ./example_1/MRatingCount.py,./example_1/RRatingCount.py -mapper MRatingCount.py -reducer RRatingCount.py -input /user/data.txt -output /user/count
```

6. When the work is done check result:
```console
    $ hdfs dfs -text /user/count/part-00000
```
