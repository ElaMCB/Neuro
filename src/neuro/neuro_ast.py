"""
Neuro Abstract Syntax Tree (AST) nodes
"""

class Node:
    """Base AST node"""
    pass

class Pipeline(Node):
    def __init__(self, name, goal, data, model, deploy):
        self.name = name
        self.goal = goal
        self.data = data
        self.model = model
        self.deploy = deploy

class DataPipeline(Node):
    def __init__(self, steps):
        self.steps = steps

class ModelCall(Node):
    def __init__(self, name, args):
        self.name = name
        self.args = args

class FunctionCall(Node):
    def __init__(self, name, args):
        self.name = name
        self.args = args
