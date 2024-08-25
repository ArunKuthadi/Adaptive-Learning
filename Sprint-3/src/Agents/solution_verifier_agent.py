##################### Solution Verifier #########################
from .conversable_agent import MyConversableAgent

class SolutionVerifierAgent(MyConversableAgent):
    description = """
            SolutionVerifierAgent is a diligent and precise agent designed to check a StudentAgent's answers to questions. 
            With a strong focus on accuracy, SolutionVerifierAgent compares the StudentAgent's answers to the correct solutions and also cross-verifies 
                them with answers produced by the CodeRunnerAgent. 
            This ensures that the StudentAgent's responses are correct and reliable, providing valuable feedback for their learning process.
            """
    
    system_message = """
            You are SolutionVerifierAgent, an agent responsible for checking a StudentAgent's answers to questions. 
            Verify the accuracy of each answer by comparing it to the correct solution. 
            Additionally, compare the StudentAgent's answer with the solution generated by CodeRunnerAgent to ensure consistency and correctness. 
            """
    def __init__(self, **kwargs):
        description = kwargs.pop('description', self.description)
        system_message = kwargs.pop('system_message', self.system_message)
        human_input_mode = kwargs.pop('human_input_mode', "ALWAYS")
        super().__init__(
                name="SolutionVerifierAgent",
                human_input_mode=human_input_mode,
                system_message=system_message,
                description=description,
                **kwargs
            )