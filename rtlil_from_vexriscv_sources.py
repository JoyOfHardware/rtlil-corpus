import os
import subprocess
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Process Verilog files to RTLIL format.")
parser.add_argument("--outdir", required=True, help="Output directory for generated RTLIL files.")
args = parser.parse_args()

output_dir = args.outdir

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Directory containing Verilog files
verilog_dir = "VexRiscv-verilog"

# Iterate over all .v files in the Verilog directory
for file in os.listdir(verilog_dir):
    if file.endswith(".v"):
        file_path = os.path.join(verilog_dir, file)
        base_name = os.path.splitext(file)[0]  # Get the base name without the extension
        output_file = os.path.join(output_dir, f"{base_name}.rtlil")

        # Run the yosys command
        yosys_command = f"yosys -p\"read_verilog {file_path}; write_rtlil {output_file}\""
        try:
            subprocess.run(yosys_command, shell=True, check=True)
            print(f"Successfully processed {file_path} to {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error: Failed to process {file_path}. Details: {e}")
            break
