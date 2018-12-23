from collections import defaultdict
from json import dumps
from os import path

# define directories
root_dir = path.dirname(path.dirname(__file__))
files_dir = path.join(root_dir, "files")
source_dir = path.join(files_dir, "source")
target_dir = path.join(files_dir, "target")

# define source file
filename = "BlackFriday.csv"
file = path.join(source_dir, filename)

# define file separator
seperator = ","

with open(file, "r") as fh_in:
    # get header row for column names
    header = fh_in.readline()
    header = header.rstrip()
    columns = header.split(seperator)

    # store for sales per product
    products = defaultdict(list)

    # iterate sales
    lines = fh_in.readlines()
    for line in lines:
        line = line.rstrip()
        rec = dict(zip(columns, line.split(seperator)))

        # check product ID exists
        product_id = rec.get("Product_ID")
        if product_id:
            # add sale to the list for the product
            products[product_id].append(rec)

    # output file per product
    for product_id in products:
        output_filename = "{}.json".format(product_id)
        output_file = path.join(target_dir, output_filename)
        print("creating file: {}".format(output_filename))
        with open(output_file, "w") as fh_out:
            # print header row
            fh_out.write("{}\n".format(",".join(columns)))

            for rec in products.get(product_id):
                # print record row
                values = list(map(rec.get, columns))
                fh_out.write("{}\n".format(",".join(values)))
