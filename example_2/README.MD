# Mapreduce with MRJob

1. From Azure portal copy cluster ssh address.
    Grupy zasobów  -> "name of the group" (ex bigdata) -> enter to the "HDInsight cluster" -> Properties -> Copy Secure Shell (SSH).

2. From local shell copy example_2 to cluster:
```console
    $ scp -r ./example_2/ ssh_address:/home/sshuser/
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

4. Install mrjob:
```console
    $ sudo pip install mrjob
```

5. Run script only local:
```console
    $ python ./example_2/ratingcount.py data.txt
```

## Additional steps:
6. From cluster shell copy data.txt to hdfs:
```console
    $ hdfs dfs -copyFromLocal ./example_2/data.txt /user/data.txt
```
7. Run script on cluster:
```console
    $ python ./example_2/ratingcount.py wasb:///data.txt -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar
```

