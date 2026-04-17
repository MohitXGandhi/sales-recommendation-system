import os

print("🚀 Running Full Pipeline...\n")

os.system("python data/generate_data.py")
os.system("python descriptive_statistics.py")
os.system("python data_visualization.py")
os.system("python recommendation_system.py")

print("\n✅ PROJECT COMPLETED SUCCESSFULLY!")