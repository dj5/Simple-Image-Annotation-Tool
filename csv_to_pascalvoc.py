import pandas as pd

import xml.etree.ElementTree as ET
import os


def csv_to_pascalvoc(path):
    fields = ['Filename', 'x1', 'y1', 'x2', 'y2','classname']
    
    df = pd.read_csv(os.path.join(path,'data.csv'), usecols=fields)
    os.chdir(path)
    try:
     os.mkdir("Annotations")
    except:
     path=os.path.join(path,"Annotations")

     for i in range(0, len(df.Filename)):
        height = int(df['y2'].iloc[i])-int(df['y1'].iloc[i])
        width = int(df['x2'].iloc[i])-int(df['x1'].iloc[i])
        depth = 3
        #print(str(df['Filename'].iloc[i].split("/")))
     
        annotation = ET.Element('annotation')
        ET.SubElement(annotation, 'folder').text = df['Filename'].iloc[i].replace(df['Filename'].iloc[i].split("/")[-1],"").split("/")[-2]
        ET.SubElement(annotation, 'filename').text = df['Filename'].iloc[i].split("/")[-1]
        ET.SubElement(annotation, 'path').text = df['Filename'].iloc[i]
        ET.SubElement(annotation, 'segmented').text = '0'
        size = ET.SubElement(annotation, 'size')
        ET.SubElement(size, 'width').text = str(width)
        ET.SubElement(size, 'height').text = str(height)
        ET.SubElement(size, 'depth').text = str(depth)
        ob = ET.SubElement(annotation, 'object')
        ET.SubElement(ob, 'name').text = df['classname'].iloc[i]
        ET.SubElement(ob, 'pose').text = 'Unspecified'
        ET.SubElement(ob, 'truncated').text = '0'
        ET.SubElement(ob, 'difficult').text = '0'
        bbox = ET.SubElement(ob, 'bndbox')
        ET.SubElement(bbox, 'xmin').text = str(df['x1'].iloc[i])
        ET.SubElement(bbox, 'ymin').text = str(df['y1'].iloc[i])
        ET.SubElement(bbox, 'xmax').text = str(df['x2'].iloc[i])
        ET.SubElement(bbox, 'ymax').text = str(df['y2'].iloc[i])

        fileName = str(df['Filename'].iloc[i].split("/")[-1])
        fileName= fileName.replace("jpeg","xml") if "jpeg" in fileName else fileName.replace(fileName[-3:],"xml")
        tree = ET.ElementTree(annotation)
        tree.write(os.path.join(path,fileName) ,encoding='utf8')
