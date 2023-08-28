Sugery_time = float(input('수술시간 : '))
Hospitalization_period = int(input('입원기간 : '))

import pickle

with open ('datasets/RecurrenceOfSurgery_regression_quest.plk','rb') as regression_file :
    loaded_model = pickle.load(regression_file)
    input_labels = [[Sugery_time,Hospitalization_period]]
    regression_predict = loaded_model.predict(input_labels)
    print('Age Result : {}'.format(regression_predict))