from thermometer import read_temp
import time
import datetime

if __name__ == '__main__':
    try:
        while True:
            temp_f = None
            while temp_f is None:
                try:
                    _, temp_f = read_temp()
                except Exception as e:
                    print(f'Error reading temperature: {e}')
                    time.sleep(1)

            current_time = datetime.datetime.fromtimestamp(time.time())
            readable_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
            print(f'{readable_time}; Temperature: {temp_f:.2f}°F')
            time.sleep(30)  
    except KeyboardInterrupt:
        pass