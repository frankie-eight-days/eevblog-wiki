---
video_id: v1YrANSmOGY
title: EEVblog #25 - The Infinite Resistor Puzzle
url: https://www.youtube.com/watch?v=v1YrANSmOGY
source: youtube-asr
---

**Dave Jones:** Hi, welcome to the AEV blog. I'm your host, Dave Jones, and this is episode number 25. I was reading the sci-electronics design newsgroup the other day, like I normally do, and somebody posted a question. It's a classic question that's been

**Dave Jones:** posted, you know, countless times before, and it's it's one you've probably come across in your studies. It's the infinite resistor problem. The infinite resistor problem is a classic electronics puzzle given to, you know, students. I can remember doing it, you

**Dave Jones:** know, 20-odd years ago, solving the silly thing. And and it's it's still being asked. And basically, what it is, if you haven't seen it, the infinite resistor problem is it's a grid of of actual resistors, and they're all 1

**Dave Jones:** ohm, they're all the same value. Doesn't matter what the actual value is, but they normally put 1 ohm. They're all the same value, and basically, the classic question is to measure the what is the resistance across one of the resistors

**Dave Jones:** if there's a whole grid of resistors going off in infinite directions. And well, the answer is half an ohm. Well, the answer is 0.5 * R if R is the if R is the value of the resistor. It's, you know, it's a classic

**Dave Jones:** answer to a classic problem. And there's many, you know, numerical ways to solve it. There's also, you know, some you know, rules of thumb ways to solve it as well. But the one poster of the sci-electronics group was

**Dave Jones:** not quite the classic one. It was actually what is the value between not just across the one resistor, but across diagonal points. What's the resistance across diagonal points like this? And well, you know, there were many people, you know, uh, saying it's real difficult

**Dave Jones:** to solve. And and yes, it is, you know, it's it can be quite difficult. Um, if, you know, if you try and do the math for a lot of people have to write a program to solve it, you know, you can't really

**Dave Jones:** solve it intuitively all that well. It's it's not as simple as the classic problem that's just across one resistor. And the answer actually, um, turns out, I I believe, I haven't actually gone through the math, um, actually done it myself, but, um, it it

**Dave Jones:** looks like the answer is, um, uh, two on pi times R. So, you know, 0.636 times R. Every time the question comes up, people argue about the math best mathematical solution, the most elegant, you know, the simplest to understand, the best

**Dave Jones:** concept, and yada yada yada. And well, you know, and it it just gets a bit boring, you know, all these math solutions, you know, I'm not a I'm not a huge, you know, math fan. I don't I don't like all these numerical solutions

**Dave Jones:** of to things. I'm more of a practical guy. I like it when you when people, you know, actually, you know, you can measure things. And, you know, practical stuff. So, well, I went, "Bugger it. I'm going to build it." So, here it is, the

**Dave Jones:** infinite resistor network. Check it out. Isn't it cool? It's almost a work of art.

**Dave Jones:** So, here it is. I actually went and built it. It's the infinite resistor network. Okay, granted, it's not actually infinite in scope, but, you know, anyone with any engineering, you know, nous at all can see that the problem is going to converge to a value.

**Dave Jones:** So, you know, it doesn't So, the question actually being infinite is a bit of a red herring. It doesn't really matter. It's going to converge pretty quickly to a single value. And, you know, so I couldn't obviously build an

**Dave Jones:** infinite one, but I did have a box of 500 odd 500 odd 10k resistors. So, I thought I'd build this sucker and see what I got. So, this is actually a 14 by 14 grid. It's got 420 resistors total. So, you

**Dave Jones:** know, it's not a bad representation. I thought, you know, you've probably at least got to go in order of magnitude you know, in size. So, you know, I figured you know, 10 by 10 would probably do it. It it should easily do

**Dave Jones:** it actually. But, you know, this is all all the resistors I I could scrounge together. They're 10k 1% resistors. Very high quality ones. And so, I lashed this together. It took me about like an hour to build this. So,

**Dave Jones:** you know, some people actually take longer to actually solve it on paper. So, you know, it can be quicker to actually build the thing that it can be to solve it if you're not very good at math. And you know, you get stuck and

**Dave Jones:** you're trying to solve the damn thing. So, let's have a look and see what we can measure. Right, so here it is. Let's try and do some measurements, shall we? Okay, I've got let's do the standard question which

**Dave Jones:** is across a single resistor here. Okay, as you can see it's it should be 0.5 times R and R is 10k. So, we should be getting 5k. And there you go, I get 5.034 k. And if you put it across another one,

**Dave Jones:** there's going to be some differences there. There you go, 5.017 and you just move it around. 5.02 and that's all within the tolerance you'd expect for such a grid. There you go, 5.029 etc. etc. Now, if you go

**Dave Jones:** further out on the grid, let's try that. 5.03 it's you know, it's pretty similar. So, let's go out let's go out somewhere else. Measure it again and 5.05. So, you start getting towards um um a non uh you know, it's once you get towards the

**Dave Jones:** edges, you don't get that ideal value. There you go, 5.134 K. Okay, so let's try the big one, the uh diagonally opposite um points, and we should get um two on pi, or in you know, in the case of this grid with 10 K

**Dave Jones:** resistors, 6. um 37 K or thereabouts. Now, here, let's try it. 6.41, that's within uh that's within our 1% tolerance. Let's try it again somewhere else. 6.41, it looks like we're getting, you know, fairly close, fairly consistent values in all

**Dave Jones:** directions. 6.42, they're all within 1%. Let's go elsewhere on the grid and try it. 6.42, so there you go. It's it's confirmed. It's um it looks like it's within it is actually uh two on pi. As you get

**Dave Jones:** towards the edge, you can see it go up. It's now out of tolerance, 6.71, because we don't have enough resistors in this direction here. So, um you know, but pretty much if you get within, you know, um three or four

**Dave Jones:** resistors outside the well away from the edge, you get fairly close to your expected value. Right, okay, let's measure the other one now, the one with the um second diagonal up. So, it's actually one up and two across. Now, this one should be um

**Dave Jones:** uh 7.732 K, and it's not. It's actually 7.853, as you can see, and that's actually um outside the uh 1% um spec, which we were meeting well before. And if we move it around like this again, it's um it's going up a

**Dave Jones:** bit. And if we keep going towards an edge, there we go. We're well outside of spec. So, this one, it looks like the the further out you go, the further spread you do inside the grid, the greater the

**Dave Jones:** tolerance you're the actual tolerance you're out on a on a fixed size grid. So, there you go. So, as you can see, the results were rather interesting. It actually showed the limitations of this fixed size grid or it

**Dave Jones:** or it appears to when we had the single resistor, we were pretty close to spot on to what we actually expected. Once we went on the diagonal, we were a bit higher than what we actually expected. And then once once we went up one and

**Dave Jones:** across two, we were even higher again. In theory, you know, outside of the spec and what we actually expected. So, there you go. The limitations of a fixed size grid. But, it's still pretty cool. So, there you go. That was a whole bunch of

**Dave Jones:** fun. I love it when you can actually measure things. It's terrific. It's much better than just solving it on paper. This is what electronics is all about. Practicality. I think I've really grown quite attached to this. It really is quite a work of

**Dave Jones:** art. I like it. I think I might actually frame it.
