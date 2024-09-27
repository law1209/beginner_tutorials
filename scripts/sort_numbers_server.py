#!/usr/bin/python3

from beginner_tutorials.srv import *
import rospy

def handle_sort_numbers(request):
    # 排序输入数组
    sorted_numbers = sorted(request.numbers)
    
    # 创建响应
    response = SortNumbersResponse()
    response.sorted_numbers = sorted_numbers
    print("Sorted numbers: ", sorted_numbers)
    
    return response

def sort_numbers_server():
    rospy.init_node('sort_numbers_server')
    s = rospy.Service('sort_numbers', SortNumbers, handle_sort_numbers)
    rospy.loginfo("Sort Numbers service is ready.")
    rospy.spin()

if __name__ == "__main__":
    sort_numbers_server()