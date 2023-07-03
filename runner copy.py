import os
import shutil
import subprocess
import time



def run_python_script(script_path):
    try:
        subprocess.run(["python", script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {script_path}: {e}")


def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print("File deleted successfully.")
    else:
        print("File not found.")

def main():
    input_directory = "Scores"  # Specify the desired input directory here

    #script1_path = "D:/user/Ioakeim Sogiakas/Music/MusicCrack/svg_files_only.py"
    script2_path = "D:/user/Ioakeim Sogiakas/Music/MusicCrack/transpose.py"

    print('Running svg_files_only.py')
    #run_python_script(script1_path)
    #time.sleep(5)  # Delay for 5 seconds
    print('Running transpose.py')
    run_python_script(script2_path)

    # Call the function to create the temporary folder
    create_temp_folder(input_directory)

    # Specify the path of the file you want to delete
    file_path = "D:\\user\\Ioakeim Sogiakas\\Music\\MusicCrack\\temp_folder.pdf"

    # Delete the file
    delete_file(file_path)


if __name__ == "__main__":
    main()

def create_temp_folder(input_directory):
    program_directory = os.path.dirname(os.path.abspath(__file__))
    scores_directory = os.path.join(program_directory, input_directory)

    # Create or empty the temporary folder in the "Scores" directory
    temp_folder_path = os.path.join(scores_directory, "temp_folder")
    if os.path.exists(temp_folder_path):
        shutil.rmtree(temp_folder_path)
    os.makedirs(temp_folder_path)
    print('Folder made and/or emptied.')

    for folder_name in os.listdir(scores_directory):
        folder_path = os.path.join(scores_directory, folder_name)
        if os.path.isdir(folder_path):

        # Copy the entire folder to the temporary folder
            folder_destination = os.path.join(temp_folder_path, folder_name)
            shutil.copytree(folder_path, folder_destination)
          # Add a delay to allow any lingering processes to release the file
        shutil.rmtree(folder_path)

print('DONE!!!')
