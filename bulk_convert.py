import os
import subprocess

# Define the path to the folder containing the .ckpt or .safetensor files
path = '<path where to save LoRAs>'
models = '<path where models exist>'

# `dim` is the dimension of the LoRA. `svp` is the save precision.
dim = 300
svp = "fp16"

# Creating a folder called output in the path folder.
output_folder = os.path.join(path, 'output')
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all the files in the folder
for filename in os.listdir(models):
    # Checking if the file ends with .ckpt and if it does not contain v1-5-pruned.
    if (filename.endswith('.ckpt') or filename.endswith('.safetensors')) and 'v1-5-pruned' not in filename:
        # Construct the full path to the file
        file_path = os.path.join(models, filename)

        # Remove the .ckpt extension from the filename
        stripped_filename = filename[:-5] if filename.endswith('.ckpt') else filename[:-12]

        # Use subprocess to run another Python script on the file
        subprocess.run(
            ['python', 'lib/extract_lora_from_models.py', "--save_precision", f"{svp}",
             "--save_to", f"{output_folder}/{stripped_filename}_LoRA{dim}.safetensors", "--model_tuned", file_path,
             "--model_org",
             f"{path}/v1-5-pruned.ckpt", "--dim", f"{dim}", ])
