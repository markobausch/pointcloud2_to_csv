#!/usr/bin/env python
from __future__ import print_function

import csv
import sys

import rospy
import sensor_msgs.point_cloud2
from sensor_msgs.msg import PointCloud2

csv_writer = csv.writer(
    open(sys.argv[2], 'wb'), delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
csv_writer.writerow(['seq', 'x', 'y', 'z', 'i'])


def point_cloud(msg):
    print(msg.header.seq)
    for point in sensor_msgs.point_cloud2.read_points(msg, skip_nans=True):
        pt_x = point[0]
        pt_y = point[1]
        pt_z = point[2]
        pt_i = point[3]
        csv_writer.writerow([msg.header.seq, pt_x, pt_y, pt_z, pt_i])


def main():
    rospy.Subscriber(sys.argv[1], PointCloud2, point_cloud)

    rospy.spin()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage ./pointcloud2_to_csv.py <topic> <output.csv>")
        exit(1)

    print("Saving '{}' in '{}' ".format(sys.argv[1], sys.argv[2]))
    rospy.init_node("pointcloud2_to_csv")
    main()
