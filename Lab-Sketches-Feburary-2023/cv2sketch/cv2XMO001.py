"""
🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 

█▀█ █▀█ █▀▀ █▄░█   █▀ █▀█ █░█ █▀█ █▀▀ █▀▀   █▀▀ █▀█ █▀▄▀█ █▀█ █░█ ▀█▀ █▀▀ █▀█   █░█ █ █▀ █ █▀█ █▄░█   ▄▀ █▀▀ █░█ ▀█ ▀▄
█▄█ █▀▀ ██▄ █░▀█   ▄█ █▄█ █▄█ █▀▄ █▄▄ ██▄   █▄▄ █▄█ █░▀░█ █▀▀ █▄█ ░█░ ██▄ █▀▄   ▀▄▀ █ ▄█ █ █▄█ █░▀█   ▀▄ █▄▄ ▀▄▀ █▄ ▄▀ 

some fucking script implementing opencv.

🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂
"""

# import modules
import cv2 as cv

img = cv.imread(filename=r'Scrap-Yard\Lab-Sketches-Feburary-2023\cv2sketch\imagesources\marnie.jpg')

cv.imshow(winname='marnie', mat=img)

cv.waitKey(0)