import pandas as pd
midx = pd.MultiIndex(levels=[      ['deer','dog','eagle'],
                                   ['speed','weight','length']     ],
                     codes=[    [0,0,0,1,1,1,2,2,2],                   
                                [0,1,2,0,1,2,0,1,2]         ])
midx
df=pd.DataFrame(index=midx,  columns=['big','small'] , data=[[10,10],[20,20],[30,30],[40,40],[50,50],[60,60],[70,70],[80,80],[90,90]])
df
