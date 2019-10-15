from itertools import groupby
import os
import hashlib

g = 4


def rot13(s):
    d = {}
    for c in (65, 97):
        for i in range(26):
            d[chr(i+c)] = chr((i+13) % 26 + c)
    
    return "".join([d.get(c, c) for c in s])


def find_dupe_files(dirpath):
    result = []
    temp = [(k, list(v)) for k, v in groupby(sorted(folder_md5(dirpath)), lambda x : x[1])]
    for entry in temp:
        if len(entry[1]) >= 2:
            result.append(entry)
    return result
    

def folder_md5(dirpath):
    for root, dirs, files in os.walk(dirpath):
        for filename in files:
            file_hexdigest = file_md5(filename)
            yield (os.path.join(root, filename), file_hexdigest)
    

def file_md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
        

def baz(start, *args):
    output = ""
    for i in args:
        if i % start == 0:
            output += ", {0}".format(i)
    
    output = output[2:]
    return output


def bar(newValue):
    global g
    g = newValue
    print("We updated the value of g to be {0}.".format(g))
    

def foo(endValue, start, stop):
    evenNumCounter=0
    for i in range(int(start), int(stop)+1, 1):
        if i==3:
            continue
        if i==endValue:
            break
        print(i)
        if i % 2 == 0:
            evenNumCounter+=1
    return evenNumCounter
    

def main():
    evenNums = foo(45, 1, 50)
    print("There were {0} even numbers.".format(evenNums))
    
    bar(6)

    baz_output = baz(10, *[4,20,65,70,467,500,37,69,30,40,50])
    print("baz_output = {0}".format(baz_output))
    
    # NOTE: Replace the folder path '/home' with the path to the folder this script
    # is actually living in
    hex_string = file_md5('/home/python-functions.py')
    print("hash of file {0} = '{1}'".format('/home/python-functions.py', hex_string))
    
    # By the way -- for the code below to work, it's advised to either (a) create a 
    # duplicate of this script in the same directory, or (b) create some other files
    # that may have unique names, but identical content
    for next_hash in folder_md5('/home'):
        print(next_hash)
        
    print("Duplicate files found (with their hashes):")    
    print(find_dupe_files('/home'))
    
    print("rot13('Hello, world!') = {0}".format(rot13('Hello, world!')))
    print("rot13('foobar') = {0}".format(rot13('foobar')))
    
    
if __name__ == "__main__":
    main()


