class Tabu :
    #init method 
    def __init__(self , headers ) :
        #headers are the title of each column 
        self.headers = headers
        #self.tabulated holds the value of tabulat-ed table 
        self.tabulated = ""
        #self.w is width of each column , w stands for width 
        self.w = 0
        #am stands for amature data , its stores the values of cloumn and rows as tuple (more like raw data ) 
        self.am = []
    #add function to add a rows 
    def add (self , data ) :
        #defining the value of width by calculating lenth of the column 
        w = [len(i) + 2 for i in data if self.w <= len(i)  ]
        #just a loop for checking if width is correct and getting updated 
        for width in w :

            if self.w <  width :

                self.w = width

       # print(self.w) <- (debug Purpose) 
        # appending the data 
        self.am.append(data)

       # print(self.am) <- (Debug Purpose) 



    #method for rendering the table 
    def render(self) :
        #getting the titles ready 
        for header in self.headers :

            self.tabulated +=  "|" + header + (self.w - len(header)  ) * " "

        self.tabulated += f"""\n{self.w * len(self.headers) * "_"}\n"""
        #gettin the rows ready 
        for rows in self.am :

            for fields in rows :

                self.tabulated += f"|{fields}" + (self.w - len(fields) ) * " "

            self.tabulated += "\n" 

        print("_" * (len(self.headers) * self.w) )
        print(self.tabulated)


# test 
a = Tabu(["something" , "not somethin" , "epic" ])

for i in range(5) :

    a.add(["ok" , "lmk" , "owl"])

a.add(["djsjsjsj" ," 7       37373" , "&£&£&£" ])

a.add(["iejdj" , "rheh" , "rueu" ])

a.render()