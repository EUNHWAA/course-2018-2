import sys

srcFileName=sys.argv[1]
objFileName=sys.argv[2]

srcFileHandle=open(srcFileName,'r')
tabtxt= srcFileHandle.read()
srcFileHandle.close()

spacetxt=tabtxt.replace("\t"," "*4)

objFileHandle=open(objFileName,'w')
objFileHandle.write(spacetxt)
objFileHandle.close()







