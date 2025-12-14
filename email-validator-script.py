import logging
import random

logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")

ALLOWED_DOMAINS={
    "gmail.com",
    "yahoo.com",
    "outlook.com",
    "icloud.com"
}

COMMON_NAMES={
    
    "johnsmith",
    "admin",
    "test",
    "user",
    "info",
    "janesmith"
}

def suggest_unique_usernames(username,domain,count=3):
    suggestions=[]
    for _ in range(count):
        number=random.randint(100,999)
        suggestions.append(f"{username}{number}@{domain}")
    return suggestions
        

def email_validator(email):
    special_characters="!#$%&'*+/=?^_`{|}~.-"   
    
    if "@"not in email:
        logging.error("Invalid email: missing @ symbol")
        raise ValueError("Invalid email: missing @ symbol")
    
    if email.count("@") !=1:
        logging.error("Multiple @ symbols found, emails can only contain one @ symbol")
        raise ValueError("Multiple @ symbols found, emails can only contain one @ symbol")
    
    
    if email[0] in special_characters:
        logging.error("Email cannot start with special characters")
        raise ValueError("Email cannot start with special characters")
    
    local,domain=email.split("@")
    if not local:
        logging.error("local part of email is missing")
        raise ValueError("Missing username before @ symbol")
    
    if not domain:
        logging.error("Domain part of email is missing")
        raise ValueError("Missing domain after @ symbol")
    
    if domain not in ALLOWED_DOMAINS:
        logging.error("Domain name does not exist in allowed domains")
        raise ValueError(f"Domain does not exist in allowed domains:{','.join(ALLOWED_DOMAINS)}")
    
    if local.lower() in COMMON_NAMES:
        suggestions=suggest_unique_usernames(local,domain)
        logging.warning("Common username detected,suggesting alternatives")
        return{
            "valid":True,
            "common_username":True,
            "suggestions":suggestions
        }
        
    
    logging.info("Email is valid")
    return{
        "valid":True,
        "common_username":False
    }
    
    
if __name__=="__main__":
    while True:
        print("\n------Email Validator------")
        email=input("Enter an email to validate (or type 'exit' to quit): ")
        if email.lower()=="exit":
            logging.info("Exiting email validator")
            break
        try:
            result=email_validator(email)
            print("Email is valid.")
            if result["common_username"]:
                print("Common username detected. Here are some suggestions:")
                for suggestion in result["suggestions"]:
                    print(f"- {suggestion}")
        except ValueError as e:
            print(f"Email is invalid:{e}")
            
    
    
    
    
        