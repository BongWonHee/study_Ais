py_list = [[1,2]
          ,[3,5]
          ,[5,6]] #list

import numpy as np

np_array = np.array([[7,8]
                    ,[9,10]
                    ,[11,12]]) # 행렬 = array
# np.mean(np_array)
# 9.5 전체평균
# np.mean(np_array, axis = 0)
# array([ 9., 10.]) # 열단위 평균
# np.mean(np_array, axis = 1)
# array([ 7.5,  9.5, 11.5]) # 행단위 평균

# 병합
np_array02 = np.array(py_list)
# np.concatenate((np_array, np_array02), axis = 0) #열단위 병합
# array([[ 7,  8],
#        [ 9, 10],
#        [11, 12],
#        [ 1,  2],
#        [ 3,  5],
#        [ 5,  6]])
# np.concatenate((np_array, np_array02), axis = 1) #행단위 병합
# array([[ 7,  8,  1,  2],
#        [ 9, 10,  3,  5],
#        [11, 12,  5,  6]])

pass