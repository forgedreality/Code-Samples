# panel layout helper
# import nanocommunicator

'''
{
  "numPanels": 26,
  "sideLength": 150,
  "positionData": [
    {
      "panelId": 1,
      "x": 1124,
      "y": 303,
      "o": 300,
      "shapeType": 0
    },
    {
      "panelId": 2,
      "x": 1124,
      "y": 389,
      "o": 0,
      "shapeType": 0
    },
    {
      "panelId": 25,
      "x": 0,
      "y": 0,
      "o": 240,
      "shapeType": 0
    },
    {
      "panelId": 26,
      "x": 299,
      "y": 433,
      "o": 60,
      "shapeType": 0
    }
  ]
}

panel_adjacency = {
    id : [adjacent panel, adjacent panel, adjacent panel]
}
'''
# def bubblesort(arr):
#     for x in range(len(arr)):
#         for i in range(len(arr)):
#             if i < len(arr) - 1 and arr[i] > arr[i + 1]:
#                 arr[i], arr[i+1] = arr[i+1], arr[i]



async def calculate_panel_adjacency(layout_object, waterfall = False, reversed = False):
    t_dict = {}
    r = None
    # edge_lengths = layout_object["sideLength"]
    # total_panels = layout_object["numPanels"]

    if waterfall:
        # return dict containing x and y values
        for l in layout_object["positionData"]:
            t_dict[l["panelId"]] = [l["x"], l["y"]]
        # sort by x, and then y where equivalent x
        x = dict(sorted(t_dict.items(), key=lambda item: ((item[1][1]) if reversed else (item[1][0], item[1][1]))))
        y = {}
        for i in x.keys():
            item = x[i][1 if reversed else 0]
            if item in y:
                y[item].append(i)
            else:
                y[item] = [i]
        r = [f for f in y.values()]
    else:
        # add x and y values
        for l in layout_object["positionData"]:
            t_dict[l["panelId"]] = l["x"] + l["y"]
        # sort by x, y sum
        r = [[i] for i in list(dict(sorted(t_dict.items(), key=lambda item: item[1])).keys())]
        print(r)

    return r