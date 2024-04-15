# Designer PDF Viewer
# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
# Selection area of characters given the input heights of 26 letters

def designerPdfViewer(h, word):
    # abc..z
    letterdict = {chr(key): h[key-97] for key in range(97, 123)}
    largest = 0
    for i in word:
        largest = letterdict[i] if letterdict[i] > largest else largest

    return largest * len(word)

print(designerPdfViewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 'abc'))