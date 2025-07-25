def remove_duplicate_ids(input_file, output_file=None):
    # Read IDs from file
    with open(input_file, 'r') as f:
        ids = f.read().splitlines()

    # Remove empty lines and convert to integers
    ids = [int(id_) for id_ in ids if id_.strip().isdigit()]

    # Remove duplicates using a set and sort in ascending order
    unique_ids = sorted(set(ids))

    # Write unique sorted IDs back to the same file or new one
    target_file = output_file if output_file else input_file
    with open(target_file, 'w') as f:
        for id_ in unique_ids:
            f.write(f"{id_}\n")

    print(f"Removed duplicates and sorted IDs. Saved to '{target_file}'.")


# Example usage
if __name__ == "__main__":
    remove_duplicate_ids("parks.txt")  # change to your file name if needed