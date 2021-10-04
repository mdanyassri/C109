import csv
import pandas as pd 
import statistics 

df = pd.read_csv("height-weight.csv")
height_list = df["Height(Inches)"].to_list()

height_mean = statistics.mean(height_list)
height_median = statistics.median(height_list)
height_mode = statistics.mode(height_list)
height_stddev = statistics.stdev(height_list)

print("mean,median and mode of height is {},{}, and {} respectively".format(height_mean, height_median, height_mode))

height_first_stddev_start, height_first_stddev_end = height_mean-height_stddev, height_mean+height_stddev 
height_second_stddev_start, height_second_stddev_end = height_mean-(2*height_stddev), height_mean+(2*height_stddev)
height_third_stddev_start, height_third_stddev_end = height_mean-(3*height_stddev), height_mean+(3*height_stddev)

height_list_of_data_within_1_stddev = [result for result in height_list if result > height_first_stddev_start and result < height_first_stddev_end]
height_list_of_data_within_2_stddev = [result for result in height_list if result > height_second_stddev_start and result < height_second_stddev_end]
height_list_of_data_within_3_stddev = [result for result in height_list if result > height_third_stddev_start and result < height_third_stddev_end]

print("{}% of data lies within 1 std_dev".format(len(height_list_of_data_within_1_stddev)*100.0/len(height_list)))
print("{}% of data lies within 2 std_dev".format(len(height_list_of_data_within_2_stddev)*100.0/len(height_list)))
print("{}% of data lies within 3 std_dev".format(len(height_list_of_data_within_3_stddev)*100.0/len(height_list)))