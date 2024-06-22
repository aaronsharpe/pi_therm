from thermometer import read_temp
import time
import datetime

if __name__ == '__main__':
    try:
        while True:
            _, temp_f = read_temp()
            current_time = datetime.datetime.fromtimestamp(time.time())
            readable_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
            print(f'{readable_time}; Temperature: {temp_f:.1f}°F')
            time.sleep(30)  
    except KeyboardInterrupt:
        pass