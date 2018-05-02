#judson tabor's gradebook. special thanks to johnathon de la cruz for the help
print ("grades for your classes")
chemistry_grade = input("what is your chemistry grade?")

geometry_grade = input("what is your geometry grade?")

history_grade = input("what is your whap grade?")

english_grade = input("what is your english grade?")

comp_grade = input("what is your computer grade?")

grade_list = [int(chemistry_grade),int(english_grade), int(comp_grade), int(history_grade),
              int(geometry_grade),]

listSum = sum(grade_list)
listlength = len (grade_list)
grade_average = listSum / listlength
grade_list.append(grade_average)

print (grade_list)
print ("your grade average is")
print (grade_average)
#by far the toughest thing ive ever done in coding, figuring out the average
#thx again to johnathon

if grade_average >=60 and grade_average <69:
    print ("poor grade")
    print (grade_average)
if grade_average >= 70 and grade_average <79:
    print ("ok grade")
    print (grade_average)
if grade_average >=80 and grade_average <89:
    print ("good grade")
    print (grade_average)
if grade_average >=90 and grade_average <99:
    print ("great grade")
    print (grade_average)
if grade_average >=99:
    print ("amazing grade, great job!")
    print (grade_average)
print ("thank you for entering your grades. have a nice day!")  

