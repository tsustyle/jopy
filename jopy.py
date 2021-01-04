import re
import sys
import os


path, platform, name = sys.argv[1], sys.argv[2], sys.argv[3]
files = os.listdir(path)
markdown_file = [i for i in files if i.endswith('.md')]
markdown_path = path + markdown_file[0]
images_directory = path + '_resources/'

git_path = '![img](/assets/images/' + platform + '/' + name + '/'

# writes the new file with correct links
def write_new_file():
    file_input = open(markdown_path, "rt")
    file_output = open(path + 'new.md', 'wt')
    link_list = rename_png_and_make_link_list()

    for i in link_list:
        for line in file_input:
            if line.strip().endswith('.png)'):
                file_output.write('\n' + i + '\n')
                break
            else:
                file_output.write(line)

#renames the image files and creats a list of links
def rename_png_and_make_link_list():
    with open(markdown_path, 'r') as f:
        x = f.read()
        filenames = re.findall("\((.*)\)", x)
        filenames = [i.replace("../", "").replace("_resources/", "") for i in filenames if i.endswith('.png')]

    link_list = []
    num = 0

    for i in filenames:
        os.rename(images_directory +i, images_directory + str(num) + '.png')
        link_list.append(git_path + str(num) + '.png)')
        num += 1

    os.rename(images_directory, path + name)
    return link_list

#make sure the directory is clean
if len(markdown_file) > 1:
    print('Too many markdown files present in directory. Exiting.')
else:
    write_new_file()

