from datetime import datetime
import os

# Get current date and time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Define absolute path for version.md
version_file_path = "/repo/version_control/docs/version.md"

# Ensure the docs directory exists
os.makedirs(os.path.dirname(version_file_path), exist_ok=True)

# Write to version.md
with open(version_file_path, "w") as file:
    file.write(f"Last updated: {current_time}\n")

print("version.md updated successfully!")
from datetime import datetime

# Get current date and time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Write to version.md
with open("../docs/version.md", "w") as file:
    file.write(f"Last updated: {current_time}\n")

print("version.md updated successfully!")

