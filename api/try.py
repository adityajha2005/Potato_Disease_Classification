import os

file_path = "D:\models\model_vmodel69.keras"
if not os.path.isfile(file_path):
    print(f"File not found: {file_path}")
else:
    print(f"File found: {file_path}")
