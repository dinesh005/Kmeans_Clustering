import os
import sys
if __name__ == '__main__':
    print "...............Started the K means based clustering..................... "
    print "..........Running..........."
    os.system("python dataextract.py")
    print "...............Finished the K means based clustering....................."

    print "...............Started the K(Weighted) means based clustering.................. "
    os.system("python weightedKNN.py")
    print "...............Finished the K(Weighted) means based clustering..................."


    print "....................Finished all the Training and Testing..................."
    print "....................Started the analysis and report........................."

    print "Details:"
    print "1. error_Matrix contains the error values of k means based clustering"
    print "2. error_Matrix_KModified contains the error values of k(Weighted) means based clustering"
    print "3. Accuracies datails of the tested data with the k values obtained from k means based clustering and k(Weighted) means clustering"

    print "................plotting the graph..........................."
    os.system("python graph_plot.py")
