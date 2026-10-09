# Exercise 7: Time-Series Processing at Scale

## Technology: InfluxDB

### 1. What is InfluxDB?

InfluxDB is a time-series database designed to store and query large volumes of time-stamped data. In comparison, Pandas is a Python library used to manipulate and analyze data, usually in memory.

### 2. Why is InfluxDB useful at scale?

InfluxDB is designed to ingest, store, and query large amounts of time-series data continuously. It is useful in production environments where data arrives frequently, such as measurements from sensors or monitoring systems.

A Pandas DataFrame is generally held in RAM, so very large datasets can use a lot of memory. Pandas is still useful for analysis, and techniques such as processing data in chunks can help with larger datasets. InfluxDB, on the other hand, is a database built for persistent time-series storage and efficient time-based queries.

InfluxDB also supports data-retention settings, which can help manage how long data is kept. Depending on the configuration, older or more detailed data can be downsampled or removed to manage storage.

### 3. Practical example: Temperature sensors

Imagine a company monitoring thousands of sensors that send temperature readings every second. Storing and querying all these readings in a single in-memory DataFrame could require a large amount of RAM. InfluxDB could store the readings persistently and help query measurements over specific time ranges, making it easier to monitor temperatures and identify patterns over time.

### 4. Sources

- [InfluxDB 3 Documentation](https://docs.influxdata.com/influxdb3/)
- [Pandas DataFrame Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
