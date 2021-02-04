import os
import shutil

#This script sorts the files in the directory into folders according to their extension

def removeDuplicates(list_organize):
    format_list = []
    for element in list_organize:
        if element not in format_list:
            format_list.append(element)
    return format_list

def moveFiles(ext_list, file_list):
    for extension in ext_list:
        try:
            os.mkdir('Origanized_files/' + extension[-3:])
        except FileExistsError:
            print('Folder exist')
        for file in file_list:
            if file[-4:] == extension[-4:]:
                print('Move file ' + file + ' to: ' + extension)
                shutil.move(file, 'Origanized_files/'+extension[-3:])

if __name__ == '__main__':
    try: 
        current_route = input('Insert route: ') #Example: C:/Users/user/Downloads
        os.chdir(current_route)
        total_list = os.listdir()

        file_list = []
        for element in total_list:
            if element.find('.') != -1:
                file_list.append(element) 
        
        ext = [ext[-4:] for ext in file_list]
        ext = removeDuplicates(ext)
        
        if os.path.isdir('Origanized_files'):
            moveFiles(ext, file_list)
        else:
            os.mkdir('Origanized_files')
            moveFiles(ext, file_list)

    except FileNotFoundError:
        print('Route not found')
    
    