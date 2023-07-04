import subprocess
import time
import os

def run_python_script(script_path):
    try:
        subprocess.run(["python", script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {script_path}: {e}")

def count_folders(directory):
    folders = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name)) and name != 'temp']
    return len(folders)

def main():
    script1_path = "D:/user/Ioakeim Sogiakas/Music/MusicCrack/svg_files_only.py"
    script2_path = "D:/user/Ioakeim Sogiakas/Music/MusicCrack/transpose2_0.py"
    scores_directory = r"D:\user\Ioakeim Sogiakas\Music\MusicCrack\Scores"

    print('Running svg_files_only.py')
    run_python_script(script1_path)
    time.sleep(3)  # Delay for 3 seconds

    folder_count = count_folders(scores_directory)
    print(f"Detected {folder_count} folders in the Scores directory.")

    for _ in range(folder_count):
        print('Running transpose2_0.py')
        run_python_script(script2_path)
        time.sleep(3)  # Delay for 3 seconds between each execution

    print('DONE!!!')

if __name__ == "__main__":
    main()
