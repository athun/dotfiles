#
# ~/.bashrc
#


## prelininaries

# If not running interactively, don't do anything
[[ $- != *i* ]] && return


# welcome message
python $HOME/.greet.py


# https://techcommons.stanford.edu/topics/git/show-git-branch-bash-prompt

# "\[\033[0;34m\]"

. ~/git-prompt.sh
export GIT_PS1_SHOWDIRTYSTATE=1
#export PS1='[\u  \w$(__git_ps1 " (%s)")]\$ '
export PS1='\[\e[0m\][\u:\[\e[1m\]\w\[\e[0m\]$(__git_ps1 " \[\e[32m\]%s\[\e[0m\]")]\$\[\e[0m\] '






# >>>>BEGIN ADDED BY CNCHI INSTALLER<<<< #
BROWSER=/usr/bin/firefox
EDITOR=/usr/bin/vim
# >>>>>END ADDED BY CNCHI INSTALLER<<<<< #


# aliases
  alias ls='ls --color=auto'
  alias feh='feh --bg-fill'
  alias pamac='pamac-manager'
  alias subl='subl3'
  alias py='python'