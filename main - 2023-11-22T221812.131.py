import random
import time
import matplotlib.pyplot as plt

class TrafficCounter:
    def __init__(self):
        self.data = []

    def simulate_traffic(self):
        # Simulate random traffic counts (replace this with actual data retrieval)
        current_traffic_count = random.randint(50, 200)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # Store the data
        self.data.append({"timestamp": timestamp, "traffic_count": current_traffic_count})

    def plot_traffic_trends(self):
        timestamps = [entry["timestamp"] for entry in self.data]
        traffic_counts = [entry["traffic_count"] for entry in self.data]

        plt.figure(figsize=(10, 6))
        plt.plot(timestamps, traffic_counts, marker='o', linestyle='-')
        plt.title('Traffic Trends')
        plt.xlabel('Timestamp')
        plt.ylabel('Traffic Count')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

def main():
    traffic_counter = TrafficCounter()

    # Simulate traffic counts for a certain period
    for _ in range(10):
        traffic_counter.simulate_traffic()
        time.sleep(1)  # Simulate 1-second intervals

    # Display traffic trends
    traffic_counter.plot_traffic_trends()

if __name__ == "__main__":
    main()
