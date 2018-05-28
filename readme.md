
# Convert JSON Serializable #

Convert an arbitraty Python object to a JSON serializable object.

## Problem ##
Not all Python objects are serializable by the JSON module.  Writing your
own `default` function and passing it into JSON `dump` or `dumps` allows
you to convert your object to something that is JSON serializable.

Note: This converts values but not keys.  Keys must still be strings
(as required by JSON).

## Example Output ##
This example uses enum.Enum and decimal.Decimal types.  The native Python
representation via `pprint()` is:
```
{'friends': [<Animal.dog: 'dog'>, <Animal.cat: 'cat'>],
 'legs': Decimal('4'),
 'name': 'AJ',
 'type': <Animal.dog: 'dog'>,
 'weight': Decimal('11.199999999999999289457264239899814128875732421875')}
```

The JSON representation via `json.dumps()` is:

```
{
    "name": "AJ",
    "legs": 4,
    "weight": 11.2,
    "type": "dog",
    "friends": [
        "dog",
        "cat"
    ]
}
```