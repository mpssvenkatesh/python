import pickle


# PICKLING
"""
data = {'Name':'Kevin', 'Age':30, 'City':'Trumbull', 'Contact':'222-333-8888'}

pickleOut = open('data.pickle', 'wb')

pickle.dump(data, pickleOut)

pickleOut.close()
"""

# Unpickling

pickleIn = open('data.pickle', 'rb')

data = pickle.load(pickleIn)

print(data)

pickleIn.close()
