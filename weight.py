import csv
import pandas as pd
import statistics

df = pd.read_csv("height-weight.csv")
weight_list = df["Weight(Pounds)"].to_list()

weight_mean = statistics.mean(weight_list)
weight_median = statistics.median(weight_list)
weight_mode = statistics.mode(weight_list)
weight_stddev = statistics.stdev(weight_list)

weight_first_stddev_start, weight_first_stddev_end = weight_mean-weight_stddev, weight_mean+weight_stddev
weight_second_stddev_start, weight_second_stddev_end = weight_mean-(2*weight_stddev), weight_mean+(2*weight_stddev)
weight_third_stddev_start, weight_third_stddev_end = weight_mean-(3*weight_stddev), weight_mean+(3*weight_stddev)

weight_list_of_data_within_1_stddev = [result for result in weight_list if result > weight_first_stddev_start and result < weight_first_stddev_end]
weight_list_of_data_within_2_stddev = [result for result in weight_list if result > weight_second_stddev_start and result < weight_second_stddev_end]
weight_list_of_data_within_3_stddev = [result for result in weight_list if result > weight_third_stddev_start and result < weight_third_stddev_end]

print("{}% of data lies within 1 std_dev".format(len(weight_list_of_data_within_1_stddev)*100.0/len(weight_list)))
print("{}% of data lies within 2 std_dev".format(len(weight_list_of_data_within_2_stddev)*100.0/len(weight_list)))
print("{}% of data lies within 3 std_dev".format(len(weight_list_of_data_within_3_stddev)*100.0/len(weight_list)))