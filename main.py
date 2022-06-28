import os
from pathlib import PurePath

def main() -> None:
    print('----------------------  FAST RENAMER  ----------------------\n')
    
    prefix, suffix = get_prefix_and_suffix()
    
    if prefix != '' or suffix != '':    
        rename_files(prefix, suffix)
        
    else:
        print('You did not enter any prefix or suffix. The files will not be renamed.')
        exit()
              
def get_prefix_and_suffix() -> tuple[str, str]:
    prefix = input('Enter the PREFIX of the files (leave it empty if you want): ')
    suffix = input('Enter the SUFFIX of the files (leave it empty if you want): ')
    
    return prefix, suffix
    
def rename_files(prefix, suffix) -> None:
    for path, subdirs, files in os.walk(ROOT_DIR):
        if(path != ROOT_DIR): # skip the root directory
            print(path)
            
            for name in files:
                name_split = name.split('.')
                
                old_path = PurePath(path, name)
                new_path = PurePath(path, prefix + name_split[0] + suffix + '.' + name_split[1])
                
                os.rename(old_path, new_path)
                print('   ', old_path, '->', new_path)
            
            print('\n')

    exit()
    
def exit():
    input('\nPress ANY KEY to exit...')
            
if __name__ == '__main__':
    ROOT_DIR = '.' + os.sep
    main()