class BestCourse:
    #instance variable
    website="http://uiu.ac.bd"

    def __init__(self, name):
        self.name =  name


spl = BestCourse("Structure Programming Language")
apl = BestCourse("Advanced Programming Language")

print(spl.name)
print(BestCourse.website)

        