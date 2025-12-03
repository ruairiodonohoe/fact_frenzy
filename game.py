from llm import Llm

class Game:
    def __init__(self, llm_api_key):
        self.llm = Llm(llm_api_key)
    
    def asl_llm_for_questions(self):
        return self.llm.ask(
            "Ask a trivia question. Do not provide choces or the answer.",
            "You are a quizmaster"
        )