import gzip, struct


# pointer position starts at start.
# everytime .read() function is called, pointer possition 
# stays where .read() stoped. 

def read_labels_from_file(filename):
    with gzip.open(filename,'rb') as myFile:

        magicNum = myFile.read(4)

        #  firstbyte var would print as: b'\x00\x00\x08\x03'
        # In binary, this is: 00000000 00000000 00000100 00000011

        print(type(magicNum))
        print(magicNum)

        print("Magic Number: ",int.from_bytes(magicNum, 'big'))

        no_lbl = myFile.read(4) # read how many labels in the file 
        no_lbl = int.from_bytes(no_lbl, 'big') # convert from bytes into ints
        print("Number of labels: ", no_lbl)

        labels = [myFile.read(1) for i in range(no_lbl)] # read labels byte by byte
        labels = [int.from_bytes(label, 'big') for label in labels] # convert into ints

        return labels

train_labels = read_labels_from_file('data/train-labels-idx1-ubyte.gz')
test_labels = read_labels_from_file('data/t10k-labels-idx1-ubyte.gz')