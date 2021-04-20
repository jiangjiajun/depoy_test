import sys
import numpy as np

py_result = list()
with open(sys.argv[1]) as f:
    for line in f:
        if not line.strip().startswith('Box('):
            continue
        line = line.strip()[4:-1]
        items = line.strip().split('\t')
        py_result.append(items)

cpp_result = list()
with open(sys.argv[2]) as f:
    for line in f:
        if not line.strip().startswith('Box('):
            continue
        line = line.strip()[4:-1]
        items = line.strip().split('\t')
        cpp_result.append(items)

assert len(py_result) == len(cpp_result), "Python Result Length: {} vs CPP Result Length: {}".format(len(py_result), len(cpp_result))

for i in range(len(py_result)):
    cid1, label1, score1, xmin1, ymin1, w1, h1 = py_result[i]
    cid2, label2, score2, xmin2, ymin2, w2, h2 = cpp_result[i]
    
    assert cid1 == cid2, "result_{} cid {} vs {}".format(i, cid1, cid2)
    assert label1 == label2, "result_{} label {} vs {}".format(i, label1, label2)

    score1 = float(score1)
    xmin1 = float(xmin1)
    ymin1 = float(ymin1)
    w1 = float(w1)
    h1 = float(h1)

    score2 = float(score2)
    xmin2 = float(xmin2)
    ymin2 = float(ymin2)
    w2 = float(w2)
    h2 = float(h2)

    abs_diff = np.fabs(score2 - score1)
    rel_diff = abs_diff / np.fabs(max(score2, score1))
    if abs_diff < 5e-03:
        continue
    if rel_diff < 5e-03:
        continue
    print(abs_diff, rel_diff)
    print(py_result[i])
    print(cpp_result[i])
    raise Exception("result_{} score not pass".format(i))

   
    abs_diff = np.fabs(xmin2 - xmin1)
    rel_diff = abs_diff / np.fabs(max(xmin2, xmin1))
    if abs_diff < 1e-03:
        continue
    if rel_diff < 1e-03:
        continue
    print(abs_diff, rel_diff)
    print(py_result[i])
    print(cpp_result[i])
    raise Exception("result_{} xmin not pass".format(i))

    abs_diff = np.fabs(ymin2 - ymin1)
    rel_diff = abs_diff / np.fabs(max(ymin2, ymin1))
    if abs_diff < 1e-03:
        continue
    if rel_diff < 1e-03:
        continue
    print(abs_diff, rel_diff)
    print(py_result[i])
    print(cpp_result[i])
    raise Exception("result_{} ymin not pass".format(i))

    abs_diff = np.fabs(w2 - w1)
    rel_diff = abs_diff / np.fabs(max(w2, w1))
    if abs_diff < 1e-03:
        continue
    if rel_diff < 1e-03:
        continue
    print(abs_diff, rel_diff)
    print(py_result[i])
    print(cpp_result[i])
    raise Exception("result_{} w not pass".format(i))

    abs_diff = np.fabs(h2 - h1)
    rel_diff = abs_diff / np.fabs(max(h2, h1))
    if abs_diff < 1e-03:
        continue
    if rel_diff < 1e-03:
        continue
    print(abs_diff, rel_diff)
    print(py_result[i])
    print(cpp_result[i])
    raise Exception("result_{} h not pass".format(i))
print("Diff Pass! " )
