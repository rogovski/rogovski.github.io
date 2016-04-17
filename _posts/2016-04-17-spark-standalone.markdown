---
layout: post
title:  "Running a Spark Standalone Cluster"
date:   2016-04-17 13:14:00 -0500
categories: big data
description: "How to setup and configure"
---

start the master

```bash
./sbin/start-master.sh
```

start the slaves. limit each instance to 2 cores and 4G ram. create three instances.

```bash
SPARK_WORKER_INSTANCES=3 ./sbin/start-slave.sh spark://your-computer-name.local:7077 -c 2 -m 4G
```

load the python shell (interfacing with master)

```bash
./bin/pyspark --master spark://your-computer-name.local:7077
```

### sources
1. [spark xml](https://github.com/databricks/spark-xml)
2. [spark csv](https://github.com/databricks/spark-csv)
3. [pyspark java integration](http://stackoverflow.com/questions/27698111/how-to-add-third-party-java-jars-for-use-in-pyspark)
4. [standalone docs](http://spark.apache.org/docs/latest/spark-standalone.html)