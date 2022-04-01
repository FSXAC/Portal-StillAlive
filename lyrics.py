
from ascii_art import *

# lyrics downloaded also from https://combineoverwiki.net/wiki/Still_Alive

class TimedLyric:
    def __init__(self, text, duration=2, pause=0, ascii_art=None):
        self.text = text
        self.duration = duration if text != '<clear>' else 0
        self.pause = pause if text != '<clear>' else 0
        self.ascii_art = ascii_art
    
    def totalDuration(self):
        return self.duration + self.pause


still_alive_lyrics = [
    TimedLyric("<clear>", ascii_art=ascii_empty),
    TimedLyric("Forms FORM-29827281-12:\nTest Assessment Report\n\n\n\n", duration=6, pause=2),
    TimedLyric("This was a triumph.\n", duration=1, pause=2),
    TimedLyric("I'm making a note here:\n", duration=2.3),
    TimedLyric("HUGE SUCCESS.\n", duration=1.8, pause=1),
    TimedLyric("It's hard to overstate\n", duration=2.5),
    TimedLyric("my satisfaction.\n", duration=2.5, pause=2.3),
    TimedLyric("Aperture Science\n", duration=1.6, pause=2.1, ascii_art=ascii_aperture),
    TimedLyric("We do what we must\n", duration=1.7),
    TimedLyric("because we can.\n", duration=1.9, pause=1.6),
    TimedLyric("For the good of all of us.\n", duration=2.9, pause=0.4),
    TimedLyric("Except the ones who are dead.\n\n", duration=1.8, pause=0.4, ascii_art=ascii_radiation),
    TimedLyric("But there's no sense crying\n", duration=1.8),
    TimedLyric("over every mistake.\n", duration=1.7),
    TimedLyric("You just keep on trying\n", duration=2.1),
    TimedLyric("till you run out of cake.\n",duration=1.8),
    TimedLyric("And the Science gets done.\n", ascii_art=ascii_atom),
    TimedLyric("And you make a neat gun.\n"),
    TimedLyric("For the people who are\n", duration=1.6, ascii_art=ascii_aperture),
    TimedLyric("still alive.\n", duration=1.5, pause=1.5),
    TimedLyric("<clear>"),

    TimedLyric("Forms FORM-55551-5:\nPersonnel File Addendum:\n\n", duration=2.7, pause=0.6),
    TimedLyric("Dear <<Subject Name Here>>,\n\n\n", duration=2.4),
    TimedLyric("I'm not even angry.\n", duration=1.9, pause=2.3),
    TimedLyric("I'm being so sincere right now.\n", duration=3.5, pause=1.5),
    TimedLyric("Even though you broke my heart.\n", duration=3.5, ascii_art=ascii_broken_heart),
    TimedLyric("And killed me.\n", duration=1.5, pause=2.1),
    TimedLyric("And tore me to pieces.\n", duration=1.6, pause=2.3, ascii_art=ascii_explosion),
    TimedLyric("And threw every piece into a fire.\n", duration=3.6, pause=1.6, ascii_art=ascii_fire),
    TimedLyric("As they burned it hurt because\n", duration=2.9),
    TimedLyric("I was so happy for you!\n", duration=1.6, pause=0.8, ascii_art=ascii_checkmark),
    TimedLyric("Now these points of data\n"),
    TimedLyric("make a beautiful line.\n"),
    TimedLyric("And we're out of beta.\n"),
    TimedLyric("We're releasing on time.\n"),
    TimedLyric("So I'm GLaD. I got burned.\n", ascii_art=ascii_explosion),
    TimedLyric("Think of all the things we learned\n", ascii_art=ascii_atom),
    TimedLyric("for the people who are\n", duration=1.5, ascii_art=ascii_aperture),
    TimedLyric("still alive.\n", pause=1.4),
    TimedLyric("<clear>"),

    TimedLyric("Forms FORM-55551-6:\nPersonnel File Addendum Addendum:\n\n", duration=1.7, pause=0.8),
    TimedLyric("One last thing:\n\n\n", duration=2.2),
    TimedLyric("Go ahead and leave me.\n", duration=1.8, pause=2.1),
    TimedLyric("I think I prefer to stay inside.\n", duration=3.4, pause=1.6),
    TimedLyric("Maybe you'll find someone else\n", duration=3.5),
    TimedLyric("to help you.\n", duration=1.2, pause=2.2),
    TimedLyric("Maybe Black Mesa...\n", duration=2, pause=2, ascii_art=ascii_black_mesa),
    TimedLyric("THAT WAS A JOKE.", duration=1.7, pause=1),
    TimedLyric(" FAT CHANCE.\n", duration=1.3, pause=1.4),
    TimedLyric("Anyway, this cake is great.\n", duration=3.2, ascii_art=ascii_cake),
    TimedLyric("It's so delicious and moist.\n", duration=1.9),
    TimedLyric("Look at me still talking\n", duration=2.4, ascii_art=ascii_glados),
    TimedLyric("when there's Science to do.\n", duration=2, ascii_art=ascii_radiation),
    TimedLyric("When I look out there,\n", duration = 1.6, ascii_art=ascii_aperture),
    TimedLyric("it makes me GLaD I'm not you.\n", duration = 2.2),
    TimedLyric("I've experiments to run.\n", duration=2.1, ascii_art=ascii_atom),
    TimedLyric("There is research to be done.\n", ascii_art=ascii_explosion),
    TimedLyric("On the people who are\n", duration=1.7, ascii_art=ascii_aperture),
    TimedLyric("still alive.\n", duration=1.2, pause=0.8),

    TimedLyric("<clear>"),
    TimedLyric("\n\n\n\nPS: And believe me I am\n", duration=2.1),
    TimedLyric("still alive.\n", duration=1.1, pause=1),
    TimedLyric("PPS: I'm doing Science and I'm\n", duration=1.9),
    TimedLyric("still alive.\n", duration=1, pause=1.1),
    TimedLyric("PPPS: I feel FANTASTIC and I'm\n", duration=1.9),
    TimedLyric("still alive.\n\n", duration=1, pause=1.3),
    TimedLyric("FINAL THOUGHT:\nWhile you're dying I'll be\n", duration=1.7),
    TimedLyric("still alive.\n\n", duration=1.3, pause=0.8),
    TimedLyric("FINAL THOUGHT PS:\nAnd when you're dead I will be\n", duration=1.9),
    TimedLyric("still alive.\n\n", duration=1, pause=1),
    TimedLyric("STILL ALIVE\n\n", duration=1.4),
    TimedLyric("<clear>"),
    TimedLyric(" ", duration=10)
]