import numpy as np

type = np.dtype([('Title', 'S50'), ('Price', np.float_)])
arr = np.array([], dtype=type)

with open('Chiba.csv', 'r') as handle:
    for line in handle:
        line = line.split(',')
        line[1] = line[1].split()
        if len(line[1]) > 1:
            title = line[0][:-1]
            price = float(line[1][0])
            info = np.array([(title, price)], dtype = type)
            arr = np.concatenate((arr, info))
arr = arr.reshape(19,1)
print(arr.ndim)
