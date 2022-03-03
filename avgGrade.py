"""متغبر جمع نمرات """
sum = 0 
for item in range (3) : 
    """ نام درس"""   
    lessonName  = input('Enter Lesson Name :')
    """نمره درس"""    
    grade = float(input('Enter Lesson Grade :'))
    """جمع نمرات"""    
    sum += grade
"""محاسبه و چاپ معدل"""
print('Average :', sum/3)    