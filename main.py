from google import genai

client = genai.Client(api_key = "AIzaSyANBncCdMcpzy2Ufu5y4UPG3cpgjgj5vCA")

################ Basic #########################

# user_input = input("Enter your prompt:")
# response = client.models.generate_content(
#     model = "gemini-2.5-flash",
#     contents = user_input
# )
# print(response.text)

#################### like chatboat #####################

# while True:
#     user_input = input ("You: ")           here each session is independent no previous data is saved
#     response = client.models.generate_content(
#     model = "gemini-2.5-flash",
#     contents = user_input  
#     )
#     print("AI: "+ response.text)
    
#################### for short term memory ###########################
 
messages = [] #to store recent past history
while True:
    user_input = input ("You: ")
    messages.append("User: "+ user_input)
    response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = messages 
    )
    print("AI: "+ response.text)