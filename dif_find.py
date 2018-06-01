from PIL import Image, ImageDraw 
#img1 - your first image
img1 = Image.open("img1.jpg") 
#img2 - your second image
img2 = Image.open("img2.jpg") 
p_set1 = img1.load() 
p_set2 = img2.load() 
ans=Image.open("img2.jpg") 
width = min(img1.size[0], img2.size[0]) 
height = min(img1.size[1], img2.size[1]) 
for i in range(width): 
	for j in range(height): 
		r=p_set1[i,j][0]-p_set2[i,j][0]
		g=p_set1[i,j][1]-p_set2[i,j][1] 
		b=p_set1[i,j][2]-p_set2[i,j][2]
		#Constants may be changed, it depends on the image
		if(abs(r)>80  or abs(g)>80  or abs(b)>80 ):
			#every 7th point, which has difference of colors greater then given constant will be highlited 
			if(i % 7==0 and j%7==0):

				ImageDraw.Draw(ans).ellipse((i, j, i + 7, j + 7), fill = (0, 0, 0))

#the result is saved as dif.jpg file			
ans.save("dif.jpg", "JPEG")
