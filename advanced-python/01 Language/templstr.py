# demonstrate template string functions
from string import Template

def main():
    # Usual string formatting with format()
    str1 = "You're watching {0} by {1}".format("Advanced Python", "Joe Marini")
    print(str1)
    
    # create a template with placeholders
    template1 = Template("You're watching ${title} by ${author}")
    
    # use the substitute method with keyword arguments
    print(template1.substitute(title="Advanced Python", author="Joe Marini"))
       
    # use the substitute method with a dictionary
    data = {
        "title": "Advanced Python",
        "author": "Joe Marini"
    }
    print(template1.substitute(data))
    
if __name__ == "__main__":
    main()
    