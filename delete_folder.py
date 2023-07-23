import shutil


def delete_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
        print(f"Folder deleted  successfully, hurrrayyy")
    except FileNotFoundError:
        print("File not found")  
    except Exception as e:
        print(f"Error as  {e}")
        
        
if __name__ == "__main__":
    folder_path  = r"C:\Users\USER\Desktop\testing"
    delete_folder(folder_path)             