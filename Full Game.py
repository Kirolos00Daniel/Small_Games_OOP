class Game():

    def __init__(self):
        print('Welcome To Full Game ^_^......')
        print('Choose your Game From our Collections')
        print('Press[1]: Even-Odd Game')
        print('Press[2]: Sum-Average Game')
        print('Press[3]: Multiplication Game')
        print('Press[4]: Finding Nemo Game')
        

        self.Choices()

    def Choices(self):
        while True:
            user_choice = input('Enter Your Choice :')
        
            try:
               user_choice= int(user_choice)
               if user_choice == 1 :
                    self.Even_Odd_Game()
               elif user_choice == 2 :
                    self.Sum_Average_Game()
               elif user_choice == 3 :
                    self.Multiplication_Game()
               elif user_choice == 4 :
                    self.Finding_nemo_Game()    
               else:
                    print('Choose from 1, 2, 3 and 4')
            except ValueError:
                   print('Enter A Valid Number')
            



    def Even_Odd_Game(self):
        print('Welcome To The Even Odd Game')
        print('I will Tell You If the Number Is Even Or Odd')
        print('If You Wanna to Leave the Game Enter X')

        while True:
            Number = input( 'Enter Your Number:')
            
            if Number == 'x':
                print('Closing The Game')
                print('Thanks For Playing ...')
                break    

            try:    
                Number = int(Number)
                if Number % 2 == 0:
                   print('Even Number')
                else:
                   print('Odd Number')
                
            except ValueError:
                print('Enter A Valid Number')

            print('--------------')    



    def Sum_Average_Game(self):
        print('This Game will take Severals Numbers and print the Average Of Them')
        count= int(input('Enter the Numbers you want to count :'))

        count_number = 0
        summ = 0

        while count_number < count:
            number= float(input('Enter The Number :'))
            count_number += 1
            summ += number
            
        print('Your Sum is :',summ)
        print('Your Average is :', summ/count)




    def Multiplication_Game(self):
        print('Welcome To The Multiplication Game')
        print('Please Enter The First and The Last Number of the Mutliplcation Table')

        start=int(input('Enter The First Number :'))
        end=int(input('Enter The Last Number :'))          


        for x in range(start,end+1):
                for y in range(1,13):
                    print(x, 'X', y, '=',x*y)
                print('======================')

     def Finding_nemo_Game(self):
         
         print('welcome to finding nemo game')
         print('if you want to exict the game press [0]')

         fish = input('fish type :')
         color= input('fish color :')

         while True:
                print(color +' '+fish+' '+'There')

                break
                
         




Game2= Game()
