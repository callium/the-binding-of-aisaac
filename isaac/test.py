# Here is a testing playground
import genetics as gen

def main():

    # This will be done every x seconds
    test_frame = gen.Frame()
    test_frame.populate((2, 5), [(1, 2),(3, 4)], 2, 5)
    test_frame.print_frame()

    # Then you will insert the frame into the gene
    test_gene = gen.Gene()
    test_gene.add_frame(test_frame)
    test_gene.print_gene()

if __name__ == "__main__":
    main()