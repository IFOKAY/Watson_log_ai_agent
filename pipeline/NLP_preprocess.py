print("Cleaning and tokenizing logs...")

with open("pipeline_logs/fetched_logs.txt") as infile, open("pipeline_logs/cleaned_logs.txt", "w") as outfile:
    for line in infile:
        line = line.strip()
        if line:
            tokens = line.replace("[", "").replace("]", "").split()
            cleaned = " ".join(tokens[1:])
            outfile.write(cleaned + "\n")
