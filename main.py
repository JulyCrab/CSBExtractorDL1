import subprocess
import sys
from pathlib import Path
from configparser import ConfigParser

# Display information to the user
print(" ")
print("\nTool made by MrJuly for Dying Light 1")
print("Before using this tool, please check the README in the HELP folder if you haven't already")
print("Please set up this file before using it, or you will encounter errors\n")
print(" ")

# Load settings from the configuration file
settings = ConfigParser()
settings.read('settings.ini')

# Extract settings from the configuration file
QuickBMSDir = settings.get('Config', 'quickbmsdir')
Output = settings.get('Config', 'outputdir')
ExtractDir = settings.get('Config', 'extractdir')
BMSScript = settings.get('Config', 'bmsscript')
BMSexe = settings.get('Config', 'quickbmsexe')

# Check if required directories and files exist
required_paths = [
    QuickBMSDir, Output, ExtractDir,
    QuickBMSDir + '/' + BMSScript,
    QuickBMSDir + '/' + BMSexe
]

for path in required_paths:
    if not Path(path).exists():
        raise ValueError(f"Path not found: {path}")

# Check for .csb files in the extraction directory
csb_files = list(Path(ExtractDir).glob('*.csb'))
if not csb_files:
    raise ValueError(f"No .csb files found in: {ExtractDir}")

# Process each .csb file
for csb_file in csb_files:
    output_csb_dir = Path(Output) / csb_file.name

    # Clean up existing .fsb files if they exist
    for fsb_file in output_csb_dir.glob('*.fsb'):
        fsb_file.unlink()

    # Create output directory if it doesn't exist
    output_csb_dir.mkdir(exist_ok=True)

    # Run QuickBMS to extract files
    extraction_command = [
        QuickBMSDir + "/" + BMSexe,
        QuickBMSDir + "/" + BMSScript,
        str(csb_file),
        str(output_csb_dir)
    ]
    
    result = subprocess.run(extraction_command, capture_output=True)
    
    sys.stdout.buffer.write(result.stdout)
    sys.stderr.buffer.write(result.stderr)
