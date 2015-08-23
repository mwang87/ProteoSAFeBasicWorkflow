#!/usr/bin/python


import sys
import getopt
import os

def get_header_mappings(header_str):
    header_mapping = {}
    header_splits = header_str.rstrip().split("\t")
    index_count = 0
    for header in header_splits:
        header_mapping[header] = index_count
        index_count += 1
    return header_mapping

def parse_xml_file(input_file):
    key_value_pairs = {}
    for line in input_file:
        #print line
        new_line = line.rstrip().replace("<parameter name=\"", "")
        #new_line = new_line.replace("\">", "=")
        new_line = new_line.replace("</parameter>", "")

        splits = new_line.split("\">")
        #print splits
        if(len(splits) != 2):
            continue


        if(splits[0] in key_value_pairs.keys()):
          key_value_pairs[splits[0]].append(splits[1])
        else:
          key_value_pairs[splits[0]] = []
          key_value_pairs[splits[0]].append(splits[1])
    return key_value_pairs

def get_mangled_file_mapping(params):
    all_mappings = params["upload_file_mapping"]
    mangled_mapping = {}
    for mapping in all_mappings:
        print mapping
        splits = mapping.split("|")
        mangled_name = splits[0]
        original_name = splits[1]
        mangled_mapping[mangled_name] = original_name

    return mangled_mapping


def parse_table_with_headers(filename):
    input_file = open(filename, "r")

    line_count = 0
    headers = []
    index_to_header_map = {}
    column_values = {}
    for line in input_file:
        line_count += 1
        if line_count == 1:
            headers = line.split("\t")
            header_idx = 0
            for header in headers:
                print header
                index_to_header_map[header_idx] = header
                header_idx += 1
                if len(header) > 1:
                    column_values[header] = []

            continue

        line_splits = line.split("\t")
        column_count = 0
        for line_split in line_splits:
            header_name = index_to_header_map[column_count]
            if len(header_name) < 1:
                continue
            column_values[header_name].append(line_split)
            column_count += 1

    return (line_count-1, column_values)



#Making sure directory exists, if not make it.
def make_sure_path_exists(path):
    if not os.path.exists(directory):
        os.makedirs(directory)

def usage():
    print "<TODO>"

def main():
    usage()

    input_data_folder = sys.argv[1]
    input_parameters = sys.argv[2]
    output_log_filename = sys.argv[3]
    output_result_folder = sys.argv[4]

    #Parsing the parameters
    parsed_parameters = parse_xml_file(open(input_parameters))
    print parsed_parameters


    #Execute Whatever you need here

    #Dummy writing file into result
    output_result_filename = os.path.join(output_result_folder, "test.out")
    output_result_file = open(output_result_filename, "w")
    output_result_file.write("TEST DATA")
    output_result_file.close();
    

    #Output Log File
    output_log_file = open(output_log_filename, "w")
    output_log_file.write("Run Successful")
    output_log_file.close()


if __name__ == "__main__":
    main()
