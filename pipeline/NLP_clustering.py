print("Clustering enriched logs...")

from collections import defaultdict

clusters = defaultdict(list)

with open("pipeline_logs/enriched_logs.txt") as infile:
    for line in infile:
        if "ERROR" in line:
            clusters["error"].append(line.strip())
        elif "WARNING" in line:
            clusters["warning"].append(line.strip())
        else:
            clusters["info"].append(line.strip())

with open("pipeline_logs/clusters.txt", "w") as f:
    for cluster, lines in clusters.items():
        f.write(f"## {cluster.upper()} LOGS\n")
        for entry in lines:
            f.write(entry + "\n")
        f.write("\n")