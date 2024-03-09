import os
import psutil
import time

MEMORY_LIMIT_GB = 30

while True:
    for process in psutil.process_iter(["pid", "name", "memory_info"]):
        ## if this process is Houdini
        if process.info["name"] == "houdinifx.exe":
            memory_usage_gb = process.info["memory_info"].rss / 1024**3
            print(f"Houdini Memory Usage: {memory_usage_gb:.2f} GB")

            ## Stop Houdini if memory usage go passed limit
            if memory_usage_gb > MEMORY_LIMIT_GB:
                try:
                    process.kill()
                    print("Houdini has been killed due to high memory usage.")
                except psutil.NoSuchProcess:
                    print("Process no longer exists")

    ## Sleep for 5 seconds
    time.sleep(2)