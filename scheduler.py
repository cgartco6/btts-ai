import schedule, time
from main import run_pipeline

schedule.every(2).minutes.do(run_pipeline)

while True:
    schedule.run_pending()
    time.sleep(1)
