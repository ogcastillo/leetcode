import os
from typing import List
import utilityFunctions.ConsoleLogger  as consoleLog
import utilityFunctions.FileLogger as fileLog


def merge(nums1: List[int], m: int, nums2: List[int], n: int):
    # log = consoleLogger().Logger get_logger()
    log = fileLog.FileLogger.get_logger()
    log.info(f"Executing script: {os.path.basename(__file__)}")
    auxNums: List[int]
    if n > 0:
        for i in range(m, m + n):
            log.info("i = "+ str(i) )
            if nums1[i] < nums2[i]:
                nums1.insert(i, nums2[i])
            else:
                nums1.insert(i, nums2[i+1])

if __name__ == '__main__':

    log = fileLog.FileLogger.get_logger()
    log.info(f"Executing script: {os.path.basename(__file__)}")
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    try:
        merge(nums1, m, nums2, n)
    except Exception as e:
        log.error(e,exc_info=True)
    print(nums1)



