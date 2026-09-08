class ConversationState:
    def __init__(self):
        self.pending_action = None
        self.data = None


conversation = ConversationState()