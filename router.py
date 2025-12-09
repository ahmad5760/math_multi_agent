from agents import SchoolAgent, CollegeAgent, UniversityAgent

class AgentRouter:
    def __init__(self, model):
        # Initialize the specific agents
        self.school_agent = SchoolAgent(model, "School Agent")
        self.college_agent = CollegeAgent(model, "College Agent")
        self.university_agent = UniversityAgent(model, "University Agent")

    def route_problem(self, level, problem):
        """
        Routes the problem to the correct agent based on level input.
        """
        level = str(level).lower().strip()

        if level in ['1', 'school', 'elementary']:
            return self.school_agent, self.school_agent.solve(problem)
        
        elif level in ['2', 'college', 'high school']:
            return self.college_agent, self.college_agent.solve(problem)
        
        elif level in ['3', 'university', 'uni', 'advanced']:
            return self.university_agent, self.university_agent.solve(problem)
        
        else:
            return None, "Error: Invalid Level. Please choose School, College, or University."