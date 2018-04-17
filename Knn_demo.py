from numpy import *


def createDataSet():
    group = array([[1.0, 0.9], [1.0, 1.0], [0.1, 0.2], [0.0, 0.1]])
    labels1 = ['A', 'A', 'B', 'B']  # four samples and two classes
    return group, labels1


def kNNClassify(newInput, dataset, labels1, k):
    numSamples = dataset.shape[0]
    diff = tile(newInput, (numSamples, 1)) - dataset
    squareDiff = diff ** 2
    squareDist = sum(squareDiff, axis=1)
    distance = squareDist ** 0.5
    sortedDistIndices = argsort(distance)

    classCount = {}
    for i in range(k):
        voteLabel = labels1[sortedDistIndices[i]]
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1

    maxCount = 0
    for key, value in classCount.items():
        if value > maxCount:
            maxCount = value
            maxIndex = key

        return maxIndex


if __name__ == "__main__":
    dataSet, labels1 = createDataSet()

    testX = array([1.2, 1.0])
    k = 3
    outputLabel = kNNClassify(testX, dataSet, labels1, k)
    print("Your input is:", testX, "and classified to class:", outputLabel)
    testX = array([0.1, 0.3])
    outputLabel = kNNClassify(testX, dataSet, labels1, k)
    print("Your input is:", testX, "and classified to class:", outputLabel)
