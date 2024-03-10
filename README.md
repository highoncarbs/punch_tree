
## Family Tree CLI 

### Setup 

`pip install click`
`python cli.py` to access the cli application

### Available Commands

`python cli.py add-person <person_name>`
`python cli.py add-relation <relation>`
`python cli.py connect <person1> <relationship> <person2>`
`python cli.py count <person1> <relations>`
`python cli.py find <person1> <relations>`

### Validation

#### Limited Relationship Validation

The code only checks if a relationship type is present in the predefined relations list, but doesn't enforce other constraints (e.g., preventing a person from being their own parent).

#### No Data Integrity Checks

The code doesn't perform extensive validation on the data itself, such as ensuring consistency of relationships or preventing duplicates.
Additional Assumptions:

#### Single Relationship Type per Connection

Each connection between people is assumed to have only one relationship type (e.g., a person can't be both a parent and a sibling to another person).

#### No Gender-Specific Relationships

The code doesn't account for gender-specific relationships (e.g., "mother", "father", "sister", "brother").

#### Single Name Identifier

People are identified solely by their name, assuming uniqueness and no need for additional identifiers or disambiguation.

#### Important Considerations

#### Relationship Complexity

The code may be limited in representing complex family structures, such as blended families or adoption, due to its assumptions about relationships.

#### Error Handling

The code's error handling is basic and might not fully address unexpected input or data inconsistencies.

#### Extensibility

Incorporating additional features or handling more complex relationships might require significant code modifications due to the assumptions made in the data structure and logic.