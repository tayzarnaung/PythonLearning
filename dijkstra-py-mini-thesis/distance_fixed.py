graph = {
    'a':{'b':3,'c':1},
    'b' : {'a':3,'c':7, 'd':5, 'e':1},
    'c': {'a':1, 'b':7, 'd':2},
    'd': {'b':5, 'c':2, 'e':7},
    'e': {'b':1, 'd':7}
}


dictionary = {
'Sule': { 'Sule Myodaw Hall': 0.277987317, 'Pan Soe Tan': 0.308944496}, 
'Sule Myodaw Hall': {'Sule':0.277987317, 'Yoke Shin Yone': 0.267080093,  'Bar Lan': 0.319386564}, 
'Yoke Shin Yone': {'Sule Myodaw Hall': 0.267080093, 'Youk Lan': 0.445289046, 'Pan Soe Tan2': 0.319575954}, 
'Youk Lan': { 'Yoke Shin Yone':0.445289046, 'Pan Soe Tan2':0.52622915905828, 'Youk Lann': 0.401209158, 'Youk Lan 2': 0.217517123}, 
'Youk Lann': { 'Youk Lan':0.401209158, 'Kyauk Taing': 0.309336351},
'Youk Lan 2': {'Youk Lan':0.217517123, 'Kyauk Taing': 0.486675035}, 
'Kyauk Taing': {'U Htaung Bo': 0.757996616, 'Youk Lann':0.309336351, 'Youk Lan 2':0.486675035}, 
'U Htaung Bo': { 'Kyauk Taing':0.757996615751393,'Taung Phat Mote': 0.670646109, 'Kan Yeik Thar': 0.646248473}, 
'Taung Phat Mote': {'A Shae Phat Mote': 0.385173739, 'U Htaung Bo':0.670646109}, 
'A Shae Phat Mote': {'Taung Phat Mote': 0.385173739}, 
'Pan Soe Tan': {'Sule': 0.308944496,'Bar Lan': 0.267080098}, 
'Bar Lan': {'Sule Myodaw Hall': 0.319386564,'Pan Soe Tan2': 0.278191101}, 
'Pan Soe Tan2': {'Youk Lan':0.52622915905828,'Yoke Shin Yone': 0.319575954, 'Kan Yeik Thar': 1.569149041}, 
'Kan Yeik Thar': {'U Htaung Bo': 0.646248473}
} 

# for i in range(10):
#     # print (i)