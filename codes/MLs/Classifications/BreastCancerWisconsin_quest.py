import os
import pickle

file = 'datasets/BreastCancerWisconsin_Regression.plk'

if os.path.exists(file) :

    area = float(input('area_worst : '))
    smoothness = float(input('smoothness_worst : '))
    compactness = float(input('compactness_worst : '))

    with open (file,'rb') as BCW_file :
        load_model = pickle.load(BCW_file)
        input_labels = [[area,smoothness,compactness]]
        regression_predict = load_model.predict(input_labels)
        print('diagnosis : {}'.format(regression_predict))
else :
    print('file no found!!')