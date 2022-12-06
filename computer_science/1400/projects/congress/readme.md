Project 4: Library of Congress
The rubric has changed since this project’s original release to include the requirement to not print to the terminal.
Expected duration: 3-6 hours
Problem
You are working in the Library of Congress as a data entry intern. The library is looking to overhaul some of their older works and wants to make sure that they are correct and get some basic data from each file. As you open your assigned files, you discover that they have all been scrambled together. The lines from each of your three texts have been placed in random order and the only clue that you have is the identifier at the end of each line.
Each line in the scrambled file contains the line in the text file, a line number, and a three-letter code that identifies the work.
Each of these items is separated by the | character. For example,
it ran away when it saw mine coming!"|164|ALC
cried to the man who trundled the barrow; "bring up alongside and help|27|TRI
"Of course he's stuffed," replied Dorothy, who was still angry.|46|WOO

Your task is to write a program that reads each line in a text file (specified in sys.argv), separates and unscrambles the texts, and collects the basic data you’d first set out to collect. For each text, you must determine
Its longest line (and the corresponding line number),
its shortest line (and corresponding line number), and
the average length of the lines in the entire text.

If there are multiple lines with the shortest or longest length, use the line number as a tiebreaker: earlier lines are “shorter” and later lines are "longer".
The summary of data should be stored in a file named novel_summary.txt. The summaries should be sorted by three-letter code and should be formatted as follows:
ALC
Longest Line (107): "No, I didn’t," said Alice: "I don’t think it’s at all a pity. I said
Shortest Line (148): to."
Average Length: 59

WOO
Longest Line (66): of my way. Whenever I’ve met a man I’ve been awfully scared; but I just
Shortest Line (71): go."
Average Length: 58

The texts themselves should be stored in a file named novel_text.txt. This file should contain the three-letter code for a work followed by its text. The lines must all be included and should be ordered and should not include line numbers or three-letter codes. The texts should be separated by a single line with five - characters. The result should look like the following:
ALC
A large rose-tree stood near the entrance of the garden: the roses
growing on it were white, but there were three gardeners at it, busily
painting them red. Alice thought this a very curious thing, and she
went nearer to watch them, and just as she came up to them she heard
one of them say, "Look out now, Five! Don’t go splashing paint over me
like that!"
"I couldn’t help it," said Five, in a sulky tone; "Seven jogged my
elbow."
On which Seven looked up and said, "That’s right, Five! Always lay the

blame on others!"
TRI
SQUIRE TRELAWNEY, Dr. Livesey, and the rest of these gentlemen having
asked me to write down the whole particulars about Treasure Island, from
the beginning to the end, keeping nothing back but the bearings of the
island, and that only because there is still treasure not yet lifted, I
take up my pen in the year of grace 17__ and go back to the time when
my father kept the Admiral Benbow inn and the brown old seaman with the
sabre cut first took up his lodging under our roof.
I remember him as if it were yesterday, as he came plodding to the
inn door, his sea-chest following behind him in a hand-barrow--a

tall, strong, heavy, nut-brown man, his tarry pigtail falling over the
WOO
All this time Dorothy and her companions had been walking through the
thick woods. The road was still paved with yellow brick, but these were
much covered by dried branches and dead leaves from the trees, and the
walking was not at all good.
There were few birds in this part of the forest, for birds love the
open country where there is plenty of sunshine. But now and then there
came a deep growl from some wild animal hidden among the trees. These
sounds made the little girl’s heart beat fast, for she did not know
what made them; but Toto knew, and he walked close to Dorothy’s side,
and did not even bark in return.