import pandas as pd
import matplotlib.pyplot as plt

import numpy as np

PetInfo =pd.read_csv('/Users/paulcarson/Documents/DogData.csv', delimiter = ',')
PetInfo.head()



#let's drop duplicate IDs and create a new variable, then graph for the sized
UniqueID = PetInfo.drop_duplicates(subset=['PetID'])
UniqueID['Size'].value_counts().plot(kind='barh')
plt.show()
# and take a look at count by shelter
UniqueID['Shelter'].value_counts().plot(kind='bar', color = 'Green')
plt.show()

PetInfo = PetInfo.loc[:, ~PetInfo.columns.str.contains('^Unnamed')]

PetInfo['YearsOld'] = PetInfo.Age.str.extract('(\d+)')

#drop duplicate ids
UniqueID = PetInfo.drop_duplicates(subset=['PetID'])

#look at count of years old
UniqueID['YearsOld'].value_counts().plot(kind='bar', color='Green')
plt.show()

#look at counts by shelter
UniqueID['Shelter'].value_counts().plot(kind='bar', color='Green')
plt.show()

#new pets by day...need to figure out how to specifify after first date
NetNewAdds = UniqueID.groupby([UniqueID['Date Added']])['PetID'].count()
NetNewAdds.plot(kind='bar', figsize=(10,5), legend=None)
plt.show()


AvailableByDay = PetInfo.groupby([PetInfo['Date Added']])['PetID'].count()
AvailableByDay.plot(kind='barh',figsize=(10,5),legend=None)
plt.show()







