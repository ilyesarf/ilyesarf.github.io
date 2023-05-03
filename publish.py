import os
import markdown


class Convert:
    def __init__(self, dir="site"):
        self.dir = dir
         
    def md2html(self, path):
        with open(path, 'r') as f:
            html = markdown.markdown(f.read())

        new_path = path.split('/')[1:]

        subdir = '.'
        if len(new_path) > 1: 
            subdir = os.path.join(*(new_path[:-1]))
            if not os.path.isdir(subdir):
                os.mkdir(subdir)

        self.cleanup(subdir)
        file = new_path[-1]
        file = file.replace(file.split('.')[-1], 'html')
        print(os.path.join(subdir, file))

        with open(os.path.join(subdir, file), 'w') as f:
            f.write(html)

    def convert(self):
        for subdir, dirs, files in os.walk(self.dir):
            if "." not in subdir[2:]:
                for f in files:
                    if any(ext in f for ext in ["md", "markdown"]):
                       self.md2html(os.path.join(subdir, f)) 
    """
    def cleanup(self, dir):
        for subdir in list(filter(lambda x: os.path.isdir(x) and '.' not in x, os.scandir(dir))):
                print(subdir)
    """         
            
if __name__ == '__main__':
    convert = Convert()
    convert.convert()
