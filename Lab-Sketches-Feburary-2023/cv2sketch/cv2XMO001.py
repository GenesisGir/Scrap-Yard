"""
🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 

█▀█ █▀█ █▀▀ █▄░█   █▀ █▀█ █░█ █▀█ █▀▀ █▀▀   █▀▀ █▀█ █▀▄▀█ █▀█ █░█ ▀█▀ █▀▀ █▀█   █░█ █ █▀ █ █▀█ █▄░█   ▄▀ █▀▀ █░█ ▀█ ▀▄
█▄█ █▀▀ ██▄ █░▀█   ▄█ █▄█ █▄█ █▀▄ █▄▄ ██▄   █▄▄ █▄█ █░▀░█ █▀▀ █▄█ ░█░ ██▄ █▀▄   ▀▄▀ █ ▄█ █ █▄█ █░▀█   ▀▄ █▄▄ ▀▄▀ █▄ ▄▀ 

displays images implementing opencv.

🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂
"""

# import modules
import cv2 as cv

img = cv.imread(filename=r'Scrap-Yard\Lab-Sketches-Feburary-2023\deepfacesketches\images\robbie.jpg')
cv.imshow(winname='some image idk', mat=img)
cv.waitKey(0)