import subprocess
import time
import os
def run_python_script(script_path):
    try:
        subprocess.run(["python", script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {script_path}: {e}")

def main():
    script1_path = "D:/user/Ioakeim Sogiakas/Music/MusicCrack/svg_files_only.py"
    script2_path = "D:/user/Ioakeim Sogiakas/Music/MusicCrack/transpose.py"


    print('Running svg_files_only.py')
    run_python_script(script1_path)
    time.sleep(5)  # Delay for 5 seconds
    print('Running ranspose.py')
    run_python_script(script2_path)

if __name__ == "__main__":
    main()

# Specify the path of the file you want to delete
file_path = "D:\\user\\Ioakeim Sogiakas\\Music\\MusicCrack\\temp_folder.pdf"

# Check if the file exists
if os.path.exists(file_path):
    # Delete the file
    os.remove(file_path)
    print("File deleted successfully.")
else:
    print("File not found.")

    

print('DONE!!!')