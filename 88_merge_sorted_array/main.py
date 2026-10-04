import os
import sys
import time
from typing import List

# Add the root directory to the path so we can import utilityFunctions
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# import utilityFunctions.ConsoleLogger  as consoleLog
import utilityFunctions.FileLogger as fileLog


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    # log = consoleLogger().Logger get_logger()
    log = fileLog.FileLogger.get_logger()
    log.info(f"Executing script: {os.path.basename(__file__)}")
    auxArr = nums1
    log.info(f" auxArr: {auxArr}")
    index = 0
    while index < len(auxArr):
        log.info('i = ' + str(index))
        if index < len(nums2):
            if auxArr[index] < nums2[index]:
                auxArr.insert(index + 1, nums2[index])
                auxArr.sort()
        index += 1
        log.info(f" auxArr: {auxArr}")
    log.info(f" auxArr: {nums1}")
    return auxArr

if __name__ == '__main__':
    initTime = time.time()
    log = fileLog.FileLogger.get_logger()
    log.info("init")
    log.info(f"Executing script: {os.path.basename(__file__)}")
    nums1 = [1, 2, 3, 0, 0, 0]
    log.info(f" array 1: {nums1}")
    m = 3
    log.info(f" m= {m}")
    nums2 = [2, 5, 6]
    log.info(f" array 2: {nums2}")
    n = 3
    log.info(f" n= {n}")
    nums1 = merge(nums1, m, nums2, n)
    auxArr = []
    for i in nums1:
            auxArr.append(0)
    for i in nums1:
        if i != 0:
            auxArr.append(i)
    log.info(f" result arr: {auxArr}")
    try:
        log.info(f"calling merge function")
        print(auxArr)
    except Exception as e:
        log.error(e,exc_info=True)
    endTime = time.time()
    log.info("end")
    log.info(f"total time taken: {endTime - initTime:2f} seconds")