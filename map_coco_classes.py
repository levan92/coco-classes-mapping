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
print('80 map to 91')
print(small2large)

large2small = {v:k for k,v in small2large.items()}
print('91 map to 80')
print(large2small)

with open('coco_mapping_80to91.json','w') as f:
    json.dump(small2large, f)
with open('coco_mapping_91to80.json','w') as f:
    json.dump(large2small, f)
