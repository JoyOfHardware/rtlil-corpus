set -ex

mkdir -p corpus

# List of files to skip
skip_files=("amaranth/examples/basic/ctr_en.py" "amaranth/examples/basic/uart.py")

for file in amaranth/examples/basic/*.py; do
    # Check if the current file is in the skip list
    if [[ " ${skip_files[@]} " =~ " $file " ]]; then
        continue  # Skip this file
    fi
    base_name=$(basename "$file" .py)  # Get the base name of the file without the .py extension
    python3 "$file" generate "corpus/$base_name.il"
done
