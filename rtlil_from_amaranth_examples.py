import os
import subprocess
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Process RTLIL files.")
parser.add_argument("--outdir", required=True, help="Output directory for generated RTLIL files.")
parser.add_argument("--amaranth", default="amaranth", required=False, help="Path to amaranth dir.")
args = parser.parse_args()

amaranth_dir = args.amaranth
output_dir = args.outdir

# Enable extended debug output
set_ex = True
if set_ex:
    print("Debug: Starting script execution")

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# List of files to skip
skip_files = [
    f"{amaranth_dir}/examples/basic/ctr_en.py",
    f"{amaranth_dir}/examples/basic/uart.py"
]

# Iterate over all .py files in the directory
example_dir = f"{amaranth_dir}/examples/basic"
for file in os.listdir(example_dir):
    if file.endswith(".py"):
        file_path = os.path.join(example_dir, file)

        # Check if the current file is in the skip list
        if file_path in skip_files:
            continue  # Skip this file

        # Get the base name of the file without the .py extension
        base_name = os.path.splitext(file)[0]

        # Run the Python script with the specified arguments
        try:
            subprocess.run([
                "python3",
                file_path,
                "generate",
                f"{output_dir}/{base_name}.il"
            ], check=True)
            if set_ex:
                print(f"Debug: Successfully processed {file_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error: Failed to process {file_path}. Details: {e}")
