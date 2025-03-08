#Michele Mora
#03/04/2025
#CIS129_Module_5_lab
#Lab 5 The Bottle Return Program

def main():  # defining main function
    next_data = 'y' # declaring next_data vaiable as y
    while(next_data =='y'): # while loop until user enters n
        i = 0 # declaring i=0
        sum = 0 # declaring sum as 0
        while(i<7): # while loop to read 7 days bottle data
            print('Enter the bottle for day #',i+1,':',end='')
            sum+=int(input())
            i+=1
        print('The total number of bottles collected is ',sum)
        print('The total paid out is $ ',sum/10)
        print('Do you want to enter another week’s worth of data?')
        next_data=str(input('(Enter y or n):'))


main()


