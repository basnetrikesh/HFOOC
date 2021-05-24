############## KEYBOARD VARIABLES ##############
# KEYBOARD SETTING/VARIABLES: 
first_col_index=[0,10,20,30,40,50]
second_col_index=[1,11,21,31,41,51]
third_col_index=[2,12,22,32,42,52]
fourth_col_index=[3,13,23,33,43,53]
fifth_col_index=[4,14,24,34,44,54]
sixth_col_index=[5,15,25,35,45,55]
seventh_col_index=[6,16,26,36,46,56]
eighth_col_index=[7,17,27,37,47,57]
ninth_col_index=[8,18,28,38,48,58]
tenth_col_index=[9,19,29,39,49,59]
key_set={0:"1",1:"2",2:"3",3:"4",4:"5",5:"6",6:"7",7:"8",8:"9",9:"0",
            10:"q",11:"w",12:"e",13:"r",14:"t",15:"y",16:"u",17:"i",18:"o",19:"p",
            20:"a",21:"s",22:"d",23:"f",24:"g",25:"h",26:"j",27:"k",28:"l",29:";",
            30:"z",31:"x",32:"c",33:"v",34:"b",35:"n",36:"m",37:"<",38:">",39:"?",
            40:"+",41:"-",42:",",43:".",44:"/",45:"*",46:"@",47:" ",48:"!",49:"<-",
            50:"%",51:"$",52:":",53:"&",54:"(",55:")",56:"=",57:"_",58:"'",59:"#",}
#counters
#this is frame count for column
frame_count_column=0
#this is frame count for row
frame_count_row=0 
#this is to store column_index to activate
col_index=[]
#initially column 0 is active/selected
col=0
#this for couting the blink (used for blink for changing the row and column)
blink_count=0 
#this is for counting the blink to check whether the key should press or not
blink_count_indivisual_key=0 
#this is for entering inside particular column 
col_select=False 
#this is to count the row after particular column is selected
row=0 
#this is to store the typed character 
type_text="" 

#mouth open count used to switch form mouse to keyboard and from keyboard to mouse
mouth_open=0

################ MODEL VARIABLES ###############
IMG_SIZE=(34,26)



