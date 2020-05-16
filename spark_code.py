from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
from pyspark.sql.functions import split, col, to_date, to_timestamp, hour, month,weekofyear


conf = SparkConf()
sc = SparkContext(conf=conf)
sqlcontext = SQLContext(sc)


class uber_data_loading():
	
	def __init__(self, sqlcontext, filename,lookup):
		self.filename = 'uber.csv'
		self.lookup = "lookup.csv"
		pass
				
	def reading(self):
		self.df = sqlcontext.read.format("csv").option("header","true").option("inferSchema","true").load(self.filename)
		self.lookup = sqlcontext.read.format("csv").option("header","true").option("inferSchema","true").load(self.lookup)
		return self.df, self.lookup
		
	def joins(self):
		df, lookup =  self.reading()
		df = df.join(lookup,on=['locationID'],how='inner')
		return df
	
	def time_conversion(self):
		df = self.joins()
		df.withColumn("date_time",(to_timestamp(col('Pickup_date'),"yyyy-MM-dd'T'hh:mm:ss")))
		return df

		
class uber_data_processing(): 

	def __init__(self, sqlcontext, data_frame):
		self.df = data_frame
	
	def area_pickup(self):
		area = self.df.groupBy("Borough").count().orderBy('count',ascending=False)
		return area
	
	def time_pickup(self):
		times = self.df.groupBy(hour('pickup_date')).count().orderBy('count',ascending=False)
		return times
		
	def month_pickup(self):
		months = self.df.groupBy(month('pickup_date')).count().orderBy('count',ascending=False)
		return months
		
	def views(self):
		self.area, self.times, self.months = self.area_pickup(), self.time_pickup(), self.month_pickup()
		print(self.area.show())
		print(self.times.show())
		print(self.months.show())

	
	
if __name__ == '__main__':
	
	obj1 = uber_data_loading(sqlcontext,'name1','name2')
	data_frame = obj1.time_conversion()

	obj2 = uber_data_processing(sqlcontext,data_frame)
	#obj2.area_pickup()
	#obj2.time_pickup()
	#obj2.month_pickup()
	obj2.views()






	
	

	
