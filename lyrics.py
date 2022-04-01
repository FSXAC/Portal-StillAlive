from ascii_art import *

# lyrics downloaded also from https://combineoverwiki.net/wiki/Still_Alive

class TimedLyric:
    def __init__(self, text, duration=0.5, pause=0, ascii_art=None):
        self.text = text
        self.duration = duration
        self.pause = pause
        self.ascii_art = ascii_art
    
    def totalDuration(self):
        return self.duration + self.pause


still_alive_lyrics = [
    TimedLyric("<clear>", ascii_art=ascii_empty),
    TimedLyric("Forms FORM-29827281-12:\nTest Assessment Report\n\n\n", duration=7),
    TimedLyric("This was a triumph.\n", duration=2, pause=2),
    TimedLyric("I'm making a note here:\n"),
    TimedLyric("HUGE SUCCESS.\n"),
    TimedLyric("It's hard to overstate\n"),
    TimedLyric("my satisfaction.\n"),
    TimedLyric("Aperture Science\n", ascii_art=ascii_aperture),
    TimedLyric("We do what we must\n"),
    TimedLyric("because we can.\n"),
    TimedLyric("For the good of all of us.\n"),
    TimedLyric("Except the ones who are dead.\n\n", ascii_art=ascii_radiation),
    TimedLyric("But there's no sense crying\n"),
    TimedLyric("over every mistake.\n"),
    TimedLyric("You just keep on trying\n"),
    TimedLyric("till you run out of cake.\n"),
    TimedLyric("And the Science gets done.\n", ascii_art=ascii_atom),
    TimedLyric("And you make a neat gun.\n"),
    TimedLyric("For the people who are\n", ascii_art=ascii_aperture),
    TimedLyric("still alive.\n"),
    TimedLyric("<clear>"),
    # TimedLyric("<pause>"),

    TimedLyric("Forms FORM-55551-5:\nPersonnel File Addendum:\n\nDear <<Subject Name Here>>,\n\n\n"),
    TimedLyric("I'm not even angry.\n"),
    TimedLyric("I'm being so sincere right now.\n"),
    TimedLyric("Even though you broke my heart.\n", ascii_art=ascii_broken_heart),
    TimedLyric("And killed me.\n"),
    TimedLyric("And tore me to pieces.\n", ascii_art=ascii_explosion),
    TimedLyric("And threw every piece into a fire.\n", ascii_art=ascii_fire),
    TimedLyric("As they burned it hurt because\n"),
    TimedLyric("I was so happy for you!\n", ascii_art=ascii_checkmark),
    TimedLyric("Now these points of data\n"),
    TimedLyric("make a beautiful line.\n"),
    TimedLyric("And we're out of beta.\n"),
    TimedLyric("We're releasing on time.\n"),
    TimedLyric("So I'm GLaD. I got burned.\n", ascii_art=ascii_explosion),
    TimedLyric("Think of all the things we learned\n", ascii_art=ascii_atom),
    TimedLyric("for the people who are\n", ascii_art=ascii_aperture),
    TimedLyric("still alive.\n"),
    TimedLyric("<clear>"),

    TimedLyric("Forms FORM-55551-6:\nPersonnel File Addendum Addendum:\n\nOne last thing:\n\n\n"),
    TimedLyric("Go ahead and leave me.\n"),
    TimedLyric("I think I prefer to stay inside.\n"),
    TimedLyric("Maybe you'll find someone else\n"),
    TimedLyric("to help you.\n"),
    TimedLyric("Maybe Black Mesa...\n", ascii_art=ascii_black_mesa),
    TimedLyric("THAT WAS A JOKE. HA HA. FAT CHANCE.\n"),
    TimedLyric("Anyway, this cake is great.\n", ascii_art=ascii_cake),
    TimedLyric("It's so delicious and moist.\n"),
    TimedLyric("Look at me still talking\n", ascii_art=ascii_glados),
    TimedLyric("when there's Science to do.\n", ascii_art=ascii_radiation),
    TimedLyric("When I look out there,\n", ascii_art=ascii_aperture),
    TimedLyric("it makes me GLaD I'm not you.\n"),
    TimedLyric("I've experiments to run.\n", ascii_art=ascii_atom),
    TimedLyric("There is research to be done.\n", ascii_art=ascii_explosion),
    TimedLyric("On the people who are\n", ascii_art=ascii_aperture),
    TimedLyric("still alive.\n"),

    TimedLyric("<clear>"),
    TimedLyric("\n\n\n\n"),
    TimedLyric("PS: And believe me I am\n"),
    TimedLyric("still alive.\n"),
    TimedLyric("PPS: I'm doing Science and I'm\n"),
    TimedLyric("still alive.\n"),
    TimedLyric("PPPS: I feel FANTASTIC and I'm\n"),
    TimedLyric("still alive.\n\n"),
    TimedLyric("FINAL THOUGHT:\nWhile you're dying I'll be\n"),
    TimedLyric("still alive.\n\n"),
    TimedLyric("FINAL THOUGHT PS:\nAnd when you're dead I will be\n"),
    TimedLyric("still alive.\n\n"),
    TimedLyric("STILL ALIVE\n\n"),
    TimedLyric("Still alive.\n\n")
]