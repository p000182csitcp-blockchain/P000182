import os


# get all local records'name(y)
def get_local_file_list() -> set:
    arr = next(os.walk("./file"))[2]
    local_files = set()
    for file in arr:
        local_files.add(file)
    return local_files


# clean the file directory
def clean_file():

    local_files = get_local_file_list()

    # set default file list
    default_files = {
        "DefaultPhoto.jpg",
        "photo.jpg",
        "private_key.pem",
        "file_to_save.bin",
    }

    # creating the difference of the two sets
    diff_files = local_files - default_files

    # remove the files
    for file in diff_files:
        os.remove("file/" + file)
