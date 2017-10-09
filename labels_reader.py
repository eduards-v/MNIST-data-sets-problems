import gzip

# pointer position starts at start.
# everytime .read() function is called, pointer possition 
# stays where .read() stopped. 

def read_label_training_sets(filename):
    with gzip.open(filename, "rb") as labels_file:
        
        magicNum = labels_file.read(4)
        print("Magic Number: ",int.from_bytes(magicNum, 'big'))
        
        no_lbls = labels_file.read(4)
        no_lbls = int.from_bytes(no_lbls, 'big') # convert from bytes into ints   
        print("Number of labels in file: ", no_lbls)

        labels = [labels_file.read(1) for i in range(no_lbls)] # read labels byte by byte
        labels = [int.from_bytes(label, 'big') for label in labels] # convert into ints

        opt = input("Would you like to print array of labels? y/n: ")
        if(opt == "y"): print("Labels: ", labels)


# read_label_training_sets('data/train-labels-idx1-ubyte.gz') # for testing
