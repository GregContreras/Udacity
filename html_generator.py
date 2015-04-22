def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('DESCRIPTION:')
    title = concept[start_location+7 : end_location-1]
    return title

def get_description(concept):
    start_location = concept.find('DESCRIPTION:')
    description = concept[start_location+13 :]
    return description

def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('TITLE:')
        next_concept_end   = text.find('TITLE:', next_concept_start + 1)
        concept = text[next_concept_start:next_concept_end]
        text = text[next_concept_end:]
    return concept
        

TEST_TEXT = """TITLE: LIST
DESCRIPTION: a new way to store data in a more structured object.
TITLE: FOR LOOPS
DESCRIPTION: new type of loop to iterate over structured data.
TITLE: STRUCTURED DATA (String Data Type)
DESCRIPTION: a sequence of ONLY characters (surrounded by single or double quotes)
TITLE: STRUCTURED DATA (List Data Type)
DESCRIPTION: sequence of ANYTHING numbers, characters, other lists!!!  Use square brackets.
TITLE: NESTED LISTS
DESCRIPTION: Can contain characters and numbers.  Ex: mixed up = ['apple', 3, 'oranges', 27, [1,2, ['alpha', 'beta']]]
TITLE: MUTATIONS
DESCRIPTION: Only supported by Lists, not Strings. Lists support mutations.  Mutations allow you to modify a value in the 

variable
TITLE: ALIASING
DESCRIPTION: This allows you to assign different names to a Variable.
TITLE: APPEND
DESCRIPTION: updates a list with a new element.
TITLE: PLUS
DESCRIPTION: similar to concatenation for strings.  It doesn't mutate but it produces a new list.
TITLE: LEN
DESCRIPTION: stands for length and outputs the number of elements in the input.
TITLE: LENGTH AND PLUS
DESCRIPTION: This will count all elements.
TITLE: LENGTH AND APPEND
DESCRIPTION: elements and appended lists are counted (elements inside the list aren't counted).
TITLE: WHILE LOOPS
DESCRIPTION: used for repeating sections of code until a defined condition is met.
TITLE: FOR LOOPS
DESCRIPTION: used when you have a piece of code which you want to repeat n number of times."""


def generate_all_html(text):
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        title = get_title(concept)
        description = get_description(concept)
        concept_html = generate_concept_HTML(title, description)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    return all_html


print generate_all_html(TEST_TEXT)
