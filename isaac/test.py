# Here is a testing playground
import genetics as gen

# Try and create a frame(will be done every x seconds), then
# add that frame to the current gene(or run in the game)
def test_frames_and_genes():
    test_frame = gen.Frame()
    test_frame.populate((2, 5), [(1, 2),(3, 4)], 2, 5)
    test_frame.print_frame()

    # Then you will insert the frame into the gene
    test_gene = gen.Gene()
    test_gene.add_frame(test_frame)
    test_gene.print_gene()


def main():
    test_frames_and_genes()
    

if __name__ == "__main__":
    main()

