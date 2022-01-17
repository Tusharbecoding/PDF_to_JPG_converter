from pdf2image import convert_from_path


# Storing Pdf with convert_from_path function
images = convert_from_path('pdf_name.pdf')

for i in range(len(images)):

	# Saving pages as images
	images[i].save('page'+ str(i) +'.jpg', 'JPEG')
