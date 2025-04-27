import os
from agents import Agent,Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
from dotenv import load_dotenv, find_dotenv
set_tracing_disabled(disabled=True)
load_dotenv(find_dotenv())

gemini_api_key=os.getenv("GEMINI_API_KEY")

# Step-1: Provider
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

# Step-2: Model
model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = provider,
)



# Step-4: Agent
fiverr_gig_agent = Agent(
    name="fiverr gig creator",
    handoff_description="Specialist Agent for fiverr gig creator",
    instructions="You provide help with fiverr gig creator. Explain your reasoning at each step and include examples",
    model=model
)

# Step-5: Start chat


def main():  
    history = []  
    while True:
        user_input = input("Enter your message. To quit enter 'exit'.")
        if user_input.lower() == "exit":
            print("Exiting....")
            break
        history.append({"role":"user","content":user_input})
        response = Runner.run_sync(
            starting_agent=fiverr_gig_agent,
            input=history
        )
        history.append({"role":"assistant","content":response.final_output})
        print("Assistant:" ,response.final_output )
       

main()
        
    
    
    
    
    #  history = []
    #     user_input=input("enter message : ")
    #     history.append({"role" : "user", "content" : user_input})

    #     result = Runner.run_sync(
    #         fiverr_gig_agent,
    #         input = history,
    #         run_config=run_config
    #     )
    #     print(result.final_output)
    #     history.append({"role" : "fiverr gig creator", "content" : result.final_output})
    #     if user_input == "exit":
    #         break