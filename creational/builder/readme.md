Python has named paramters, so , complex objects like `House` can have
```python
class House:

    def __init__(self,floors=1, has_garage=False, has_swimming_pool=False, has_deck=False):
```
So we can do this easily: 
```python
facncy_house = House(floors=3, has_deck=True)
```

But for interests sake this is how we could implement it in python (its a bit crude but it works)