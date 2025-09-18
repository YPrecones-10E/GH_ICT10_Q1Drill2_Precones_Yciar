# Working with Strings
from pyscript import display, document

def generate (e):
    document.getElementById('cont').innerText=""

    name = document.getElementById('name').value
    age = document.getElementById('age').value
    school= document.getElementById('school').value


    message = f"""👤 Student Profile
    Name   : {name}
    Age    : {age}
    School : {school}

    ✏️ Notes:
    {name}\t is {age} years old \n and studies at {school}.
    """
    display(message, target='cont')