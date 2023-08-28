texture_mean = float(input('texture_mean : '))
perimeter_mean = float(input('perimeter_mean : '))

import pickle

with open ('datasets/BreastCancerWisconsin_Regression.pkl','rb') as regression_file :
    loaded_model = pickle.load(regression_file)
    input_labels = [[texture_mean,perimeter_mean]]
    result_predict = loaded_model.predict(input_labels)
    print('Predict radius_mean Result : {}'.format(result_predict))
    pass
