import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """

    evidence = []
    labels = []

    months = dict()
    months = {"Jan": 0, "Feb": 1, "Mar": 2, "Apr": 3, "May": 4, "June": 5, "Jul": 6, "Aug": 7, "Sep": 8, "Oct": 9, "Nov": 10, "Dec": 11 }

    with open(filename, 'r') as f:
        csvreader = csv.reader(f)
        next(csvreader, None) #Skip the headers
        for i in csvreader:
            row = [int(i[0]), #Administrative
                   float(i[1]), #Administrative_Duration
                   int(i[2]), #Informational
                   float(i[3]), #Informational_Duration
                   int(i[4]), #ProductRelated
                   float(i[5]), #ProductRelated_Duration
                   float(i[6]), #BounceRates
                   float(i[7]), #ExitRates
                   float(i[8]), #PageValues
                   float(i[9]), #SpecialDay
                   months[i[10]], #Month
                   int(i[11]), #OperatingSystems
                   int(i[12]), #Browser
                   int(i[13]), #Region
                   int(i[14]), #TrafficType
                   1 if i[15] == "Returning_Visitor" else 0, #VisitorType
                   1 if i[16] == "TRUE" else 0 #Weekend
                   ]
            evidence.append(row)

            #Revenue
            if i[17] == "TRUE":
                labels.append(1)
            else:
                labels.append(0)
    return (evidence, labels)


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    n = KNeighborsClassifier(n_neighbors = 1)
    n.fit(evidence, labels)
    return n


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    
    truePositive = 0
    trueNegative = 0
    positive = labels.count(1)
    negative = labels.count(0)

    for i in range(len(labels)):
        if labels[i] == 1 and predictions[i] == 1:
            truePositive += 1
        elif labels[i] == 0 and predictions[i] == 0:
            trueNegative += 1 

    sensitivity = truePositive / positive
    specifivity = trueNegative / negative

    return (sensitivity, specifivity)


if __name__ == "__main__":
    main()
