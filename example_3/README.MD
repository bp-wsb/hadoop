# PIG

1. From Azure portal copy cluster ssh address.
    Grupy zasobów  -> "name of the group" (ex bigdata) -> enter to the "HDInsight cluster" -> Properties -> Copy Secure Shell (SSH).

2. From local shell copy example_3 to cluster:
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

4. From cluster shell copy data.txt to hdfs:
```console
    $ hdfs dfs -copyFromLocal /home/sshuser/example_3/data.txt /user/data.txt
```
**where:**<br/>
* sshuser - is default name created by the Azure<br/>

5. Run script on cluster
```console
    $ pig -x mapreduce ./example_3/rating.pig
```
