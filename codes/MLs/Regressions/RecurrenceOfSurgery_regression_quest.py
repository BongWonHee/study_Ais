import os
import pickle
file_path = 'datasets/RecurrenceOfSurgery_regression_quest.plk'

if os.path.exists(file_path) :

    Sugery_time = float(input('수술시간 : '))
    Hospitalization_period = int(input('입원기간 : '))



    with open (file_path,'rb') as regression_file :
        loaded_model = pickle.load(regression_file)
        input_labels = [[Sugery_time,Hospitalization_period]]
        regression_predict = loaded_model.predict(input_labels)
        print('Age Result : {}'.format(regression_predict))
else :
    print('file not found!!')