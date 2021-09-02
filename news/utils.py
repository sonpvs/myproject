import matplotlib.pyplot as plt
import seaborn as sns  
from io import BytesIO  
import base64  


def get_image(): 
	# create a bytes buffer for the image to save 
	abc = BytesIO() 
	# create the plot with the use of BytesI0 object as its ‘file’ 
	plt.savefig(abc, format='png') 
	# set the cursor the begining of the stream 
	abc.seek(0) 
	# retreive the entire content of the ‘file’ 
	image_png = abc.getvalue() 
	graph = base64.b64encode(image_png) 
	graph = graph.decode('utf-8') 
	# free the momory of the buffer 
	abc.close() 
	return graph



def get_simple_plot(chart_type, *args, **kwargs):
	# https://matplotlib.org/fagq/usage_faq.html?highlight=backend#what-is—a-backend 
	plt.switch_backend('AGG') 
	fig = plt.figure(figsize=(10,4)) 
	x = kwargs.get('x') 
	y = kwargs.get('y') 
	data = kwargs.get('data') 

	if chart_type == 'bar plot':
		title = "title"
		plt.title(title)
		plt.bar(x, y)
	elif chart_type == 'line plot':
		title = "title" 
		plt.title(title) 
		plt.plot(x, y) 
	else: 
		title = "title" 
		plt.title(title)
		sns.countplot(x="gioitinh", hue="hocvan", data=data) 

	plt.tight_layout()
	graph = get_image() 
	return graph
