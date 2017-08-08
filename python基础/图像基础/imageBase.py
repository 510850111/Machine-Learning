# -*- coding: utf-8 -*-

import cv2 as cv2
fn = "img/test1.jpg"

if __name__ == '__main__':
    print ('loading %s... ' % fn)
    img = cv2.imread(fn)
    cv2.imshow('preview...',img)
    cv2.waitKey()
    cv2.destroyAllWindows()