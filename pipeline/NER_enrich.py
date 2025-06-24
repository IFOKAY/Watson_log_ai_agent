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