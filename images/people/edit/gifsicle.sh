gifsicle -U input.gif "#-2-1" -o reverse.gif
gifsicle -d 9 input.gif reverse.gif > boomerang.gif
gifsicle -U boomerang.gif `seq -f "#%g" 0 3 999` -O2 -o output.gif
# gifsicle -U --flip-horizontal mike.gif > mike2.gif
rm boomerang.gif
rm reverse.gif
