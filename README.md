# DuodecimalCalculator
Dozenal (duodecimal) calculator with excellent GUI. Including basic mode, scientific mode, and base converter mode.

## Numeral System

| Dozenal | O | A | B | C | D | E | F | G | H | I | K | L | AO |
| Decimal | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |

## Basic Mode:

Including basic arithmetic operation functions. Able to display the last equation.

<img width="182" alt="1" src="https://github.com/PhyChemBlue/DuodecimalCalculator/assets/59059717/571f5edc-3031-415e-9463-3c7efb7fb69d">

## Scientific Mode:

In addition to the basic mode, scientific mode includes exponential and logarithmic functions, trigonometric functions, power and root functions, and many other mathematical functions. It also includes one independent memory (M) and one last answer memory (Ans), constants like e and π. It further includes functions like angular unit conversion between degrees and radians, and base conversion from dozenal to decimal.

<img width="182" alt="2" src="https://github.com/PhyChemBlue/DuodecimalCalculator/assets/59059717/920f92e9-50c5-46ad-bb88-b1955cb1a9ba">

## Base Converter Mode:

Able to convert numbers between decimal and dozenal.

<img width="182" alt="3" src="https://github.com/PhyChemBlue/DuodecimalCalculator/assets/59059717/9cc46207-1fe8-482f-849c-3301e8c75592">

## Why use OABC...IKL instead of 0123...9AB as dozenal numeral system?

It is to remind you that you are dealing with a totally different numeral system. Although it may seems more familiar when you are tackling arithmetic without carry if you use 012...9AB as numeral system, you may often be disturbed by number sense from the decimal system, especially when you're tackling arithmetic with carry or you're not getting attention. For example, you may habitually think that "13" is a prime number in dozenal because it is in decimal, actually it can be divided by "3" because it ends in "3" (if you still feel confused, think that "13(doz) = 15(dec)"). You will not encounter this problem if you see "AC", unless you convert it into "13" at first. "AC" is divisible by "C" because numbers end in "O", "C", "F", or "I" is divisible by "C". You may also think that "0.9" is closer to "1" than "one half" in dozenal, but you may not think so if you see "O.I" (Actually, the distance between "O.I" to "O.F" and "O.I" to "A" is the same. If you still feel confused, think that O.I = 0.9(doz) = 0.75(dec) (NOT 0.9(dec)!!!)).

As for memorizing multiplication tables, the only convenience of using 012...9AB numeral system is that you don't need to memorize the following 4 rules again(2×2=4, 2×3=6, 2×4=8, 3×3=9). However, you have to tackle the interference from decimal when you memorize other 51 rules(such as 4×9=30, 5×6=26, 9×9=69, and so on). These are why I use OABC... instead of 0123... as dozenal numeral system.

Dozenal multiplication table:

||A|B|C|D|E|F|G|H|I|K|L|AO|
|A|A|B|C|D|E|F|G|H|I|K|L|AO|
|B|B|D|F|H|K|AO|AB|AD|AF|AH|AK|BO|
|C|C|F|I|AO|AC|AF|AI|BO|BC|BF|BI|CO|
|D|D|H|AO|AD|AH|BO|BD|BH|CO|CD|CH|DO|
|E|E|K|AC|AH|BA|BF|BL|CD|CI|DB|DG|EO|
|F|F|AO|AF|BO|BF|CO|CF|DO|DF|EO|EF|FO|
|G|G|AB|AI|BD|BL|CF|DA|DH|EC|EK|FE|GO|
|H|H|AD|BO|BH|CD|DO|DH|ED|FO|FH|GD|HO|
|I|I|AF|BC|CO|CI|DF|EC|FO|FI|GF|HC|IO|
|K|K|AH|BF|CD|DB|EO|EK|FH|GF|HD|IB|KO|
|L|L|AK|BI|CH|DG|EF|FE|GD|HC|IB|KA|LO|
|AO|AO|BO|CO|DO|EO|FO|GO|HO|IO|KO|LO|AOO|
