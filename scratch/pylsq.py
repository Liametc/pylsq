import itertools
import glob
import os
import re

if __name__ == "__main__":

    glob_path= '/jobs/ancient/assets/environment/mainstreet/3d/surface/work/maya/images/vegetationScatter/mj0290/base/*_v122/*'
    
    paths = glob.glob(glob_path)

    regex = re.compile(r".*\.(\d*)\.exr")
    
    paths = sorted(paths)
    
    def key_func(item):
        return item.split('.',1)[0]
        
    def func(items):
        return items[1] - items[0]

    for id_, group in itertools.groupby(paths, key=key_func):
        x = []
        path = ""
        for item in group:
            match = regex.match(item)
            if match:
                x.append(int(match.group(1)))
            path = item
                

        groups = []
        prev = set()
        for index, (id_, g) in enumerate(itertools.groupby(itertools.izip(x[:-1], x[1:]), func)):
            this_grp = set()
            for item in g:
                    this_grp.update(item)
            if len(this_grp) <= 2 and id_ == 1:
                continue
            prev.difference_update(this_grp)
            groups.append((id_, this_grp))
            prev = this_grp

        frame_str = ''
        first = ''
        for step, frange in groups:
            frame_str += first
            first = ','
            if len(frange) == 1:
                    frame_str += '{0}'.format(next(iter(frange)))
            elif step == 1:
                    frame_str += '{0}-{1}'.format(min(frange), max(frange))
            else:
                    frame_str += '{0}-{1}x{2}'.format(min(frange), max(frange), step)
        
        print os.path.dirname(path), '\n\t', re.sub('\.\d*\.', '.####.', os.path.basename(path)), frame_str
