from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

# Initialize the anonymizer engine
engine = AnonymizerEngine()

#input text
'''
The input text should be "My name is <Your First Name>, <Your Full Name>."
Example: "My name is Siyuan, Siyuan Jiang."
'''
'''
text = "My name is Bashir, Khadijah Bashir."
#text = "My name is Khadijah, Khadijah Bashir"

# recognizer results (start and end positions)
analyzer_results = [
    RecognizerResult(entity_type="PERSON", start=11, end=17, score=0.8),  #
    RecognizerResult(entity_type="PERSON", start=19, end=34, score=0.8),  #
]
'''
# Define the input text
text = "My name is Khadijah, Khadijah Bashir."

# recognizer results (start and end positions)
analyzer_results = [
    RecognizerResult(entity_type="PERSON", start=11, end=19, score=0.8),  # 
    RecognizerResult(entity_type="PERSON", start=21, end=36, score=0.8),  # 
]


# Define the anonymization operator
operators = {
    "PERSON": OperatorConfig("replace", {"new_value": "kbashir2-ux"})
}

# Perform anonymization
result = engine.anonymize(
    text=text,
    analyzer_results=analyzer_results,
    operators=operators
)

# Print the result
print(result)
