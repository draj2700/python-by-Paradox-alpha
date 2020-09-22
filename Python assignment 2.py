DHEERAJ PARGAI
9837488468


que.1- You are an employer in a company which have a web
       application for which you have to develop a calculator.
       Write a program to design a calculator in which you 
       have to give some scientific function like comparing two
       numbers and find the smaller and greater one as well.

Ans.   num1=int(input("enter any number"))
       num2=int(input("enter any number again"))
       print("sum=",num1+num2)
       print("subtraction=",num1-num2)
       print("multiply=",num1*num2)
       print("division=",num1/num2)
       print("num1 is equals to num2",num1==num2)
       print("num1 is greater then num2",num1>num2)

que.2- One girl named as Chandni, have to write a paragraph
       but by mistake she wrote some letters in upper
       and some in lower case. Now she wants to arrange
       them in a grammatical manner as capital letter after 
       every specific symbol like comma, full stop, etc. and 
       rest in lower case. Write a program to help her out.

Ans.   s="amit is here, and you. are you there"
       print(s.title())


que.3- You are an employer in a company, HR gives you a task 
       to mail a document. You want to find one word and 
       also count how many times it came in document.
             {HINT-assume the data as a paragraph of your choice.}

Ans.   mail="Although you do not expect your employees to work beyond the usual working hours, a humble note of thanks will encourage your employees. They will realise that their hard work’s been noticed by the company, making them want to work harder and contribute in more ways.This is a commonly used template to thank employees for the job when done well. This letter is an effective way to appreciate the job well done by your employees."
       print(mail.find("employees"))
       print(mail.count("employees"))


que.4- There is a girl wants to write autobiography of her 
       favorite player. She writes a paragraph for that but
       missed some words. Now help her to add those words.
             {HINT-use format of function data(autobiography)of your choice.}

Ans.   msd="Mahendra Singh Dhoni born in 7 July {}, commonly known as M. S. Dhoni and {}, is a cricket player and was the former captain of the Indian cricket team. Dhoni is a {} -handed batsman. He is known as the greatest captain of all time, having achieved more success than any other captain in the history of cricket."
       print(msd.format(1981,"Mahi","right"))


que.5- Explain standard data types in detail with example.

Ans.   STANDARD DATATYPES-
        
       A Data Type describes the characteristic of a variable. Python has six standard Data Types which are divided into two groups -

       Immutable - values can not change once assigned to a variable . Numbers,string and tuples are immutable datatypes.

       Mutable - values can be change using some functions . Lists, dictionary and sets are mutable datatypes.

       1.Numeric -
                  Python numeric data type is used to hold numeric values like;

        •int – holds signed integers of non-limited length.

        •long- holds long integers.

        •float- holds floating precision numbers and it’s accurate upto 15 decimal places.

        •complex- holds complex numbers.
  
         a=10
         print(type(a))
            Output - < class 'int' >

       2.String -
                 The string is a sequence of characters. Python supports Unicode characters. 
       Generally, strings are represented by either single or double quotes.
   
         Str="Ram singh"
         Print(type(str))
            Output - < class 'str' >

       3.Tuple -
                Tuple is another data type which is a sequence of data similar to list. But it is immutable. 
       That means data in a tuple is write protected. Data in a tuple is written using parenthesis and commas.
         Tuple1=(1,2,3,4,5)

      4.List -
              The list is a versatile data type exclusive in Python. list is an ordered sequence of some data written using square brackets([]) and commas(,)
         Lst1 =[1,4,ram,7]

      5.Dictionary -
                    Dictionaries are written within curly braces in the form key:value. It is very useful to retrieve data in an optimized way among a large amount of data.
         Dict1={1:rohit,2:Mohit,3:binod}

      6.Set -
             A set is an unordered collection of items. Set is defined by values separated by a comma inside braces { }.
         Set = {5,1,2.6,"python"}

