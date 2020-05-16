# Uber-Ride-Data-Processing-with-Apache-Spark

## Table of Content
-	Objective
- Requirements
- Architecture
-	Data Description
-	Steps Followed
-	Results
-	Conclusion

## Objective
Spark provides a distributed in memory computation for larger dataset. Spark performs very fast joins and aggregation even with millions of rows, which otherwise is a slow process if working with traditional tools. Therefore, in this analysis I have used spark for processing 14 million uber-rides-data. The SparkSQL module within Spark architecture is used, which provides an API for SQL like queries. 

## Requirements
Please go through this blog which I wrote in order to setup the environment - 

## Architecture
![Untitled Diagram (2)](https://user-images.githubusercontent.com/32847030/82127761-14489600-9784-11ea-929d-d8d7276c2a1c.jpg)


## Data Description
The data contains 14 million rows that represents uber pickups within the New York city from April to September 2015. Additionaly, the look up files is used along with data from 2015 in order to perfrom joins. The data was collected by FiveThirtyEigher and made publically available here https://github.com/fivethirtyeight/uber-tlc-foil-response  

## Steps Followed
1.	Downlaoding data and setting-up spark on Linux
2.  Reading data into SparkSQL
3.	Understanding Schema 
4.	Performed appropriate Joins 
5.	Time and Date conversion
6.	Performed aggregation queries 

## Result
-	In year 2015, Manhattan had the greatest number of pickups (10 million) followed by Brooklyn (2.3 million).
-	In year 2015, highest volume of uber requests were between 6PM-11PM.
-	In 2015, the trend was – as the months moved ahead, the number of pickups rises. Which reflects that people tend to go out more in summer with the greatest number of pickups in June (2015).

## Conclusion
The analysis shows that spark provide fast results on aggregation and joined performed on large files with millions of rows. Although there can be many ways the data can be analyzed based on the business requirement, but the objective of this analysis is to experience working with spark on very large datasets. 

------   
     
![1](https://user-images.githubusercontent.com/32847030/82128059-0267f280-9786-11ea-923f-adfe44be8bdd.JPG)
![2](https://user-images.githubusercontent.com/32847030/82128060-0267f280-9786-11ea-99cb-a190728463ff.JPG)
![3](https://user-images.githubusercontent.com/32847030/82128061-03008900-9786-11ea-9040-5c6723b57882.JPG)

