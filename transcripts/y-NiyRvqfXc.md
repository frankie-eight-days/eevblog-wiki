---
video_id: y-NiyRvqfXc
title: Another Altium Designer ERC Bug
url: https://www.youtube.com/watch?v=y-NiyRvqfXc
source: youtube-asr
timestamps: {"0": 3, "1": 15, "2": 30, "3": 41, "4": 52, "5": 62, "6": 74, "7": 91, "8": 108, "9": 133}
---

**Dave Jones:** And it looks like I found another bug potentially. But uh just an update from the uh previous one. I um said well I updated the description for uh that bug.

**Dave Jones:** The issue seems to only be with the uh compile and individual schematic document. So the out job actually works if you set it to project here. But if you set it to sketch dock, it's just like doing the right click on the schematic document.

**Dave Jones:** And that seems to be where the bug is. But if you select project, everything's fine. So I've actually selected project here. And here it is. I've actually got um watch this.

**Dave Jones:** Okay, let's compile PCB project. And I'll show you the thing at the moment. Here is the messages we get. Okay. And just take note of what they are and how many of them are.

**Dave Jones:** And there are actually I can show you that in a sec. Oh no, I won't. Anyway, um there's going to be a few more in there if I actually run the out job.

**Dave Jones:** Now watch this. If I generate content, bingo. Look, we've got this extra stuff. Component has unused subp part. Okay. And it showed up in here as well. It's not the same.

**Dave Jones:** Now, I've actually disabled that um option. I specifically didn't want it. So in here down in where is it? With parts um here we go with parts sub unused subp part in component.

**Dave Jones:** I've set that to no report. So it should not generate that. So it's not consistent when you do it from here. It you watch this will actually vanish. These ones will vanish if I do the compile project like that.

**Dave Jones:** Oh hang on. Sorry. um not from here but in the messages in the messages window it's not there so one so there you go that's a good side byside example one of them using the out job to generate this HTML report has the unused subp parts it hasn't taken up the uh setting that I've set in the projects and I've saved everything and I haven't tried restarting the software have you

**Dave Jones:** tried turn it off and on again um no I haven't done that but it shouldn't have to so clearly there is a a discrepancy between the two different things here uh the two different uh ways to run that ERC and that's got to be yet another bug surely.
