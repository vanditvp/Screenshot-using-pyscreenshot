

import pyscreenshot 


image = pyscreenshot.grab(bbox=(10, 10, 500, 500)) 


image.show() 

image.save("screenshot1.png") 
