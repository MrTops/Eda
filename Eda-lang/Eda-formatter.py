def format_file(file_loc):
	"""
	Takes in a file location and loads it into a form eda can run
	This tool is useful if you'd rather not mess with formatting
	
	if the file doesn't exist it will return []
	"""
	try:
		file_content = open(file_loc, "r").readlines()
	except:
		return []
	
	toReturn = []
	for line in file_content:
		toReturn.append(line.rstrip("\n"))
	return toReturn