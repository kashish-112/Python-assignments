text = "X-DSPAM-Confidence:    0.8475"

#find the position of 0
nu = text.find("0")

#from the info found earlier using find()print the required value in float type
print(float(text[23:30]))