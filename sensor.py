import random
import time

def generate_sensor_data():
    temperature = round(random.uniform(20.0, 30.0), 2)
    humidity = round(random.uniform(30.0, 70.0), 2)
    
    return {
        "temperature": temperature,
        "humidity": humidity
    }

def main():
    print("Starting IoT Sensor Simulation...\n")
    
    for _ in range(5):
        data = generate_sensor_data()
        print(f"Temperature: {data['temperature']}°C | Humidity: {data['humidity']}%")
        time.sleep(2)

if __name__ == "__main__":
    main()
