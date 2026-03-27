---
title: "Java constructor weirdness"
date: 2005-05-26 14:50:00 -0600
mood: annoyed
song: "Good Charlotte - Lifestyles of the rich & famous (Frequence3"
original_url: https://restless-coder.livejournal.com/15139.html
---

Every once in a while, something about the way Java works still surprises me. If you're not a programmer, you will probably not be interested in this technical rant, so I've enclosed it in a cut.  
  

Here is a small example program that demonstrates the issue:  
  

  
  

    
    
            **// Extension.java**
    
            **/**** **Demonstrates a weird inheritance issue.*****/**
            **public** **class** Extension **extends** Base {
              **private** **int** value = **100** ;
    
              **public** Extension() {
                **super**(); **// super constructor calls doStuff for us**
                System.out.println(**"Extension constructor: value = "** + value);
              }
    
              **public** **void** doStuff() {
                **// You would think value would be 100 here, wouldn't you? ;-)**
                **// But it is zero, because the value = 100 assignment does not happen**
                **// until after the superclass constructor is finished. (Why? No idea!)**
                **// Since this method overrides a method called in the superclass**
                **// constructor, the execution of this method happens before the**
                **// extension's field assignments.**
                System.out.println(**"Extension.doStuff() before: value = "** + value);
                **super**.doStuff(); **// do stuff superclass does, in addition to our stuff**
                System.out.println(**"Extension.doStuff() after: value = "** + value);
              }
    
              **public** **static** **void** main(String[] args) { **new** Extension(); }
            }
    
            **class** Base {
              **public** Base() {
                System.out.println(**"Base constructor: before doStuff"**);
                doStuff();
                System.out.println(**"Base constructor: after doStuff"**);
              }
              **public** **void** doStuff() { System.out.println(**"Base.doStuff()"**); }
            }
    

  
  

And the program's output:  

    
    
            Base constructor: before doStuff
            Extension.doStuff() before: value = 0
            Base.doStuff()
            Extension.doStuff() after: value = 0
            Base constructor: after doStuff
            Extension constructor: value = 100
    

  
  

If you haven't figured out what is going on here, I'll explain. The value field of the Extension class is assigned an initial value of 100. But when the value is first referenced in Extension's doStuff() method, the value is mysteriously 0. The reason, it turns out, is because field initializations are not actually performed until _after_ the superclass constructor completes. But in this case, the superclass constructor calls doStuff(), which has been overridden in Extension, so that the doStuff() method is actually executed _before_ the superclass constructor finishes! This results in value still being 0 (the default, initial value for ints in Java), instead of 100. This behavior is counterintuitive -- even though the declaration of value and its initial assignment to 100 are on the same line of source code, these steps are split up significantly.  
  

It took me an hour to understand this behavior in the context of my software, and I'm still trying to think of a clean way to work around it. Ideally, I would like to assign the field's initial value before the superclass constructor finishes. There are several ways I know of to do that, but they are all bad design. So instead, I will probably end up redefining what the different values of the variable mean, such that when value is zero, it performs the behavior currently performed when value == 100, and vice versa. It's just annoying that the Java language's implementation is causing my data model to bend over backwards here.  
  

Edit: Actually, this problem is solvable simply by adding another field:  

    
    
              **private** **boolean** valuesAssigned = **true** ;
    

  
  

Then you can check whether the values have been assigned yet with a simple "if (valuesAssigned)" branch, since the default initial boolean value in Java is false. I am doing something similar but less hackish for my solution.  
  

And actually, this situation can get even messier if you decide to change the value within Extension's doStuff() method. If you put something like "value = 25;" at the end of Extension.doStuff(), then run the program, it will still be 100 within Extension's constructor after super(), because the initial value assignment takes place implicitly after super() wraps up, overwriting the assignment of 25 earlier! Talk about a snake in the grass.  
  
  

* * *

"If Java had true garbage collection, most programs would delete themselves upon execution."  
  
\--Robert Sewell
