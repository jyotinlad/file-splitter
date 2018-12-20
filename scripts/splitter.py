from os import path
from json import dumps

# define directories
root_dir = path.dirname(path.dirname(__file__))
files_dir = path.join(root_dir, "files")
source_dir = path.join(files_dir, "source")
target_dir = path.join(files_dir, "target")

# define source file
filename = "BlackFriday.csv"
file = path.join(source_dir, filename)

seperator = ","

with open(file, "r") as fh_in:
    # get header row for column names
    header = fh_in.readline()
    header = header.rstrip()
    columns = header.split(seperator)

    lines = fh_in.readlines()
    for line in lines:
        line = line.rstrip()
        rec = dict(zip(columns, line.split(seperator)))

        # check user and product exist so a good file name can be created
        user = rec.get("User_ID")
        product = rec.get("Product_ID")
        if not user and not product:
            continue

        output_filename = "{}.{}.json".format(user, product)
        output_file = path.join(target_dir, output_filename)
        print("creating file: {}".format(output_filename))
        with open(output_file, "w") as fh_out:
            fh_out.write(dumps(rec, indent=4))
