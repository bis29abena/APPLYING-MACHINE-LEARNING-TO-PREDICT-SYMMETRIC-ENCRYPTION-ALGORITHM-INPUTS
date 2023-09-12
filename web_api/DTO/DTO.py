class DTO():
    def __init__(self):
        self.message: str = None
        self.success: bool = None
        self.responseData: str = None
    
    def response(self, message: str, success: bool, response: str):
        self.message = message
        self.success = success
        self.responseData = response
        
        return {
            "message": self.message,
            "success": self.success,
            "response": self.responseData
        }