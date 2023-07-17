import schedule
import time
from jobs import checkHouse

if __name__ == "__main__":
    schedule.every(10).minutes.do(checkHouse.job)
    while True:
        schedule.run_pending()
        time.sleep(1)
# schedule.every(1).
# seconds.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)
# schedule.every().minute.at(":17").do(job)

# def job_with_argument(name):
#     print(f"I am {name}")
#
#
# schedule.every(10).seconds.do(job_with_argument, name="Peter")
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
