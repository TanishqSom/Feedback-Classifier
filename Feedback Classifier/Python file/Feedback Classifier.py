#List of positive words that are often used
positive_words = ['good','great','astounding','bedazzling','brilliant','breathtaking','classy','compelling','dazzling','eclipsing','nice','amazing','relaxing']
#List of negative words that are often used
negative_words = ['bad','worst','dissatisfactory','boring','poor','second-rate','second-class','cheap','inferior','substandard']



#Creating our function 
def Classifier(feedback):
    for i in feedback.split():
        if i in positive_words:
            output = "This is a positive feedback"
        if i in negative_words:
            output = "This is a negative feedback"
    return output




#Taking input
feedback = str(input("Your feedback \n"))

#Calling the function
print(Classifier(feedback))
