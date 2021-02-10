MultiIndex:Pandas MultiIndex.to_frame() function create a DataFrame with the levels of the MultiIndex as columns.

import pandas as pd
midx = pd.MultiIndex(levels=[      ['deer','dog','eagle'],
                                   ['speed','weight','length']     ],
                     codes=[    [0,0,0,1,1,1,2,2,2],                   
                                [0,1,2,0,1,2,0,1,2]         ])
df=pd.DataFrame(index=midx,  columns=['big','small'] , data=[[10,10],[20,20],[30,30],[40,40],[50,50],[60,60],[70,70],[80,80],[90,90]])
O/P
		big	small
deer	speed	10	10
weight	20	20
length	30	30
dog	speed	40	40
weight	50	50
length	60	60
eagle	speed	70	70
weight	80	80
length	90	90
