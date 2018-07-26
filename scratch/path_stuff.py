frame_regex = re.compile(r"\.([-\d]+)")  # find frame numbers in file paths

hash_regex = re.compile(r"\.(#+|@+)|\.[%\$F]+(\d+)d?")  # frame padding eg ####/@@@@/%04d/$F4

flag_regex = re.compile(r"^-+[a-zA-Z]")  # A flag is a - followed by a letter


def get_files_on_filesystem(search_str):
    """Search for all files that match the given search path.
    
    Args:
        search_str (str): The search term.
        
    Returns:
        list(str): The files matching the search term.
    
    Raises:
        FilesNotExist: If the input files don't exist on disk.
    """
    glob_search = hash_regex.sub(".*", search_str)
    paths = glob.glob(glob_search)
    if not paths:
        msg = "No files like '{0}' were found on the filesystem.".format(
            search_str
        )
        raise exc.FilesNotExist(msg)
    return paths


def create_destination_template(in_path):
    """Create a template string for later substitutions of frame values.
    
    The template can determine the frame padding value and create a format-style
    string accordingly.
    
    Args:
        in_path (str): The input search path.
    
    Returns:
        str: The template file path string.
    """
    count = itertools.count()
    def repl(match):
        """Replace hashing-type strings with python ones.
        
        Args:
            match (re.MatchObject): The match object.
        
        Returns:
            str: The python format string.
        """
        index = count.next()
        if match.group(1):
            pad = len(match.group(1))  # #### or @@@@ type
        else:
            pad = int(match.group(2))  # %04d or $F4 type
        return ".{{{0}:0{1}}}".format(index, pad)
    template = hash_regex.sub(repl, in_path)
    return template
