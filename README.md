# Jopy

### Why

I use Joplin as my note taking app and I found it frustrating to have to go through my file and change all of the links to match my website's filesystem, so I wrote this little script to handle it.

### What does it do?

Joplin saves images with a random name, this script will parse the exported markdown file and rename them to your specifications (in a new file called new.md).

Example before:

![before](/images/before.png)

Example after:

![after](/images/after.png)

### Full list of features
- Parses and edits the document to match your filesystem
- Renames each screenshot in relation to where it is in the document (0 - first | 1 - second... etc)
- Saves the document as YEAR-MONTH-DAY-NAME.md for easy Jekyll Blog integration
- Renames the screenshots folder to match the document name
- Attempts to clean up after the Joplin export by removing uneeded and empty folders


### If you found this...

I don't imagine many people stumbling across this, but if you do and you want to use it then you're going to have to either modify your website's filesystem or modify the script. Right now it sets the links as `/assets/images/platform/name/`, change that line to your website's image folder OR change your website's images directory `/assets/images/`

### How do I use it?

It takes three arguments:
1. path to your exports folder
2. platform (name of images subdirectory (/images/subdirectory))
3. name (name of images subdirectory's subdirectory (/images/subdirectory/subdirectory))

### Usage example

`python3 jopy.py /home/user/exported/ hackthebox doctor`

### Todo

- Switch from `sys.argv[]` to `argparse`
- GitHub integration for automatic staging and pushing after formatting



