class Game1:
    def __init__(self):
        while True:
            print('''
                   1:Welcome In our Game
                   2:even_odd_list Game
                   3:Count word Game
                   4:print numbers form 0 to enter number Game
                   5:divisibility on number2 Game
                   6:divisibility on number1 and number2 from(0,100) Game
                   7:choice X to exit ''')
               
            user_choice=int(input('Enter Number Of Game'))
            if user_choice==2:
                  print(self.towlist([1,2,3,4,5,6,7,8,9]))
                 
            
            elif user_choice==3:
                 word=input('Enter your sentance')
                 self.count_word(word)

            elif user_choice==4:
                number=int(input('Enter End number'))
                self.print_numbers(number)
                
            elif user_choice==5:
                number1=int(input('Enter first number'))
                number2=int(input('Enter second number'))
                self.divi_number2(number1,number2)

            elif user_choice==6:
                number1=int(input('Enter first number'))
                number2=int(input('Enter second number'))
                self.divi_number2_number2(number1,number2)



            play_again=input('choice any key to play again or press x to exit')      
            if play_again=='x':
                break



    


    def towlist(self,list1):
        global list_odd
        global list_even

    
        list_odd=[]
        list_even=[]
        for i in list1:
            if i%2==0:
                list_even.append(i)
            else:
                list_odd.append(i)

        return list_even ,list_odd
    

    def count_word(self,word):

        list1=word.split()
        print(len(set(list1)))





    def print_numbers(self,number):
        for i in range(number+1 ):
            print(i)


    def divi_number2(self,number1,number2):
        for i in range(number1+1):
            if i%number2==0:
                print(i)
        

    def divi_number2_number2(self,number1,number2):
        for i in range(101):
            if i%number1==0 and i%number2==0:
                print(i)

        


g=Game1()





        

            
