import os

def organize_config():
    # Prompt the user for the file path
    input_path = input("Enter the input path for config.ini: ").strip()
    
    # Ensure the file exists
    if not os.path.isfile(input_path):
        print("Error: File not found.")
        return

    # Read and parse the file
    with open(input_path, 'r') as file:
        lines = file.readlines()

    # Group entries (4 lines per entry, with the 4th being empty)
    entries = []
    for i in range(0, len(lines), 4):
        if i + 3 < len(lines):  # Ensure no out-of-bounds access
            entry = lines[i:i+4]
            if len(entry) == 4 and entry[1].startswith("url = ") and entry[2].startswith("valid_string = ") and entry[3].strip() == "":
                entries.append(entry)
            else:
                print(f"Skipping malformed entry at lines {i + 1}-{i + 4}")
    
    if not entries:
        print("No valid entries found in the config file.")
        return

    # Sort entries by URL
    sorted_entries = sorted(entries, key=lambda x: x[1].split(" = ")[1].strip())
    
    # Reassign link numbers
    for idx, entry in enumerate(sorted_entries, 1):
        entry[0] = f"[Link {idx}]\n"
    
    # Save the sorted entries to a new file
    output_path = os.path.join(os.path.dirname(input_path), 'config_organized.ini')
    with open(output_path, 'w') as file:
        for entry in sorted_entries:
            file.writelines(entry)
    
    # Display the statistics
    total_links = len(entries)
    print(f"Links Found: {len(lines) // 4}")
    print(f"Links Moved: {total_links}")
    print(f"Total Entries: {total_links}")
    print(f"Organized file saved as: {output_path}")

if __name__ == "__main__":
    organize_config()
