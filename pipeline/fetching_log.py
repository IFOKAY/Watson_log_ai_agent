print("Fetching logs from OpenShift pods...")

# Dummy logic for placeholder
import os
os.makedirs("pipeline_logs", exist_ok=True)
with open("pipeline_logs/fetched_logs.txt", "w") as f:
    f.write("""
[INFO] App started
[WARNING] Disk usage high
[ERROR] Connection to DB failed
[INFO] Retrying connection
[ERROR] Timeout occurred
""")

# NER_enrich.py
print("Performing NER enrichment...")

with open("pipeline_logs/cleaned_logs.txt") as infile, open("pipeline_logs/enriched_logs.txt", "w") as outfile:
    for line in infile:
        if "error" in line.lower():
            outfile.write(f"{line} | TYPE: ERROR\n")
        elif "warn" in line.lower():
            outfile.write(f"{line} | TYPE: WARNING\n")
        else:
            outfile.write(f"{line} | TYPE: INFO\n")