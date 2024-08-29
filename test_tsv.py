import csv
def read_tsv_file(file_path):
        print("inside read tsv")
        with open(file_path, 'r') as file_reader:
            print(file_reader)
            try:
                tsvin = csv.reader(file_reader, delimiter='\t')
                print("tsvin")
                print(tsvin)
                for line in tsvin:
                    yield line
            except Exception as e:
               print(e)

for data in read_tsv_file(r"C:\python_projects\fake_annotations.txt"):
     print("data",data)