class Animal2:

    def __init__(self, name, features,communicate):  
        self.name =name
        self.features =features
        self.communicate =communicate
        print(self.name, self.features)
    

    def communincate(self):
        print(f'the {self.name} {self.communicate}')
        
    def  food(self, food_item):
        print(f'{self.name} would like to eat {food_item}')


    def birthday(self):
        print('happy Birthday')


