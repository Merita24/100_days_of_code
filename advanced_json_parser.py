class InvalidJsonIndexError(Exception):
    pass







class JSONParser:
    def __init__(self,text):
        self.text=text
        self.index=0
        
    def current_char(self):
        if self.index<len(self.text):
            return self.text[self.index]
        return None
    
    def advance(self):
        self.index+=1
        
    def skip_whitespaces(self):
        while self.current_char()and self.current_char().isspace():
            self.advance()
            
    def parse_value(self):
        self.skip_whitespaces()
        char=self.current_char()
        if char == "{":
            return self.parse_object()
        elif char=="[":
            return self.parse_array()
        elif char=='"':
            return self.parse_string()
        elif char and (char.isdigit() or char =='-'):
            return self.parse_number()
        elif self.text.startswith("true",self.index):
            self.index+=4
            return True
        elif self.text.startswith("false",self.index):
            self.index+=5
            return False
        elif self.text.startswith("null",self.index):
            self.index+=4
            return None 
        else:
            raise InvalidJsonIndexError(f"Invalid JSON at index:{self.index}")
        
    def parse_string(self):
        self.advance()
        start=self.index
        while self.current_char()!='"':
            self.advance()
        value=self.text[start:self.index]
        self.advance()
        return value
    
    def parse_number(self):
        start=self.index
        while self.current_char()and (self.current_char().isdigit() or self.current_char() in '.-'):
            self.advance()
        num_str=self.text[start:self.index]
        if '.'in num_str:
            return float(num_str)
        return int(num_str)
    
    
    def parse_array(self):
        self.advance()
        arr=[]
        
        while True:
            self.skip_whitespaces()
            if self.current_char()==']':
                self.advance()
                return arr
            
            value=self.parse_value()
            arr.append(value)
            self.skip_whitespaces()
            if self.current_char()==',':
                self.advance()
                
    def parse_object(self):
        self.advance()
        obj={}
        
        while True:
            self.skip_whitespaces()
            if self.current_char()=="}":
                self.advance()
                return obj
            
            key=self.parse_string()
            self.skip_whitespaces()
            self.advance()
            value=self.parse_value()
            obj[key]=value
            
            self.skip_whitespaces
            if self.current_char()==',':
                self.advance()

if __name__=="__main__":
    json_text = '{"name": "Merita", "age": 24, "skills": ["python", "security"]}'

parser = JSONParser(json_text)
result = parser.parse_value()
print(result)
            