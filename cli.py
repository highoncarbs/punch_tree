import click
import json

# TODO
# 1. Create JSON storage - Done
# 2. Add Persons - Done
# 3. Add Relationships (works only if person exists in the family tree)  - Done
# 4. Connect Persons as per relationship 
# 5. Count the number of relations of a person
# 6. Get the parent of the child


# Define file path for data storage
data_file = "family_tree.json"

def load_data():
  
  try:
    with open(data_file, 'r') as f:
      return json.load(f)
  except (FileNotFoundError, json.JSONDecodeError):
    return { 'tree': {}, 'relations':[]}

def save_data(data):
  
  with open(data_file, 'w') as f:
    json.dump(data, f, indent=2)

people = load_data()  # Load data on init

def get_person(name):

  if name not in people['tree']:
    click.echo(f"Person '{name}' not found in family tree.")
    return None
  return people['tree'][name]

@click.group()
def family_tree():
  pass


@family_tree.command()
@click.argument('name')
def add_person(name):
  
  people['tree'][name] = {}
  save_data(people)
  click.echo(f"Person '{name}' added to family tree.")

@family_tree.command()
@click.argument('relation')
def add_relation(relation):
   
    if relation not in people['relations']:
        people['relations'].append(relation)
        save_data(people)
        click.echo(f"Relation '{relation}' added to family tree.")
    else:
        click.echo(f"Relation '{relation}' alrady exisits in family tree.")

@family_tree.command()
@click.argument('name1')
@click.argument('relationship')
@click.argument('name2')
def connect(name1, relationship, name2):
  
    person1 = get_person(name1)
    person2 = get_person(name2)
    if person1 is None or person2 is None:
        return

    if relationship.lower() not in people['relations']:
        click.echo(f"Invalid relationship '{relationship}'. Valid options are: {', '.join(people['relations'])}")
        return

    if relationship.lower() in list(person1.keys()):
        people['tree'][name1][relationship].append(name2)
     
    else:
        people['tree'][name1].setdefault(relationship, []).append(name2)

    save_data(people)
    click.echo(f"Connected '{name1}' as '{relationship}' of '{name2}'.")

@family_tree.command()
@click.argument('name1')
@click.argument('relationship')
def count(name1, relationship):
  
    person1 = get_person(name1)
    if person1 is None :
        return

    if relationship.lower() not in people['relations']:
        click.echo(f"Invalid relationship '{relationship}'. Valid options are: {', '.join(people['relations'])}")
        return
    try: 
        count = len(people['tree'][name1][relationship])
    except KeyError:
        count = 0
    save_data(people)
    click.echo(f"Count of '{relationship}' of '{name1} is {count}'.")

@family_tree.command()
@click.argument('name1')
@click.argument('relationship')
def find(name1, relationship):
   
    person1 = get_person(name1)
    if person1 is None :
        return

    if relationship.lower() not in people['relations']:
        click.echo(f"Invalid relationship '{relationship}'. Valid options are: {', '.join(people['relations'])}")
        return
    try: 
        click.echo(' '.join(people['tree'][name1][relationship]))
    except KeyError:
        click.echo('None found')


if __name__ == '__main__':
  family_tree()