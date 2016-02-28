#Name : PRUDHVI RATNA BADRI SATYA
#A number : A02057243
#Email : prudhvibadri@aggiemail.usu.edu 
#Assignment name : CHATBOT.


from __future__ import print_function

from nltk.chat.util import Chat, reflections

responses = (

(r'((.*)(?=.*professor|lecturer|instructor|teacher)(.*)(?=.*Email|contact|mail id)(.*))',
("Nick.flann@ gmail.com is the contact email",
"His email id is Nick.flann@ gmail.com")),
             
(r'(.*)(professor|lecturer|instructor|teaching|teacher|flann|nick|nicholas|Nicholas S Flann|Nick flann|Nicholas Flann)(.*)\??',
("Nicholas S Flann  is the instructor of cs6600",
"Nick flann is the professor dealing this course for this semester",
" Nicholas Flann teaches this course  ")), 
             
(r'((.*)(textbook|text book)(.*))',            
("Artificial Intelligence: A Modern Approach (3rd Edition), by Russel and Norvig, Prentice Hall, 2009\n\nGet one for You",
"Artificial Intelligence: A Modern Approach (3rd Edition), by Russel and norvig\n\nBuy one",
"AI :A Modern Approach (3rd Edition), by Russel and Norvig, Prentice Hall, 2009\n\n you can get it online")),
             
(r'(.*)(sub topics|subtopic|subtopics)(.*)',
("Refer to canvas since there are many topics under this ",
"you are asking me large data...u please refer to canvas")),

(r'((.*)(topics|course topics|coursetopics)(.*))', 
("\nThe following topics are present in this course\n\n 1 Artificial Intelligence\n\n 2 Intelligent Agents \n\n 3 Solving Problems by Searching\n\n 4 Beyond Classical Search\n\n 5 Adversarial Search\n\n 18 Learning from Examples\n\n 20 Learning Probabilistic Models\n\n 21 Reinforcement Learning",
"\nThere are eight topics in this course\n\n 1 Artificial Intelligence\n\n 2 Intelligent Agents \n\n 3 Solving Problems by Searching\n\n 4 Beyond Classical Search\n\n 5 Adversarial Search\n\n 18 Learning from Examples\n\n 20 Learning Probabilistic Models\n\n 21 Reinforcement Learning")), 
 
(r'((.*)(?=.*assignment|assignments)(.*)(?=.*list|full list|all)(.*))' ,
("1 Chat Bot Assignment\n\n 2 Optimization Assignment \n\n 3 programming Assignment \n\n 4 Game Playing Assignment ",
" 1 Chat Bot Assignment\n\n 2 Optimization Assignment \n\n 3 programming Assignment \n\n 4 Game Playing Assignment ")),
             
(r'((.*)(?=.*assignment|assignments|mid exams|final project|exams|exam|project|finalproject|midexams)(.*)(?=.*due date|points|submission|submit)(.*))' ,
("Refer to canvas for more detailed information",
"Go to canvas for detailed information")),

(r'(.*)(assignment|assignments)(.*)',
 ("1 Chat Bot Assignment\n\n 2 Optimization Assignment \n\n 3 programming Assignment \n\n 4 Game Playing Assignment ",
" 1 Chat Bot Assignment\n\n 2 Optimization Assignment \n\n 3 programming Assignment \n\n 4 Game Playing Assignment ")),
             
(r'(.*)(point|points|marks|proportion|gradeproportion|grade proportion)(.*)',
 (" 1 Assignment - 40 \n\n 2 Written homework - 10 \n\n 3 Mid exams -20 \n\n 4 final project - 50  \n\n  Total - 120 ",
" 1 Assignment - 40 \n\n 2 Written homework - 10 \n\n 3 Mid exams -20 \n\n 4 final project - 50  \n\n  Total - 120 ")),
             
(r'(.*)(sub topics)(.*)',
("Refer to canvas since the information is large i cant provide you",
"you are asking me large data...u please refer to canvas")),

(r'((.*)(?=.*homework)(.*)(?=.*submit|submission)(.*))' ,
("Submit your homework using the Canvas Systems.Make sure that your homework is submitted correctly. If you have multiple files to submit, zip multiple files into one file before submission.",
"Submit your homework using the Canvas Systems.Make sure that your homework is submitted correctly. If you have multiple files to submit, zip multiple files into one file before submission.")),           

(r'(.*)(homework)(.*)',
("Homework should be done individually.It is for 10 points",
"Homework should be done individually by everyone. It has 10 points")), 
             
(r'((.*)(?=.*name|title|code)(.*)(?=.*subject|course|title)(.*))' ,
("CS6600 Intelligent Systems",
"CODE IS CS6600-INTELLIGENT SYSTEMS")), 
                          
(r'((.*)(?=.*course)(.*)(?=.*overview)(.*))' ,
("Artificial Intelligence (AI) aims to understand the mechanisms underlying thought and intelligent behavior, and their embodiment in machines.",
" Intelligent system course approaches AI by using Intelligent Agents as an integrating perspective on the main topics in intelligent behavior.")),
             
(r'((.*)(?=.*office)(.*)(?=.*hours)(.*))' ,
("Office Hours:Tuesday: 9:00 -- 11:00 \n Wednesday: 10:30 -- 12:30",
"office hours are on Tuesday : 9-11 and Wednesday :10:30 -- 12:30")), 
             
(r'((.*)(office|office room)(.*))' ,
("its old Main Room no. 420",
"Office is at 420 old main")),
             
(r'((.*)(doubts|meet|query|queries|problems|problem)(.*))' ,
("Available Office Hours are on Tuesday: 9:00 -- 11:00 \n\t\t\t Wednesday: 10:30 -- 12:30",
"Go and meet during office hours are on Tuesday : 9-11 and Wednesday :10:30 -- 12:30")), 
                                  
                      
(r'((Tell about|tell more about|give|tell|know|know about|about|research)(.*)(?=.*him|flann|his|nick|professor|lecturer|instructor|teaching|teacher|nicholas|Nicholas S Flann|Nick flann|Nicholas Flann)(.*))',
("Dr.Flann's research interests lie advancing executable biology by developing mechanistic multiscale models that bridge the gap between regulatory network dynamics and morphological outcomes.",
 "Dr.Nick flann is interested in the development and application of multiscale models to significant biological subsystems in development, cancer, immunity and yeast colony development. ")),

(r'(hello|howdy|hey|hi(.*))',
  ("Hi...how are you??",
   "Hi....How can i help u??",
   "I am ready to help u.")),
             
(r'((.*)(?=.*subject|course|title)(.*)(?=.*semester|period|semester offered)(.*))',
("This course is available for fall 2014",
"Semester to take this course is fall 2014")),
             
             
(r'((.*)(semester|period|semester offered)(.*))' ,
("This course is available for fall 2014",
"Semester to take this course is fall 2014")),

(r'((.*)(?=.*when)(.*)(?=.*course)(.*))' ,
("This course is available for fall 2014",
"Semester to take this course is fall 2014")),
             
(r'((.*)(?=.*timing|timings|time)(.*)(?=.*class)(.*))' ,
("M F 11:30-12:45",
"MONDAY Friday 11:30-12:45",
"MF 11:30 A.M. - 12:45 P.M.")),
             
(r'((.*)(?=.*timing|timings|time)(.*))',            
("M F 11:30-12:45",
"MONDAY Friday 11:30-12:45",
"MF 11:30 A.M. - 12:45 P.M. Main117")),   
             
(r'((.*)(?=.*grades|grade)(.*)(?=.*see|find|access|)(.*))' ,
("Your grades will be available through the Canvas System",
"Grades can be viewed on canvas")),
             
(r'((.*)(?=.*in completes|incomplete|unfinished|not complete)(.*))' ,
("This means that an incomplete cannot be given to prevent receipt of a bad grade. Under no circumstances can an incomplete be given for which a re-take of the class is required to make up the work.",
"The University policy will be adhered to for incompletes. This means that an incomplete cannot be given to prevent receipt of a bad grade. Under no circumstances can an incomplete be given for which a re-take of the class is required to make up the work.")),             


(r'((.*)(?=.*cheating policy)(.*))' ,
(" Please refer to the Computer Science Department Bulletin Board  for the department's official policy.",
"Refer to the Computer Science Department Bulletin Board  for the department's official policy.")),
             
(r'((.*)(?=.*location|place|class|classroom|room)(.*))',             
("its main117",
"old main 117")),
             
(r'((.*)(ada compliance|compliance|ada)(.*))',             
("If a student has any disability that will likely require some accommodation by the instructor, the student must contact the instructor and document the disability through the Disability Resource Center (Taggart Student Center, Room 104), preferably during the first week of the course. Any requests for special considerations relating to attendance, pedagogy, taking of examinations, etc., must be discussed with and approved by the instructor. In cooperation with the Disability Resource Center, course materials can be provided in alternative formats, e.g., large print, audio, diskette, or Braille.",
"If a student has any disability that will likely require some accommodation by the instructor, the student must contact the instructor and document the disability through the Disability Resource Center (Taggart Student Center, Room 104), preferably during the first week of the course. Any requests for special considerations relating to attendance, pedagogy, taking of examinations, etc., must be discussed with and approved by the instructor. In cooperation with the Disability Resource Center, course materials can be provided in alternative formats, e.g., large print, audio, diskette, or Braille.")),
       
(r'((.*)(?=.*find|get|know|give|fetch|search)(.*)(?=.*info|information|assignment|assignments|syllabus|professor|instructor|teacher)(.*))' ,                         
("Go the canvas to know more information",
"Access canvas for information",
"All assignments and other information dealing with the course are posted on Canvas.")),
             
(r'((.*)(?=.*prerequisites|prerequisite|minimum)(.*))',
("2.5 GPA; \n Grade of C- or better in C 2420 or permission by instructor.",
"2.5 minimum GPA \n c- grade in 2420 \n Get permission from instructor. " )), 
             
(r'((.*)(?=.*Course|subject|course|course work|cs6600|intelligent systems|objective|course objective)(.*))' ,
("This course gives an introduction to the philosophies and techniques of Artificial Intelligence.",
 "CS6600 includes developing a variety of techniques for the design and application of intelligent systems for solving complex problems.")),                 

(r'((.*)(?=.*info|information|details)(.*)(?=.*Course|subject|course|course work|cs6600|intelligent systems|objective|course objective)(.*))' ,
("This course gives an introduction to the philosophies and techniques of Artificial Intelligence.",
 "CS6600 includes developing a variety of techniques for the design and application of intelligent systems for solving complex problems.")),             
                       
(r'((?=.*name)(.*)(?=.your|ur)(.*))',
("my name is chat bot",
"i am  cs6600 chatter bot",
"i am known by name chat bot")),
    
(r'((?=.*who)(.*)(?=.*are)(.*)(?=.you|u)(.*))',
("my name is  cs6600 chat bot",
"i am  cs6600 chatter bot",
"i am known by name  cs6600 chat bot")),         
             
 (r'tell about (you|u|yourself)',
 (" i am created recently ",
  "i am an intelligent chat bot")),
             
(r'((?=.*your|ur)(.*)(?=.*age)(.*))',
 ("i am just born",
  "i am younger than u",
   "You are older than me")),
             
(r'((?=.*how)(.*)(?=.*are|r)(.*)(?=.*you|u)(.*))' ,
("i am super...how about you??",
"i am good...hope you are fine too",
"i am fine....how are you??")),

(r'((?=.*my)(.*)(?=.*name)(.*))' ,
  (" %1..Nice name ",
   "its a nice name"
    "I see, %1",
    "so %1")),
             
  (r'(.*)(good|fine|great)(.*)',
  ("i like that",
   "That's nice"
   "good to hear that")),


#===========================================================================

 (r'OK THEN',
    ("ANYTHING ELSE YOU WISH TO ADD?",
     "IS THAT ALL YOU HAVE TO SAY?",
     "SO, YOU AGREE WITH ME?")),
(r'OK',
    ("DOES THAT MEAN THAT YOU ARE AGREE WITH ME?",
     "SO YOU UNDERSTAND WHAT I'M SAYING.",
     "OK THEN.")),
             
(r'(.*)thankyou|thank you|thank',
("you are welcome",
"you are a polite person",
"its ok...dont thank me")),
             
(r'(.*)help(.*)',
("i can help you on cs6600 syllabus",
"i made to help you on cs6600 syllabus")),

(r'no',
("why are you saying no??",
"i thought you would say yes...please tell me reason")),
              
  (r'i mean (.*)',
    ("SO, %1 mean.",
     "SO, THAT'S WHAT YOU MEAN.",
     "I THINK THAT I DIDN'T CATCH IT THE FIRST TIME.",
     "OH, I DIDN'T KNOW MEANT THAT.")),
             
  (r'i (didnt|did not) mean (.*)',
    ("ok,what did u mean then?? ",
     "oh,i guess i misunderstood u")),
   (r'answer (.*)',
      ("yes i can answer",
       "i am pretty sure i can answer")), 
                   
 (r'I need (.*)',
  ("Why do you need %1?",
    "Are you sure you need %1?")),

  (r'Why dont you (.*)',
  ("Do you really think I don't %1?",
    "Perhaps eventually I will %1.",
    "Do you really want me to %1?")),

  (r'Why cant I (.*)',
  ("Do you think you should be able to %1?",
    "If you could %1, what would you do?",
    "I don't know -- why can't you %1?",
    "Have you really tried?")),

  (r'I cant (.*)',
  ("How do you know you can't %1?",
    "Perhaps you could %1 if you tried.",
    "What would it take for you to %1?")),

  (r'I am (.*)',
  ("Did you come to me because you are %1?",
    "How long have you been %1?",
    "How do you feel about being %1?")),

  (r'Im (.*)',
  ("How does being %1 make you feel?",
    "Do you enjoy being %1?",
    "Why do you tell me you're %1?",
    "Why do you think you're %1?")),

  (r'Are you (.*)',
  ("Why does it matter whether I am %1?",
    "Would you prefer it if I were not %1?",
    "Perhaps you believe I am %1.",
    "I may be %1 -- what do you think?")),

  (r'What (.*)',
  ("Why do you ask?",
    "How would an answer to that help you?",
    "What do you think?")),

  (r'How (.*)',
  ("How do you suppose?",
    "Perhaps you can answer your own question.",
    "What is it you're really asking?")),

  (r'Because (.*)',
  ("Is that the real reason?",
    "What other reasons come to mind?",
    "Does that reason apply to anything else?",
    "If %1, what else must be true?")),

  (r'(.*) sorry (.*)',
  ("There are many times when no apology is needed.",
    "What feelings do you have when you apologize?")),


  (r'I think (.*)',
  ("Do you doubt %1?",
    "Do you really think so?",
    "But you're not sure %1?")),

  (r'Yes',
  ("You seem quite sure.I like it",
    "OK, but can you elaborate a bit?",
    "so,you approve it",
    "you are very confident")),
             
  (r'Is it (.*)',
  ("Do you think it is %1?",
    "Perhaps it's %1 -- what do you think?",
    "If it were %1, what would you do?",
    "It could well be that %1.")),

  (r'It is (.*)',
  ("You seem very certain.",
    "If I told you that it probably isn't %1, what would you feel?")),

  (r'Can you (.*)',
  ("What makes you think I can't %1?",
    "If I could %1, then what?",
    "Why do you ask if I can %1?")),
             
 

  (r'Can I (.*)',
  ("Perhaps you don't want to %1.",
    "Do you want to %1?",
    "If you could %1, would you?")),

  (r'You are (.*)',
  ("Why do you think I am %1?",
    "Does it please you to think that I'm %1?",
    "Perhaps you would like me to be %1.",
    "Perhaps you're really talking about yourself?")),

  (r'You\'re (.*)',
  ("Why do you say I am %1?",
    "Why do you think I am %1?",
    "Are we talking about you, or me?")),

  (r'I dont (.*)',
  ("Don't you really %1?",
    "Why don't you %1?",
    "Do you want to %1?")),

  (r'I feel (.*)',
  ("Good, tell me more about these feelings.",
    "Do you often feel %1?",
    "When do you usually feel %1?",
    "When you feel %1, what do you do?")),

  (r'I have (.*)',
  ("Why do you tell me that you've %1?",
    "Have you really %1?",
    "Now that you have %1, what will you do next?")),

  (r'I would (.*)',
  ("Could you explain why you would %1?",
    "Why would you %1?",
    "Who else knows that you would %1?")),

  (r'Is there (.*)',
  ("Do you think there is %1?",
    "It's likely that there is %1.",
    "Would you like there to be %1?")),

 
  (r'You (.*)',
  ("We should be discussing you, not me.",
    "Why do you say that about me?",
    "Why do you care whether I am %1? or not")),

  (r'Why (.*)',
  ("Why don't you tell me the reason why %1?",
    "Why do you think %1?")),

  (r'I want (.*)',
  ("What would it mean to you if you got %1?",
    "Why do you want %1?",
    "What would you do if you got %1?",
    "If you got %1, then what would you do?")),

  (r'(.*)\?',
  ("Why do you ask that?",
    "Ask me questions that i can answer",
    "your questions do not match my level....ask simple questions",
    "Why don't you tell me?")),

  (r'(.*)(quit|bye|good bye)(.*)',
  ("Thank you for talking with me.",
    "Good-bye.",
    "Take care....bye..."
    " Have a good day!")),

  (r'(.*)',
  ("Please tell me more.",
    "Let's change focus a bit",
    "Can you elaborate on that?",
    "Why do you say that %1?",
    "I see.",
    "Very interesting.",
    "I see. Give me more information."
    "I'M NOT SURE IF I UNDERSTAND WHAT YOU ARE TALKING ABOUT.",
     "CONTINUE, I'M LISTENING...",
     "VERY GOOD CONVERSATION!")),
         

)            
            
             

my_chatbot = Chat(responses, reflections)

def my_chat():
    print('*' * 75) 
    print("Chatbot!".center(75)) 
    print('*' * 75) 
    print ("I will give information about CS6600 course syllabus".center(75))
    print("")
    print('Lets begin our chat'.center(75)) 
    print('*' * 75)
    print("") 
    print ("I am Ready")
    my_chatbot.converse()

def demo(): my_chat()

if __name__ == "__main__":
    demo()
