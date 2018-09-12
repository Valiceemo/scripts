#!/bin/sh

# COLORS
blackText=$(tput setaf 0)   # Black
redText=$(tput setaf 1)     # Red
greenText=$(tput setaf 2)   # Green
yellowText=$(tput setaf 3)  # Yellow
blueText=$(tput setaf 4)    # Blue
magentaText=$(tput setaf 5) # Magenta
cyanText=$(tput setaf 6)    # Cyan
whiteText=$(tput setaf 7)   # White
resetText=$(tput sgr0)      # Reset to default color

TICK="[${greenText}✓${resetText}]"
INFO="[i]"
DONE="${greenText}  done!${resetText}"

str="Consolidating blocklists"
echo -ne "  ${INFO} ${str}..."
str="All done here big man"
echo "  ${TICK} ${str}
