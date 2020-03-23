import json
classes_80_txt = './coco80.names'
classes_91_txt = './coco91.names'
manual_mapping = {'motorbike':'motorcycle',
                  'aeroplane':'airplane',
                  'sofa':'couch',
                  'pottedplant': 'potted plant',
                  'diningtable':'dining table',
                  'tvmonitor':'tv'
                 }
with open(classes_80_txt,'r') as f:
    lines80 = f.readlines()
with open(classes_91_txt,'r') as f:
    lines91 = f.readlines()

classes91 = []
for cl in lines91:
    classes91.append(cl.strip())

small2large = {}
for small_i, cl in enumerate(lines80):
    cl = cl.strip()
    if cl in manual_mapping:
        cl = manual_mapping[cl]
    small2large[small_i+1] = classes91.index(cl) + 1

print(small2large)
with open('coco_mapping.json','w') as f:
    json.dump(small2large, f)
