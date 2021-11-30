# 数据工具
import os
from xml.dom.minidom import Document

"""
生成xml文件

<annotation>
    <folder>images</folder>
    <filename>road0.png</filename>
    <size>
        <width>267</width>
        <height>400</height>
        <depth>3</depth>
    </size>
    <segmented>0</segmented>
    <object>
        <name>trafficlight</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <occluded>0</occluded>
        <difficult>0</difficult>
        <bndbox>
            <xmin>98</xmin>
            <ymin>62</ymin>
            <xmax>208</xmax>
            <ymax>232</ymax>
        </bndbox>
    </object>
</annotation>
"""


def genXml(imageSrc, imageDst, imageWidth, imageHeight, imageLabel,
           imageXmin, imageYmin, imageXmax, imageYmax):
    dir, file = os.path.split(imageSrc)
    print("路径：", dir)
    print("文件名：", file)
    doc = Document()
    annotation = doc.createElement("annotation")
    doc.appendChild(annotation)

    folder = doc.createElement("folder")
    annotation.appendChild(folder)
    folderText = doc.createTextNode("images")
    folder.appendChild(folderText)

    filename = doc.createElement("filename")
    annotation.appendChild(filename)
    filenameText = doc.createTextNode(file)
    filename.appendChild(filenameText)

    size = doc.createElement("size")
    annotation.appendChild(size)

    width = doc.createElement("width")
    size.appendChild(width)
    widthText = doc.createTextNode(imageWidth)
    width.appendChild(widthText)

    height = doc.createElement("height")
    size.appendChild(height)
    heightText = doc.createTextNode(imageHeight)
    height.appendChild(heightText)

    depth = doc.createElement("depth")
    size.appendChild(depth)
    depthText = doc.createTextNode("3")
    depth.appendChild(depthText)

    segmented = doc.createElement("segmented")
    annotation.appendChild(segmented)
    segmentedText = doc.createTextNode("0")
    segmented.appendChild(segmentedText)

    object_x = doc.createElement("object")
    annotation.appendChild(object_x)

    name = doc.createElement("name")
    object_x.appendChild(name)
    nameText = doc.createTextNode(imageLabel)
    name.appendChild(nameText)

    pose = doc.createElement("pose")
    object_x.appendChild(pose)
    poseText = doc.createTextNode("Unspecified")
    pose.appendChild(poseText)

    truncated = doc.createElement("truncated")
    object_x.appendChild(truncated)
    truncatedText = doc.createTextNode("0")
    truncated.appendChild(truncatedText)

    difficult = doc.createElement("difficult")
    object_x.appendChild(difficult)
    difficultText = doc.createTextNode("0")
    difficult.appendChild(difficultText)

    bndbox = doc.createElement("bndbox")
    object_x.appendChild(bndbox)

    xmin = doc.createElement("xmin")
    bndbox.appendChild(xmin)
    xminText = doc.createTextNode(imageXmin)
    xmin.appendChild(xminText)

    ymin = doc.createElement("ymin")
    bndbox.appendChild(ymin)
    yminText = doc.createTextNode(imageYmin)
    ymin.appendChild(yminText)

    xmax = doc.createElement("xmax")
    bndbox.appendChild(xmax)
    xmaxText = doc.createTextNode(imageXmax)
    xmax.appendChild(xmaxText)

    ymax = doc.createElement("ymax")
    bndbox.appendChild(ymax)
    ymaxText = doc.createTextNode(imageYmax)
    ymax.appendChild(ymaxText)

    filename = str(file).split(".")[0]
    filename = filename + ".xml"
    f = open(imageDst + filename, "w")
    f.write(doc.toprettyxml(indent="  "))
    f.close()
    f = open(imageDst + filename, 'r')
    lines = f.readlines()
    f.close()
    f = open(imageDst + filename, 'w')
    f.write(''.join(lines[1:]))
    f.close()


if __name__ == '__main__':
    print("----")
    genXml("/Users/ruanchenhao/Downloads/w/data/original/images/1109.jpg",
           "/Users/ruanchenhao/Downloads/w/data/original/",
           "100", "100", "jay", "0", "0", "0", "0")

    # aa = str("1109.jpg").split(".")[0]
    # print(aa)

# def genXml(images_path, xmls_path):
#     src_paths = getPaths(images_path)
#     dst_path = xmls_path
#     for image in src_paths:
#         dir, file = os.path.split(image)
#         print("文件名：", file)
#         doc = Document()
#         annotation = doc.createElement("annotation")
#         doc.appendChild(annotation)
#
#         folder = doc.createElement("folder")
#         annotation.appendChild(folder)
#         folderText = doc.createTextNode("desktop")
#         folder.appendChild(folderText)
#
#         filename = doc.createElement("filename")
#         annotation.appendChild(filename)
#         filenameText = doc.createTextNode(file)
#         filename.appendChild(filenameText)
#
#         path = doc.createElement("path")
#         annotation.appendChild(path)
#         pathText = doc.createTextNode(image)
#         path.appendChild(pathText)
#
#         source = doc.createElement("source")
#         annotation.appendChild(source)
#         database = doc.createElement("database")
#         source.appendChild(database)
#         databaseText = doc.createTextNode("Unknown")
#         database.appendChild(databaseText)
#
#         size = doc.createElement("size")
#         annotation.appendChild(size)
#
#         width = doc.createElement("width")
#         size.appendChild(width)
#         widthText = doc.createTextNode("130")
#         width.appendChild(widthText)
#
#         height = doc.createElement("height")
#         size.appendChild(height)
#         heightText = doc.createTextNode("155")
#         height.appendChild(heightText)
#
#         depth = doc.createElement("depth")
#         size.appendChild(depth)
#         depthText = doc.createTextNode("3")
#         depth.appendChild(depthText)
#
#         segmented = doc.createElement("segmented")
#         annotation.appendChild(segmented)
#         segmentedText = doc.createTextNode("0")
#         segmented.appendChild(segmentedText)
#
#         object_x = doc.createElement("object")
#         annotation.appendChild(object_x)
#
#         name = doc.createElement("name")
#         object_x.appendChild(name)
#         nameText = doc.createTextNode("JayZhou")
#         name.appendChild(nameText)
#
#         pose = doc.createElement("pose")
#         object_x.appendChild(pose)
#         poseText = doc.createTextNode("Unspecified")
#         pose.appendChild(poseText)
#
#         truncated = doc.createElement("truncated")
#         object_x.appendChild(truncated)
#         truncatedText = doc.createTextNode("1")
#         truncated.appendChild(truncatedText)
#
#         difficult = doc.createElement("difficult")
#         object_x.appendChild(difficult)
#         difficultText = doc.createTextNode("0")
#         difficult.appendChild(difficultText)
#
#         bndbox = doc.createElement("bndbox")
#         object_x.appendChild(bndbox)
#
#         xmin = doc.createElement("xmin")
#         bndbox.appendChild(xmin)
#         xminText = doc.createTextNode("1")
#         xmin.appendChild(xminText)
#
#         ymin = doc.createElement("ymin")
#         bndbox.appendChild(ymin)
#         yminText = doc.createTextNode("1")
#         ymin.appendChild(yminText)
#
#         xmax = doc.createElement("xmax")
#         bndbox.appendChild(xmax)
#         xmaxText = doc.createTextNode("129")
#         xmax.appendChild(xmaxText)
#
#         ymax = doc.createElement("ymax")
#         bndbox.appendChild(ymax)
#         ymaxText = doc.createTextNode("154")
#         ymax.appendChild(ymaxText)
#
#         filename = file.replace('.jpg', '.xml')
#         f = open(dst_path + filename, "w")
#         f.write(doc.toprettyxml(indent="  "))
#         f.close()
#         f = open(dst_path + filename, 'r')
#         lines = f.readlines()
#         f.close()
#         f = open(dst_path + filename, 'w')
#         f.write(''.join(lines[1:]))
#         f.close()
