import re, sys, os, shutil, glob
from datetime import date

try:
    path, platform, name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Cleaning up the export because Joplin likes to export all of the parent notebooks
    md_file = glob.glob(path + "**/*.md", recursive=True)
    shutil.move(md_file[0], path + 'file.md')

    files = os.listdir(path)

    try:
        for i in files:
            if i.endswith('.md') or i == '_resources':
                pass
            else:
                os.remove(i)
    except:
        print(f"\n[!] Couldn't remove {i}! Skipping cleanup. [!]")

    markdown_path = path + 'file.md'
    images_directory = path + '_resources/'

    git_path = '![img](/assets/images/' + platform + '/' + name + '/'
    todays_date = date.today().strftime("%Y-%m-%d")

    # writes the new file with correct links
    def write_new_file():
        file_input = open(markdown_path, "r")
        file_output = open(path + f'{todays_date}-{name}.md', 'w')
        link_list = rename_png_and_make_link_list()

        #for i in link_list:
        x = 0
        for line in file_input:
            if line.strip().endswith('.png)'):
                file_output.write('\n' + link_list[x] + '\n')
                x += 1
            else:
                file_output.write(line)

        file_input.close()
        file_output.close()
        os.remove(markdown_path)

    #renames the image files and creates a list of links
    def rename_png_and_make_link_list():
        with open(markdown_path, 'r') as f:
            x = f.read()
            filenames = re.findall("\((.*)\)", x)
            filenames = [i.replace("../", "").replace("_resources/", "") for i in filenames if i.endswith('.png')]

        link_list = []

        for index, i in enumerate(filenames):
            os.rename(images_directory +i, images_directory + str(index) + '.png')
            link_list.append(git_path + str(index) + '.png)')

        os.rename(images_directory, path + name)
        return link_list

    write_new_file()
    print('[+] Done! [+]\n')
except:
    print('\n[!] Usage: python3 jopy.py /path/to/export/folder/ category name [!]\n')
