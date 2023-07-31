from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
ans=True
class User_interface:
    def __init__(self,quiz:QuizBrain):
        self.quiz=quiz
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.canvas = Canvas(bg="white",width=300,height=250)


        self.ques_text =self.canvas.create_text(150,125,text=" ",
                                fill=THEME_COLOR,
                                width=280,
                                font=("Arial", 20,"italic"))

        self.canvas.grid(column=0, row=1, columnspan=2,pady=50)



        #---- buttons

        true_image =PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image, bd=0, highlightthickness=0,command=self.true)
        self.true_button.grid(column=0, row=2, pady=20, padx=20)

        false_image =PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, bd=0, highlightthickness=0,command=self.false)
        self.false_button.grid(column=1, row=2, pady=20, padx=20)
        self.get_next_question()

    def true(self):
        global ans

        ans = self.quiz.check_answer("true")
        self.feedback(ans)
        if self.quiz.still_has_questions():
         self.get_next_question()

    def false(self):
        global ans
        ans= self.quiz.check_answer("false")
        self.feedback(ans)
        if self.quiz.still_has_questions():
          self.get_next_question()
    def feedback(self,ans):
        if ans:
            self.canvas.config(bg="green")
            self.window.after(1000,self.change)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000,self.change)

    def change(self):
        self.canvas.config(bg="white")



    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.ques_text, text=q_text)







        self.window.mainloop()
