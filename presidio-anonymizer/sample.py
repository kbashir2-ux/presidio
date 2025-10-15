from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

# Initialize the anonymizer engine
engine = AnonymizerEngine()

# Define the input text
text = "My name is Khadijah, Khadijah Bashir"

# Define the recognizer results
analyzer_results = [
    RecognizerResult(entity_type="PERSON", start=11, end=19, score=0.8),   # "Khadijah"
    RecognizerResult(entity_type="PERSON", start=21, end=33, score=0.8),   # "Khadijah Bashir"
]

# Define the anonymization operator to replace with your GitHub username
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
