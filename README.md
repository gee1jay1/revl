Greg Judd - REVL Developer Task

Please find enclosed my attempt at the REVL developer task.

I know this isn't perfect, but I did want to honour the time constraint.

Thoughts on general approach:

My two primary ideas were
1) Have a series of Python dictionaries for each country that specify the config for base vat, and any special rules
   (e.g. bread, milk). The main drawback here was that this would mean defining a very generic and extendable syntax to 
   represent each of the rules for a given type of item. This would be hard to read, and may even prove impossible to do.
   The upside would be that if you can get it right, the actual code to implement it should be fairly generic.
2) Have a class for each of the countires, and within each define any custom rules while inheriting the relevant rules from 
   the region. This means we can reuse code, define a clear relationship between regions and countries and makes things easier 
   to extend (more countries, sub regions within countries etc). The main drawback is that some rules may be so specialised 
   that it could be hard to define in terms of parent rules.
   
I decided to go for approach 2 and I think the drawback of approach one, especially within the time limit, would have made 
things difficult.

I have added tests, and hope these serve as demonstation of the code (vs a script just to run the class methods).
To run tests 'py.test test_calculate_vat.py'. If I had more time, I would add more tests, but hope this gives a flavour of
the kind of tests I write.

I have assumed that the products are stored in a way, or can easily be converted, such that they are a dictionary with a name
and type key. I think it would be better if I had also made the cost and region values in this product dictionary as opposed separate values. Although this isn't much of a change in the code.
So I'm assuming any given product will have a type, cost (pre vat) and region in some format that I am able to parse.
I would imagine products are either stored in a database or will be taken off a queue.
I have assumed each product will only be subject to one customised VAT rule, but this may need to be altered.

Improvements:
- I think perhaps disassociating the product from the VAT class might be better, as it would allow one VAT class to calculate
  multiple product's VAT. The downside is that it will then require passing around the cost and product type.
- More tests.
- Error handling / input checking.
- Just to note, while I try to keep them short I usually don't hard enforce line length. There are a handful >79 so if this
  formatting were a requirement then I would fix up. As with adding mandatory doc strings etc if these are part of REVL's
  coding standards.

Questions for developers / stakeholders:
- How time critical is this operation? Will it be performed on thousands of incoming products every second?
- How often do we expect tax rules to change?
- How many regions / countries do we expect to have in the future? 
- What decimal place do we wish to round to?
- Will every value be in the correct currency and need to be returned in the correct currency (i.e. different from input)?

