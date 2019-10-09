gifsicle -U input.gif "#-2-1" -o reverse.gif
gifsicle -d 11 input.gif reverse.gif > boomerang.gif
gifsicle -U boomerang.gif `seq -f "#%g" 0 3 999` -O2 -o output.gif
rm boomerang.gif
rm reverse.gif
