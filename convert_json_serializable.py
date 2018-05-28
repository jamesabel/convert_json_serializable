
from enum import Enum
import json
from pprint import pprint
from decimal import Decimal


def convert_json_serializable(o):
    """
    Convert an object to a type that is json serializable.
    Use with json.dump or json.dumps with argument default=convert_json_serializable.

    Example:
        json.dumps(my_animal, indent=4, default=convert_json_serializable)

    :param o: object to be converted to a type that is json serializable
    :return: a json serializable representation
    """
    if hasattr(o, 'value'):
        # e.g. enum.Enum
        serializable_representation = o.value
    elif type(o) is Decimal:
        # decimal.Decimal, both integer and floating point
        if o % 1 == 0:
            # if representable with an integer, use an integer
            serializable_representation = int(o)
        else:
            # not representable with an integer so use a float
            serializable_representation = float(o)
    else:
        raise NotImplementedError('can not serialize %s' % type(o))
    return serializable_representation


def main():
    class Animal(Enum):
        dog = "dog"
        cat = "cat"

    my_animal = {'name': 'AJ',  # normal string
                 'legs': Decimal(4),  # Decimal with an integer (e.g. boto3 uses Decimal)
                 'weight': Decimal(11.2),  # Decimal with a float (e.g. boto3 uses Decimal)
                 'type': Animal.dog,  # user defined Enum
                 'friends': [Animal.dog, Animal.cat]  # an convert inside other complex objects (lists, dicts)
                 }

    print('native Python representation:')
    pprint(my_animal)
    print()

    print('json representation:')
    print(json.dumps(my_animal, indent=4, default=convert_json_serializable))


if __name__ == '__main__':
    main()
