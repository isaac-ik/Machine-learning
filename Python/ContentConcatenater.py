import sys

def main()->None:
    conconcated = ""
    if len(sys.argv) > 1:
        for var in range(1, len(sys.argv), 1):
            try:
                file = open(sys.argv[var], "r")
                valid = True
            except:
                print("file: {} cant be opened".format(sys.argv[var]))
                valid = False
            if valid == True:
                content = file.read()
                conconcated = conconcated + content
                file.close()
    else:
        print("without Command line arguments")
    print(conconcated)
    
main()
