# Overview
This project provides command line tool to query nearest food trucks.

# Environment
The command line tool depends on Python3 and Makefile

# Tutorial
### Install dependencies
```
make dependency
```

### Get nearest food trucks
```
script/get_nearest_trucks.py -a [LATITUDE] -g [LONGITUDE] -n [NUMBER_OF_RESULTS]
```
For example, to get 5 nearest food trucks for latitude:longitude 37.76201920035647,-122.42730642251331:
```
script/get_nearest_trucks.py -a 37.76201920035647 -g -122.42730642251331 -n 5
```
The results are in ascending order of distance.

### Update csv file of food trucks
```
make update_csv
```

### Test
```
make test
```

### Clean temporary data
```
make clean
```

# Design
The algorithm is to simply calculate distances to all food trucks, sort them by distance, and then pick up the top K ones.
Considering the number of records are currently less than 500, this simple solution should be adequeate.
If the number of records increases dramatically in the future, some more advanced algorithms may be used, such as heap search, or KD tree.

# Future work
### Use map API to get route distance
Calculating distance purely by coordinates may not be accurate.
It would be more useful to get route distance based on different travel modes by using map APIs (e.g. google map or bing map).

### Deploy serverless solution in Cloud
The code can be deployed into Cloud using serverless solution.
Take AWS Cloud as example, we can use the following resources:
- S3 object to store CSV file of trucks information
- Cloudwatch event to trigger a Lambda function to periodically update the CSV file in S3
- A second Lambda function to run the python code script/get_nearest_trucks.py
- API gateasy to provide Web API query interface for get_nearest_trucks Lambda function
- Static website files (html and javascript) in S3 bucket to host web interface
