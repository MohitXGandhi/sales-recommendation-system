import subprocess
import sys

print(" Running Full Pipeline...\n")

subprocess.run([sys.executable, "data/generate_data.py"], check=True)
subprocess.run([sys.executable, "descriptive_statistics.py"], check=True)
subprocess.run([sys.executable, "data_visualization.py"], check=True)
subprocess.run([sys.executable, "recommendation_system.py"], check=True)

print("\n PROJECT COMPLETED SUCCESSFULLY!")