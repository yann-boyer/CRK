import argparse
import hashlib

parser = argparse.ArgumentParser(description = "A small utility !")
parser.add_argument("input_file_path", metavar = "INPUT_FILE_PATH", type = str, help = "Path of the file you want to (en/de)crypt !")
parser.add_argument("output_file_path", metavar = "OUTPUT_FILE_PATH", type = str, help = "Path of the final file !")
parser.add_argument("key", metavar = "KEY", type = str, help = "Key used for (en/de)crypt !")

args = parser.parse_args()

key_sha256 = hashlib.sha256(args.key.encode("utf-8")).digest()

with open(args.input_file_path, "rb") as input_file:
    with open(args.output_file_path, "wb") as output_file:
        i = 0
        while input_file.peek():
            c = ord(input_file.read(1))
            j = i % len(key_sha256)
            b = bytes([c ^ key_sha256[j]])
            output_file.write(b)
            i += 1

print("Task executed successfuly !")
