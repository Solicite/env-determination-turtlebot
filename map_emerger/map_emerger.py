#!/usr/bin/env python
# -*-coding:Utf-8 -*

import numpy as np
from PIL import Image
import glob,os


def scan_files(directory,postfix=None,prefix=None):
  files_list=[]

  for root, sub_dirs, files in os.walk(directory):
    for special_file in files:
      if postfix:
        if special_file.endswith(postfix):
          files_list.append(os.path.join(root,special_file))
      elif prefix:
        if special_file.startswith(prefix):
          files_list.append(os.path.join(root,special_file))
      else:
        files_list.append(os.path.join(root,special_file))

  return files_list

def map_emerge(directory, image_type):
    image_list_path = scan_files(directory, image_type)

    image_list =[]
    for image_path in image_list_path:
        image_list.append(Image.open(image_path))


    baseimg = image_list[0]
    sz = baseimg.size
    basemat = np.atleast_2d(baseimg)

    for i in range(1, len(image_list)):
        image = image_list[i]
        image = image.resize(sz,Image.ANTIALIAS)
        mat=np.atleast_2d(image)
        print(file)
        basemat=np.append(basemat,mat,axis=0)

    final_img=Image.fromarray(basemat)
    final_img.save("../merged.png")

    return final_img

if __name__ == "__main__":
    map_emerge("./", ".png").show()
