#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import rospy
from beginner_tutorials.srv import *

def call_sort_numbers_service():
    rospy.wait_for_service('sort_numbers')
    try:
        sort_numbers = rospy.ServiceProxy('sort_numbers', SortNumbers)

        # 接受命令行参数或者直接使用默认值
        if len(sys.argv) > 1:
            num = [float(arg) for arg in sys.argv[1:]]
        else:
            num = [5, 7, 1, 4, 2]

        print("Sending numbers: ", num)

        request = SortNumbersRequest()
        request.numbers = num

        #调用服务
        response = sort_numbers(request)
        #打印结果
        print("response: ",response.sorted_numbers)
        
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

if __name__ == "__main__":
    call_sort_numbers_service()
