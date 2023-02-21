import os, sys
import json


result = []


def get_duplicates(a):
    folder_path = a
    folder = os.listdir(folder_path)
    try:
        status=0
        for file in folder:
            file_path = f'{folder_path}/{file}'
            json_file = json.load(open(file_path, encoding="utf8"))
            result = list(json_file.items())[1][1]
            pks = [(item['PK'], item['SK']) for item in result]
            res = list(set([item for item in pks if pks.count(item)>1]))
            for item in pks:
                if pks.count(item) > 1:
                    status = 1

            if res == []:
                print(f"{file} : no Duplicates found")
            else:
                print(f"All the duplicates from file:{file} are : + {res}")
                sys.exit(1)

        return status
    except IndexError:
        print("Cannot access out of range elements")


def main():
    status = get_duplicates('fixtures')
    print(status)


if __name__ == "__main__":
    main()