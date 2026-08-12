---
video_id: v1YrANSmOGY
title: EEVblog #25 - The Infinite Resistor Puzzle
url: https://www.youtube.com/watch?v=v1YrANSmOGY
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 33, "3": 50, "4": 67, "5": 82, "6": 95, "7": 116, "8": 127, "9": 147, "10": 163, "11": 172, "12": 181, "13": 194, "14": 218, "15": 226, "16": 241, "17": 255, "18": 267, "19": 284, "20": 292, "21": 303, "22": 315, "23": 328, "24": 344, "25": 356, "26": 369, "27": 390, "28": 404, "29": 428, "30": 443, "31": 460, "32": 483, "33": 500, "34": 513, "35": 522, "36": 534}
---

**Dave Jones:** Hi, welcome to the AEV blog. I'm your host, Dave Jones, and this is episode number 25. I was reading the sci-electronics design newsgroup the other day, like I normally do, and somebody posted a question.

**Dave Jones:** It's a classic question that's been posted, you know, countless times before, and it's it's one you've probably come across in your studies. It's the infinite resistor problem. The infinite resistor problem is a classic electronics puzzle given to, you know, students.

**Dave Jones:** I can remember doing it, you know, 20-odd years ago, solving the silly thing. And and it's it's still being asked. And basically, what it is, if you haven't seen it, the infinite resistor problem is it's a grid of of actual resistors, and they're all 1 ohm, they're all the same value.

**Dave Jones:** Doesn't matter what the actual value is, but they normally put 1 ohm. They're all the same value, and basically, the classic question is to measure the what is the resistance across one of the resistors if there's a whole grid of resistors going off in infinite directions.

**Dave Jones:** And well, the answer is half an ohm. Well, the answer is 0.5 * R if R is the if R is the value of the resistor. It's, you know, it's a classic answer to a classic problem.

**Dave Jones:** And there's many, you know, numerical ways to solve it. There's also, you know, some you know, rules of thumb ways to solve it as well. But the one poster of the sci-electronics group was not quite the classic one.

**Dave Jones:** It was actually what is the value between not just across the one resistor, but across diagonal points. What's the resistance across diagonal points like this? And well, you know, there were many people, you know, uh, saying it's real difficult to solve.

**Dave Jones:** And and yes, it is, you know, it's it can be quite difficult. Um, if, you know, if you try and do the math for a lot of people have to write a program to solve it, you know, you can't really solve it intuitively all that well.

**Dave Jones:** It's it's not as simple as the classic problem that's just across one resistor. And the answer actually, um, turns out, I I believe, I haven't actually gone through the math, um, actually done it myself, but, um, it it looks like the answer is, um, uh, two on pi times R.

**Dave Jones:** So, you know, 0.636 times R. Every time the question comes up, people argue about the math best mathematical solution, the most elegant, you know, the simplest to understand, the best concept, and yada yada yada.

**Dave Jones:** And well, you know, and it it just gets a bit boring, you know, all these math solutions, you know, I'm not a I'm not a huge, you know, math fan.

**Dave Jones:** I don't I don't like all these numerical solutions of to things. I'm more of a practical guy. I like it when you when people, you know, actually, you know, you can measure things.

**Dave Jones:** And, you know, practical stuff. So, well, I went, "Bugger it. I'm going to build it." So, here it is, the infinite resistor network. Check it out. Isn't it cool?

**Dave Jones:** It's almost a work of art. So, here it is. I actually went and built it. It's the infinite resistor network. Okay, granted, it's not actually infinite in scope, but, you know, anyone with any engineering, you know, nous at all can see that the problem is going to converge to a value.

**Dave Jones:** So, you know, it doesn't So, the question actually being infinite is a bit of a red herring. It doesn't really matter. It's going to converge pretty quickly to a single value.

**Dave Jones:** And, you know, so I couldn't obviously build an infinite one, but I did have a box of 500 odd 500 odd 10k resistors. So, I thought I'd build this sucker and see what I got.

**Dave Jones:** So, this is actually a 14 by 14 grid. It's got 420 resistors total. So, you know, it's not a bad representation. I thought, you know, you've probably at least got to go in order of magnitude you know, in size.

**Dave Jones:** So, you know, I figured you know, 10 by 10 would probably do it. It it should easily do it actually. But, you know, this is all all the resistors I I could scrounge together.

**Dave Jones:** They're 10k 1% resistors. Very high quality ones. And so, I lashed this together. It took me about like an hour to build this. So, you know, some people actually take longer to actually solve it on paper.

**Dave Jones:** So, you know, it can be quicker to actually build the thing that it can be to solve it if you're not very good at math. And you know, you get stuck and you're trying to solve the damn thing.

**Dave Jones:** So, let's have a look and see what we can measure. Right, so here it is. Let's try and do some measurements, shall we? Okay, I've got let's do the standard question which is across a single resistor here.

**Dave Jones:** Okay, as you can see it's it should be 0.5 times R and R is 10k. So, we should be getting 5k. And there you go, I get 5.034 k.

**Dave Jones:** And if you put it across another one, there's going to be some differences there. There you go, 5.017 and you just move it around. 5.02 and that's all within the tolerance you'd expect for such a grid.

**Dave Jones:** There you go, 5.029 etc. etc. Now, if you go further out on the grid, let's try that. 5.03 it's you know, it's pretty similar. So, let's go out let's go out somewhere else.

**Dave Jones:** Measure it again and 5.05. So, you start getting towards um um a non uh you know, it's once you get towards the edges, you don't get that ideal value.

**Dave Jones:** There you go, 5.134 K. Okay, so let's try the big one, the uh diagonally opposite um points, and we should get um two on pi, or in you know, in the case of this grid with 10 K resistors, 6.

**Dave Jones:** um 37 K or thereabouts. Now, here, let's try it. 6.41, that's within uh that's within our 1% tolerance. Let's try it again somewhere else. 6.41, it looks like we're getting, you know, fairly close, fairly consistent values in all directions.

**Dave Jones:** 6.42, they're all within 1%. Let's go elsewhere on the grid and try it. 6.42, so there you go. It's it's confirmed. It's um it looks like it's within it is actually uh two on pi.

**Dave Jones:** As you get towards the edge, you can see it go up. It's now out of tolerance, 6.71, because we don't have enough resistors in this direction here. So, um you know, but pretty much if you get within, you know, um three or four resistors outside the well away from the edge, you get fairly close to your expected value.

**Dave Jones:** Right, okay, let's measure the other one now, the one with the um second diagonal up. So, it's actually one up and two across. Now, this one should be um uh 7.732 K, and it's not.

**Dave Jones:** It's actually 7.853, as you can see, and that's actually um outside the uh 1% um spec, which we were meeting well before. And if we move it around like this again, it's um it's going up a bit.

**Dave Jones:** And if we keep going towards an edge, there we go. We're well outside of spec. So, this one, it looks like the the further out you go, the further spread you do inside the grid, the greater the tolerance you're the actual tolerance you're out on a on a fixed size grid.

**Dave Jones:** So, there you go. So, as you can see, the results were rather interesting. It actually showed the limitations of this fixed size grid or it or it appears to when we had the single resistor, we were pretty close to spot on to what we actually expected.

**Dave Jones:** Once we went on the diagonal, we were a bit higher than what we actually expected. And then once once we went up one and across two, we were even higher again.

**Dave Jones:** In theory, you know, outside of the spec and what we actually expected. So, there you go. The limitations of a fixed size grid. But, it's still pretty cool. So, there you go.

**Dave Jones:** That was a whole bunch of fun. I love it when you can actually measure things. It's terrific. It's much better than just solving it on paper. This is what electronics is all about.

**Dave Jones:** Practicality. I think I've really grown quite attached to this. It really is quite a work of art. I like it. I think I might actually frame it.
